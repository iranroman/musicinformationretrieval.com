"""Utility files and functions used across all notebooks"""

import os
from time import sleep

import matplotlib.pyplot as plt
import requests

BASE_URL = "https://musicinformationretrieval.com"
DOWNLOAD_ATTEMPTS = 10
WAIT_SECONDS = 2

ASSETS = [
    'audio/125_bounce.wav',
    'audio/58bpm.wav',
    'audio/brahms_hungarian_dance_5.mp3',
    'audio/busta_rhymes_hits_for_days.mp3',
    'audio/c_strum.wav',
    'audio/clarinet_c6.wav',
    'audio/classic_rock_beat.mp3',
    'audio/classic_rock_beat.wav',
    'audio/conga_groove.wav',
    'audio/cowbell.wav',
    'audio/funk_groove.mp3',
    'audio/jangle_pop.mp3',
    'audio/latin_groove.mp3',
    'audio/oboe_c6.wav',
    'audio/prelude_cmaj.wav',
    'audio/simple_loop.wav',
    'audio/simple_piano.wav',
    'audio/sir_duke_piano_fast.mp3',
    'audio/sir_duke_piano_slow.mp3',
    'audio/sir_duke_trumpet_fast.mp3',
    'audio/sir_duke_trumpet_slow.mp3',
    'audio/thx_original.mp3',
    'audio/tone_440.wav',
    *[f"audio/drum_samples/test/kick_{str(i).zfill(2)}.mp3" for i in range(62)],
    *[f"audio/drum_samples/test/snare_{str(i).zfill(2)}.mp3" for i in range(32)],
    *[f"audio/drum_samples/train/kick_{str(i).zfill(2)}.mp3" for i in range(1, 11)],
    *[f"audio/drum_samples/train/snare_{str(i).zfill(2)}.mp3" for i in range(1, 11)],
    'img/classic_rock_beat_drumtab.png'
]


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


def download_file(path, attempts: int = DOWNLOAD_ATTEMPTS):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Skip files if they exist on disk
    if os.path.isfile(path):
        return

    # Download file and save
    file_url = f"{BASE_URL}/{path}"

    for _ in range(attempts):
        try:
            r = requests.get(file_url)
            r.raise_for_status()

            with open(path, "wb") as f:
                f.write(r.content)
        except:
            sleep(WAIT_SECONDS)
            continue
        else:
            return

    raise ValueError(f"Could not download {path}, try again later")


def download_audio():
    # Filter paths that are blobs (files) and inside 'audio/' folder
    paths = [os.path.join("assets", item) for item in ASSETS if item.startswith("audio/")]
    for path in paths:
        download_file(path)

def download_images():
    # Filter paths that are blobs (files) and inside 'image/' folder
    paths = [os.path.join("assets", item) for item in ASSETS if item.startswith("img/")]
    for path in paths:
        download_file(path)
