"""Test that all links in a notebook are valid and do not 404"""

import json
import requests
import pytest
from pathlib import Path
from urlextract import URLExtract

NOTEBOOKS = Path("mirdotcom/content").rglob("*.ipynb")


def extract_links_from_notebook(nb_path: Path):
    """
    Extract all HTTP/HTTPS URLs from markdown and code cells.
    """
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

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
def test_links_are_valid(nb):
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
