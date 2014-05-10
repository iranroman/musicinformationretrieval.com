stanford-mir
============

[![Stories in Ready](https://badge.waffle.io/stevetjoa/stanford-mir.png?label=ready&title=Ready)](https://waffle.io/stevetjoa/stanford-mir)

Instruction for the Music Information Retrieval Workshop at CCRMA, Stanford University, 2014.

Contributions
-------------

Your contributions are very welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/stanford-mir/issues)" in the right navigation bar, then "New Issue".  For a prioritized list of open issues awaiting contribution, click on the blue "[Ready](https://waffle.io/stevetjoa/stanford-mir)" button above.

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).


How to Use this Repo
--------------------

If you're a visitor, simply visit <http://nbviewer.ipython.org/github/stevetjoa/stanford-mir> and browse the IPython notebooks. <http://nbviewer.ipython.org> renders IPython notebooks from a GitHub repo so it can be viewed in a web browser.

If you're a workshop participant, follow the steps below

1. install git

2. install vagrant


Install Git
-----------

If you don't have Git, [download Git here](http://git-scm.com).

Optional: create an account at <http://github.com>. Doing so will easily allow you to contribute code back into this repo. Then, fork this repo: 

    1. Click "Fork" in the top-right corner.

    2. Clone this repository onto your local machine:

        macbook:~$ git clone https://github.com/your_github_username/stanford-mir

Otherwise, to clone this repository onto your local machine:

    macbook:~$ git clone https://github.com/stevetjoa/stanford-mir


Install Vagrant
---------------

A major difficulty in earlier offerings of this workshop was installing software prequisites and handling dependencies. Everyone has a different computing setup, and we would often run into problems when installed packages conflict, or prerequisites aren't met. 

This year, we will use [Vagrant](http://vagrantup.com) to create a local virtual development environment running Ubuntu 12.04. Vagrant will ensure that every person has exactly the same development environment with the same installed packages. 

Vagrant is available for all major operating systems, including Windows, Mac OS X, and Linux. It's a breeze to install.

1.  Install [VirtualBox](https://www.virtualbox.org) and [Vagrant](http://vagrantup.com).

2.  Create a new virtual machine using our customized Vagrant box built upon [Ubuntu 12.04 64-bit](https://vagrantcloud.com/stevetjoa/stanford-mir).

        macbook:~/stanford-mir$ vagrant up

    If this is your first time running `vagrant up`, this step may take several minutes to download the vagrant box.

3.  Finally, login to the new virtual machine:

        macbook:~/stanford-mir$ vagrant ssh

    This step logs you in to Ubuntu locally as user `vagrant` with default password `vagrant`.


Using IPython
-------------

A majority of our instruction and laboratory work will occur inside the IPython notebook. You can think of the IPython notebook like the Mathematica or Matlab desktop, except it's in Python and it runs inside your web browser.

1.  In your vagrant box, go to the `stanford-mir` directory:

2.  Run `ipython notebook`.

3.  On your *host* machine, visit <http://localhost:8888>. Congratulations, you are now running an IPython notebook, and you can get started with the workshop material.
