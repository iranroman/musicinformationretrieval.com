"""Utility files and functions used across all notebooks"""

import os

import matplotlib.pyplot as plt
import requests

API_URL = "https://api.github.com/repos/iranroman/musicinformationretrieval.com/git/trees/gh-pages?recursive=1"
BASE_URL = "https://musicinformationretrieval.com"


def init():
    """
    Initialisation function called inside many notebooks.

    Sets plotting style, downloads assets.
    """
    set_plt_style()
    download_audio()
    download_images()


def set_plt_style():
    plt.style.use('seaborn-v0_8-muted')
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.bottom'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.xmargin'] = 0
    plt.rcParams['axes.ymargin'] = 0
    plt.rcParams['image.cmap'] = 'gray'
    plt.rcParams['image.interpolation'] = "none"


def download_audio():
    # Get the JSON tree data from GitHub API
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    # Filter paths that are blobs (files) and inside 'audio/' folder
    paths = [item['path'] for item in data['tree'] if item['type'] == 'blob' and item['path'].startswith('assets/audio/')]

    for path in paths:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Download file and save
        file_url = f"{BASE_URL}/{path}"
        r = requests.get(file_url)
        r.raise_for_status()

        with open(path, "wb") as f:
            f.write(r.content)


def download_images():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    # Filter paths that are blobs (files) and inside 'audio/' folder
    paths = [item['path'] for item in data['tree'] if item['type'] == 'blob' and item['path'].startswith('assets/img/')]

    for path in paths:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Download file and save
        file_url = f"{BASE_URL}/{path}"
        r = requests.get(file_url)
        r.raise_for_status()

        with open(path, "wb") as f:
            f.write(r.content)
