musicinformationretrieval.com
=============================

`stanford-mir` is now **`musicinformationretrieval.com`.**

This repository contains instructional Jupyter notebooks related to music information retrieval (MIR). Inside these notebooks are Python code snippets that illustrate basic MIR systems.

The simplest way to use this repository is to (1) browse a read-only version of this repo at [musicinformationretrieval.com](http://musicinformationretrieval.com), and (2) follow along using a blank Jupyter notebook of your own.

Installation
------------

1.  Download and install [Anaconda for Python 3.x](https://www.anaconda.com/download).
    
2.  Install [librosa](https://librosa.github.io/librosa/install.html) and [ffmpeg](https://librosa.github.io/librosa/install.html#ffmpeg). If you installed Anaconda during step 1:

        conda install -c conda-forge librosa ffmpeg

If these packages are already installed, don't forget to upgrade them.

To upgrade, `conda upgrade`.

[2018 June 24] These notebooks reflect the following package versions:

-   numpy 1.14.2
-   scipy 1.0.0
-   matplotlib 2.2.0
-   ipython 6.2.1
-   jupyter 1.0.0
-   librosa 0.6.1
-   scikit-learn 0.19.1
-   pandas 0.22.0
-   joblib 0.11

Usage
-----

1.  Start the [Jupyter notebook](http://jupyter.org/) server on your local machine. For Mac users, at the Terminal:

        your-local-machine:~$ jupyter notebook

    For Windows users, open the application "Jupyter Notebook". Alternatively for Windows: open the application "Anaconda Prompt" and type in `jupyter notebook`.

    Jupyter should automatically open a new window in your web browser that resembles a directory tree.

2.  To open a new notebook, in the new window of your web browser, click on *New* near the top right to open a new notebook.

    -   To rename the notebook, click on "Untitled" in the top left, and choose a different name.
    -   Inside a cell, run `1+2`. Press `<Shift-Enter>` on a cell to run that cell. Hopefully you get the output `3`.
    -   Inside a cell, run `import scipy, sklearn, pandas, librosa`. Press `<Shift-Enter>` to run the cell. If that runs without error, congratulations, you have the necessary libraries installed properly.
    -   Try executing the content from <http://musicinformationretrieval.com> inside this blank notebook.

3.  To close the Jupyter notebook,

    -   Save the notebook. (Either use keyboard shortcut `s`, or "File | Save" in the top menu.)
    -   Close the browser window.
    -   If you opened the notebook from a prompt/shell as indicated in Step 1 above, from that shell, press `<Ctrl-C>` twice to return to the prompt.

Congratulations, you are now running a Jupyter notebook, and you can get started with the notebooks in this repository.

After installing, if something doesn’t work, try closing the terminal or restarting the OS. Sometimes that can reset the necessary configurations.


Troubleshooting
---------------

[Issue #729](https://github.com/librosa/librosa/issues/729): `import librosa` causes `TypeError: expected string or buffer` 

-   Workaround: downgrade `joblib` to v0.11:

        pip install joblib==0.11


Contributions
-------------

Your contributions are welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/musicinformationretrieval.com/issues)" in the right navigation bar, then "New Issue".  Issues can include Python bugs, spelling mistakes, broken links, requests for new content, and more.

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).

This repo is statically hosted using [GitHub Pages](https://pages.github.com/). Any changes to HTML files in the `gh-pages` branch will be seen on [musicinformationretrieval.com](http://musicinformationretrieval.com).

To edit musicinformationretrieval.com:

1.  Edit a notebook, e.g.:

        $ jupyter notebook kmeans.ipynb

2.  Convert notebook to HTML:

        $ jupyter nbconvert kmeans.ipynb

3.  Commit the notebook and the HTML:

        $ git add kmeans.ipynb kmeans.html
        $ git commit
        $ git push

    You may need to wait 1-2 minutes before the changes are live on GitHub Pages.

