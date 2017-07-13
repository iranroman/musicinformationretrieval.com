stanford-mir
============

Instructional material for the [Music Information Retrieval Workshop](https://ccrma.stanford.edu/workshops/music-information-retrieval-2017) at CCRMA, Stanford University, 2014-17. The 2017 workshop is sold out and beyond capacity. Sorry.


How to Use This Repo
--------------------

This repository contains Jupyter notebooks related to music information retrieval (MIR). Inside these notebooks are Python code snippets that illustrate basic MIR systems.

The simplest way to use this repository is to (1) browse a read-only version of this repo at [musicinformationretrieval.com](http://musicinformationretrieval.com), and (2) follow along using a blank Jupyter notebook of your own.

### Start the Jupyter Notebook

A majority of our instruction and laboratory work will occur inside the [Jupyter notebook](http://jupyter.org/). You can think of the Jupyter notebook like the Mathematica or Matlab desktop, except it uses Python and it runs inside your web browser.

1.  Start the Jupyter notebook server on your local machine:

        stanford-mir:~$ jupyter notebook

2.  On your local machine, visit <http://localhost:8888> inside a web browser. 

3.  To open a new notebook, click on *New* near the top right. This is your scrap notebook. Try executing the content from <musicinformationretrieval.com> inside this blank notebook.

Congratulations, you are now running a Jupyter notebook, and you can get started with the workshop material.


Contributions
-------------

Your contributions are very welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/stanford-mir/issues)" in the right navigation bar, then "New Issue".  Issues can include Python bugs, spelling mistakes, broken links, requests for new content, and more.  For a prioritized list of open issues awaiting contribution, click on the blue "[Ready](https://waffle.io/stevetjoa/stanford-mir)" button above.

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).

This repo is statically hosted using [GitHub Pages](https://pages.github.com/). Any changes to HTML files in the `gh-pages` branch will be seen on [musicinformationretrieval.com](http://musicinformationretrieval.com).

To edit musicinformationretrieval.com:

1.  Edit a notebook, e.g.:

        $ ipython notebook kmeans.ipynb

2.  Convert notebook to HTML:

        $ ipython nbconvert --to html kmeans.ipynb

3.  Commit the notebook and the HTML:

        $ git add kmeans.ipynb kmeans.html
        $ git commit
        $ git push

    You may need to wait 1-2 minutes before the changes are live on GitHub Pages.

