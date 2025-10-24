"""Utility files and functions used across all notebooks"""

import matplotlib.pyplot as plt
import os


def init():
    """
    Initialisation function called inside many notebooks.

    Sets plotting style.
    """
    set_plt_style()


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


def set_working_directory():
    """
    Thebe working directory is by default set to the repository root

    We need to set it correctly so that filepaths/assets can be loaded correctly
    """
    # Just change the directory so that ../../assets will work OK
    if "mirdotcom" not in os.listdir(os.getcwd()):
        os.chdir(os.path.join(os.getcwd(), "mirdotcom/content/1_introduction"))
