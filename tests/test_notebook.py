"""
Test notebook formatting and contents.

Note that this **does not** run the notebooks directly; `nbmake` is used for that instead. These tests simply
check basic formatting (e.g., do any HTML links 404, are any cells empty, do we have a title, etc.)
"""

import json
import re
from pathlib import Path

import pytest
import requests
from urlextract import URLExtract

NOTEBOOKS = list(Path("mirdotcom/content").rglob("*.ipynb"))

AVOID_TAGS = ["hide-input", "hide_input", "hide-output", "hide_output", "hide-cell", "hide_cell"]
HEADING_PATTERN = re.compile(r'^(#+)\s+')


def load_notebook(nb_path: Path) -> dict:
    """
    Loads a notebook up as a JSON dictionary
    """
    with open(nb_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize("nb_path", NOTEBOOKS)
def test_tags(nb_path: Path):
    """
    Notebooks should not use 'hide-*' tags
    """
    nb = load_notebook(nb_path)
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            if cell["metadata"] and "tags" in cell["metadata"]:
                for tag in cell["metadata"]["tags"]:
                    for avoid_tag in AVOID_TAGS:
                        assert tag != avoid_tag


@pytest.mark.parametrize("nb_path", NOTEBOOKS)
def test_title(nb_path: Path):
    """
    First cell in notebook should be a title
    """
    nb = load_notebook(nb_path)

    cell1 = nb["cells"][0]
    assert cell1["cell_type"] == "markdown"

    content = cell1["source"]
    if isinstance(content, list):
        content = content[0]
    # First two characters should be header characters
    assert content[0:2] == "# "


@pytest.mark.parametrize("nb_path", NOTEBOOKS)
def test_imports_mirdotcom(nb_path: Path):
    """
    If the notebook contains code, "mirdotcom" should be imported and `mirdotcom.init()` called.
    """
    nb = load_notebook(nb_path)

    code_contents = []
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            code_contents.extend([i.strip() for i in cell["source"]])
    if len(code_contents) > 0:
        assert any("import mirdotcom" in s for s in code_contents)


def extract_links_from_notebook(nb_path: Path):
    """
    Extract all HTTP/HTTPS URLs from markdown and code cells.
    """
    nb = load_notebook(nb_path)

    extractor = URLExtract()
    links = set()

    for cell in nb.get("cells", []):
        if "source" in cell:
            text = "".join(cell["source"])
            for url in extractor.find_urls(text):
                # Skips over cases where code (e.g., `IPython.display.Audio`) was picked up as URL
                if not url.startswith("http"):
                    continue
                links.add(url)

    return sorted(links)


def check_url(url, nb, timeout=5):
    """
    Return status code or raise pytest failure.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    try:
        resp = requests.head(url, headers=headers, allow_redirects=True, timeout=timeout)
        if resp.status_code >= 400 or resp.status_code < 200:
            # Some sites block HEAD requests: fallback to GET
            resp = requests.get(url, headers=headers, allow_redirects=True, timeout=timeout)
        return resp.status_code
    except requests.RequestException as e:
        pytest.fail(f"Error checking notebook {nb}, {url}: {e}")


@pytest.mark.parametrize("nb", NOTEBOOKS)
def test_links_are_valid(nb: Path):
    """
    Each link in the notebook should return a 2xx or 3xx status code.
    """
    urls = extract_links_from_notebook(nb)
    for url in urls:
        # Wikipedia URLs may have format e.g. "Pitch_(music)", but the regex
        #  spits out "Pitch_(music", which 404s, so just use the root page
        if "wikipedia" in url and "(" in url:
            url = url.split("_")[0]

        status = check_url(url, nb)
        if status in (999, 403):
            print(f"{url} blocked automated access (status {status})")
            continue
        assert 200 <= status < 400, f"Notebook {nb}, {url} returned {status}"


@pytest.mark.parametrize("nb", NOTEBOOKS)
def test_no_empty_cells(nb: Path):
    """
    No cells should be empty.
    """

    nb = load_notebook(nb)
    for cell in nb["cells"]:
        if cell["source"] == "":
            pass
        assert cell["source"] != ""


def extract_markdown_headings(nb: dict):
    """
    Extract Markdown heading levels (1 for '#', 2 for '##', etc.) from a notebook.
    """
    heading_levels = []
    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            content = cell["source"]
            if not isinstance(content, list):
                content = [content]

            for source in content:
                for line in source.splitlines():
                    match = HEADING_PATTERN.match(line.strip())
                    if match:
                        heading_levels.append(len(match.group(1)))

    return heading_levels


def check_linear_ascent(levels):
    """
    Ensure heading levels ascend or descend linearly (by 1 at most).
    """
    for prev, curr in zip(levels, levels[1:]):
        diff = curr - prev
        # Allow only: same level, +1 up, or any level down
        if diff > 1:
            return False, (prev, curr)
    return True, None


@pytest.mark.parametrize("notebook_path", NOTEBOOKS)
def test_markdown_headings_linear(notebook_path):
    """
    The titles in notebooks should all ascend linearly
    """
    nb = load_notebook(notebook_path)
    levels = extract_markdown_headings(nb)
    assert levels, f"No markdown headings found in {notebook_path}"

    ok, offending = check_linear_ascent(levels)
    assert ok, f"Invalid heading jump from {offending[0]} to {offending[1]} in {notebook_path}"
