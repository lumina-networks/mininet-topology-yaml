Mininet-Topology-Yaml
=====================

.. image:: https://img.shields.io/pypi/v/mininet-topology-yaml.svg
    :target: https://pypi.python.org/pypi/mininet-topology-yaml
    :alt: Latest PyPI version

A CLI plugin for `topology-yaml <https://github.com/lumina-networks/topology-yaml>`_.

It makes creating Table and Clos (spine/leaf) topology files easier.

Most importantly it is able to spawn a mininet session with the hosts, switches, links and connect to the controllers
defined in the topology file.

Requirements
~~~~~~~~~~~~

- Python 2.7
- Mininet 2.2.2
- OVS 2.8.1

Installation
~~~~~~~~~~~~

From Source:

::

$ git clone https://github.com/lumina-networks/mininet-topology-yaml
$ cd mininet-topology-yaml
$ sudo pip install .

From PyPi

::

$ pip install mininet-topology-yaml


Usage
~~~~~

**topology-yaml** will be the command after installation. For example:
::

    $ Usage: topology-yaml [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      create  Create Topology File
      delete  Delete Topology File
      mininet  Mininet Topology Commands
      read    Read Topology File


Troubleshooting
~~~~~~~~~~~~~~~

Could not load plugin
---------------------

::

    Usage: topology-yaml [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      create   Create Topology File
      delete   Delete Topology File
      mininet  † Warning: could not load plugin. See `topology-yaml mininet
               --help`.
      read     Read Topology File

This warning generally occurs when mininet is not installed on the system. Ensure mininet is installed and the Python
API for mininet is globally available.


Documentation
~~~~~~~~~~~~~

To build documentation:

::

$ make documentation

Or

::

$ cd docs
$ make html


Licence
-------

MIT

Authors
-------

`mininet-topology-yaml` was written by `Lumina NetDev <oss-dev@luminanetworks.com>`_.
