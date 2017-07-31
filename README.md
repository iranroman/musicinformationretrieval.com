stanford-mir
============

Instructional material for the [Music Information Retrieval Workshop](https://ccrma.stanford.edu/workshops/music-information-retrieval-2017) at CCRMA, Stanford University, 2014-17.


How to Use This Repo
--------------------

This repository contains Jupyter notebooks related to music information retrieval (MIR). Inside these notebooks are Python code snippets that illustrate basic MIR systems.

The simplest way to use this repository is to (1) browse a read-only version of this repo at [musicinformationretrieval.com](http://musicinformationretrieval.com), and (2) follow along using a blank Jupyter notebook of your own.

### Install Python and relevant libraries

1.  If you’re totally new, the simplest solution is to download and install [Anaconda for Python 2 (2.7)](https://www.continuum.io/downloads), not Python 3. 
    
2.  Install [librosa](https://librosa.github.io/librosa/install.html) and [ffmpeg](https://librosa.github.io/librosa/install.html#ffmpeg).

If these packages are already installed, don't forget to upgrade them before the workshop.

To upgrade, use either `pip install --upgrade` or `conda upgrade` depending upon which package installer you used for the respective package.

### Start the Jupyter Notebook

A majority of our instruction and laboratory work will occur inside the [Jupyter notebook](http://jupyter.org/). You can think of the Jupyter notebook like the Mathematica or Matlab desktop, except it uses Python and it runs inside your web browser.

1.  Start the Jupyter notebook server on your local machine. For Mac users, at the Terminal:

        your-local-machine:~$ jupyter notebook

    For Windows users, open the application "Jupyter Notebook". Alternatively for Windows: open the application "Anaconda Prompt" and type in `jupyter notebook`.

2.  On your local machine, visit <http://localhost:8888> inside a web browser. 

3.  To open a new notebook, click on *New* near the top right. This is your scrap notebook. 

    -   Immediately rename the notebook by clicking on "Untitled" in the top left, and choosing a different name.
    -   Inside a cell, run `1+2`. Press `<Shift-Enter>` on a cell to run that cell. Hopefully you get the output `3`.
    -   Inside a cell, run `import scipy, sklearn, pandas, seaborn, librosa`. Press `<Shift-Enter>` to run the cell. If that runs without error, congratulations, you have the necessary libraries installed properly.
    -   Try executing the content from <http://musicinformationretrieval.com> inside this blank notebook.

4.  To close the Jupyter notebook,

    -   Save the notebook. (Either use keyboard shortcut `s`, or "File | Save" in the top menu.)
    -   Close the browser window.
    -   If you opened the notebook from a prompt/shell as indicated in Step 1 above, from that shell, press `<Ctrl-C>` twice to return to the prompt.

Congratulations, you are now running a Jupyter notebook, and you can get started with the workshop material.

After installing, if something doesn’t work, try closing the terminal or restarting the OS. Sometimes that can reset the necessary configurations.


Contributions
-------------

Your contributions are very welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/stanford-mir/issues)" in the right navigation bar, then "New Issue".  Issues can include Python bugs, spelling mistakes, broken links, requests for new content, and more.

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).

This repo is statically hosted using [GitHub Pages](https://pages.github.com/). Any changes to HTML files in the `gh-pages` branch will be seen on [musicinformationretrieval.com](http://musicinformationretrieval.com).

To edit musicinformationretrieval.com:

1.  Edit a notebook, e.g.:

        $ jupyter notebook kmeans.ipynb

2.  Convert notebook to HTML:

        $ jupyter nbconvert --to html kmeans.ipynb

3.  Commit the notebook and the HTML:

        $ git add kmeans.ipynb kmeans.html
        $ git commit
        $ git push

    You may need to wait 1-2 minutes before the changes are live on GitHub Pages.

