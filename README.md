stanford-mir
============

[![Stories in Ready](https://badge.waffle.io/stevetjoa/stanford-mir.png?label=ready&title=Ready)](https://waffle.io/stevetjoa/stanford-mir)

Instructional material for the [Music Information Retrieval Workshop](https://ccrma.stanford.edu/workshops/music-information-retrieval-mir) at CCRMA, Stanford University, 2014.


How to Use this Repo
--------------------

This repo contains a bunch of IPython notebooks related to music information retrieval.

If you're a **visitor**, [browse this repo at nbviewer.ipython.org](http://nbviewer.ipython.org/github/stevetjoa/stanford-mir) which renders the notebooks in this repo so they can be viewed in a web browser.

If you're a **workshop participant**, follow the steps below to get started with Git, Vagrant, and IPython.


### Install Git

If you don't have Git, [download Git here](http://git-scm.com), and install it on your local machine.

Clone this repo onto your local machine:

    macbook:~$ git clone https://github.com/stevetjoa/stanford-mir


### Install Vagrant

We use [Vagrant](http://vagrantup.com) to create a local virtual machine running Ubuntu 12.04. Vagrant ensures that every person has exactly the same development environment with the same installed packages. 

Vagrant is available for all major operating systems, including Windows, Mac OS X, and Linux. It's a breeze to install.

1.  Install [VirtualBox](https://www.virtualbox.org) and [Vagrant](http://vagrantup.com).

2.  Create a new virtual machine using [our customized Vagrant box](https://vagrantcloud.com/stevetjoa/stanford-mir) built upon Ubuntu 12.04 64-bit.

        macbook:~/stanford-mir$ vagrant up

    If this is your first time running `vagrant up`, this step may take five minutes to download the Vagrant box.

3.  Finally, login to the new virtual machine:

        macbook:~/stanford-mir$ vagrant ssh

    This step logs you in to Ubuntu locally as user `vagrant` with default password `vagrant`.

Note: outdated versions of Mac OS X may yield problems with `vagrant ssh`. To avoid such problems, please upgrade (for free) to the latest version of Mac OS X.


### Start IPython

A majority of our instruction and laboratory work will occur inside the [IPython notebook](http://ipython.org/notebook.html). You can think of the IPython notebook like the Mathematica or Matlab desktop, except it's in Python and it runs inside your web browser.

1.  In your Vagrant box, start the IPython notebook server:

        vagrant@stanford-mir:~$ ipython notebook

2.  On your *host* machine, visit <http://localhost:8888>. 

3.  Open the notebook `stanford-mir/Table_of_Contents.ipynb`.

Congratulations, you are now running an IPython notebook, and you can get started with the workshop material.


Contributions
-------------

Your contributions are very welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/stanford-mir/issues)" in the right navigation bar, then "New Issue".  Issues can include Python bugs, spelling mistakes, broken links, requests for new content, and more.  For a prioritized list of open issues awaiting contribution, click on the blue "[Ready](https://waffle.io/stevetjoa/stanford-mir)" button above.

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).
