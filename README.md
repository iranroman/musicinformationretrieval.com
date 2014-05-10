stanford-mir
============

[![Stories in Ready](https://badge.waffle.io/stevetjoa/stanford-mir.png?label=ready&title=Ready)](https://waffle.io/stevetjoa/stanford-mir)

Instructional material for the [Music Information Retrieval Workshop](https://ccrma.stanford.edu/workshops/music-information-retrieval-mir) at CCRMA, Stanford University, 2014.

Contributions
-------------

Your contributions are very welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/stanford-mir/issues)" in the right navigation bar, then "New Issue".  For a prioritized list of open issues awaiting contribution, click on the blue "[Ready](https://waffle.io/stevetjoa/stanford-mir)" button above.

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).


How to Use this Repo
--------------------

Basically, this repo contains a bunch of IPython notebooks related to music information retrieval.

If you're a visitor, [browse this repo at nbviewer.ipython.org](http://nbviewer.ipython.org/github/stevetjoa/stanford-mir) which renders the notebooks in this repo so they can be viewed in a web browser.

If you're a workshop participant, follow the steps below to get started with Git, Vagrant, and IPython.


Install Git
-----------

If you don't have Git, [download Git here](http://git-scm.com), and install it on your local machine.

Optional: create an account at <https://github.com>. A GitHub account allows you to contribute code back into this repo. Then, fork this repo: 

1.  Click "Fork" in the top-right corner.

2.  Clone this repo onto your local machine:

        macbook:~$ git clone https://github.com/your_github_username/stanford-mir

Otherwise, without a GitHub account, to clone this repo onto your local machine:

    macbook:~$ git clone https://github.com/stevetjoa/stanford-mir


Install Vagrant
---------------

In previous workshops, a major difficulty was installing software prequisites and handling dependencies. Everyone has a different computing setup, and we would often run into problems when installed packages conflict or prerequisites aren't met. 

This year, we will use [Vagrant](http://vagrantup.com) to create a local virtual development environment running Ubuntu 12.04. Vagrant will ensure that every person has exactly the same development environment with the same installed packages. 

Vagrant is available for all major operating systems, including Windows, Mac OS X, and Linux. It's a breeze to install.

1.  Install [VirtualBox](https://www.virtualbox.org) and [Vagrant](http://vagrantup.com).

2.  Create a new virtual machine using [our customized Vagrant box](https://vagrantcloud.com/stevetjoa/stanford-mir) built upon Ubuntu 12.04 64-bit.

        macbook:~/stanford-mir$ vagrant up

    If this is your first time running `vagrant up`, this step may take five minutes to download the Vagrant box.

3.  Finally, login to the new virtual machine:

        macbook:~/stanford-mir$ vagrant ssh

    This step logs you in to Ubuntu locally as user `vagrant` with default password `vagrant`.


Using IPython
-------------

A majority of our instruction and laboratory work will occur inside the [IPython notebook](http://ipython.org/notebook.html). You can think of the IPython notebook like the Mathematica or Matlab desktop, except it's in Python and it runs inside your web browser.

1.  In your Vagrant box, go to the `stanford-mir` directory, and start the IPython notebook server:

        vagrant@stanford-mir:~$ cd stanford-mir
        vagrant@stanford-mir:~/stanford-mir$ ipython notebook

2.  On your *host* machine, visit <http://localhost:8888>. 

Congratulations, you are now running an IPython notebook, and you can get started with the workshop material.
