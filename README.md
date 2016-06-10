stanford-mir
============

Instructional material for the [Music Information Retrieval Workshop](https://ccrma.stanford.edu/workshops/music-information-retrieval-mir) at CCRMA, Stanford University, 2014-16.


How to Use This Repo
--------------------

This repo contains a bunch of IPython notebooks related to music information retrieval.

If you're a **visitor**, browse a read-only version of this repo at [musicinformationretrieval.com](http://musicinformationretrieval.com).

If you're a **workshop participant**, follow the steps below to get started with Git and IPython.


### Install Git

Git is a version control system. You will use Git to retrieve the latest version of our IPython notebooks and to track changes that you make to these notebooks.

1.  [Download Git](http://git-scm.com), and install it on your local machine.

2.  Clone this repo onto your local machine:

        macbook:~$ git clone https://github.com/stevetjoa/stanford-mir

### Start IPython

A majority of our instruction and laboratory work will occur inside the [IPython notebook](http://ipython.org/notebook.html). You can think of the IPython notebook like the Mathematica or Matlab desktop, except it's in Python and it runs inside your web browser.

1.  Start the IPython notebook server:

        stanford-mir:~$ ipython notebook

2.  On your *host* machine, visit <http://localhost:8888>. 

3.  Open the notebook `index.ipynb`, or click on any `.ipynb` file to open it.

Congratulations, you are now running an IPython notebook, and you can get started with the workshop material.


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

        $ git commit kmeans.ipynb kmeans.html
        $ git push


Appendix
--------

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

    Note: do *not* upgrade the virtual machine to Ubuntu 14.04 when prompted.

    Note: outdated versions of Mac OS X may yield problems with `vagrant ssh`. To avoid such problems, please upgrade (for free) to the latest version of Mac OS X.

#### Troubleshooting Vagrant

*   Problem: When on a Windows host machine, `vagrant ssh` results in a timeout error: `ssh_exchange_identification: read: Connection reset by peer`.

    Solution: Go into the BIOS, and make sure that Hardware Virtualization is enabled. For details, see [this answer on Stack Overflow](http://stackoverflow.com/questions/22575261/vagrant-stuck-connection-timeout-retrying/25504245#25504245). 

*   Problem: The folder `stanford-mir` on the guest machine is empty.

    Solution: Vagrant probably failed to sync folders between the host and the guest machines. Try `vagrant provision` or `vagrant reload` from the host machine.

