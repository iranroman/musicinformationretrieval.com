stanford-mir
============

[![Stories in Ready](https://badge.waffle.io/stevetjoa/stanford-mir.png?label=ready&title=Ready)](https://waffle.io/stevetjoa/stanford-mir)

Instruction for the Music Information Retrieval Workshop at CCRMA, Stanford University, 2014.

For a list of open issues, click on the blue "[Ready](https://waffle.io/stevetjoa/stanford-mir)" button above.

Your contributions are very welcome! You can contribute in two ways:

1. Submit an issue. Click on "[Issues](https://github.com/stevetjoa/stanford-mir/issues)" in the right navigation bar, then "New Issue".

2. Submit changes to source code or documentation. [Fork this repo](https://help.github.com/articles/fork-a-repo), make edits, then [submit a pull request](https://help.github.com/articles/using-pull-requests).


Getting Started
---------------

If you don't have Git, [download Git here](http://git-scm.com).

Then, to download this repository:

    macbook:~$ git clone https://github.com/stevetjoa/stanford-mir


Create a Virtual Machine
------------------------

A major difficulty in earlier offerings of this workshop was installing software prequisites and handling dependencies. Everyone has a different computing setup, and we would often run into problems when installed packages conflict, or prerequisites aren't met. This year, we will use [Vagrant](http://vagrantup.com) to create a local, empty, virtual development environment running Ubuntu 12.04. Vagrant will ensure that every person has exactly the same development environment with the same installed packages. It's a breeze to install.

Vagrant is available for all major operating systems, including Windows, Mac OS X, and Linux.

1.  Install [VirtualBox](https://www.virtualbox.org) and [Vagrant](http://vagrantup.com).

2.  Create a new virtual machine using our customized Vagrant box built upon [Ubuntu 12.04 64-bit](https://vagrantcloud.com/stevetjoa/stanford-mir).

        macbook:~/stanford-mir$ vagrant up

    If this is your first time running `vagrant up`, this step may take several minutes to download the vagrant box, `stanford-mir-vbox.box`.

3.  Finally, login to the new virtual machine:

        macbook:~/stanford-mir$ vagrant ssh

    This step logs you in to Ubuntu locally as user `vagrant` with default password `vagrant`.
