Commands
******************************

The Mininet-Topology-Yaml plugin for Topology-Yaml provides the capability to create Table and Clos (spine/leaf) topology
files that conform to topology-yaml format.

Most importantly it is able to spawn a mininet session with the hosts, switches, links and connect to the controllers
defined in the topology file.

dc
~~

**topology-yaml mininet dc** takes the path to a file as a filename argument and six options to define a Clos topology.

::

    Usage: topology-yaml mininet dc [OPTIONS] [FILENAME]

    Create DC Topology File For Mininet

    Options:
      --data-centres INTEGER          [default: 1]
      --spines INTEGER                [default: 2]
      --leaves INTEGER                [default: 4]
      --hosts INTEGER                 [default: 1]
      --controller <TEXT IP_ADDRESS>...
                                      Multiple controller option Name and IP tuple
      --interface <TEXT TEXT>...      Multiple interface option Name and Switch
                                      Name tuple
      --help                          Show this message and exit.


table
~~~~~

**topology-yaml mininet table** takes the path to a file as a filename argument and six options to define a table topology.

::

    Usage: topology-yaml mininet table [OPTIONS] [FILENAME]

    Create Table Topology File For Mininet

    Options:
      --rows INTEGER                  [default: 3]
      --columns INTEGER               [default: 3]
      --links-per-row INTEGER         [default: 1]
      --links-per-column INTEGER      [default: 1]
      --controller <TEXT IP_ADDRESS>...
                                      Multiple controller option Name and IP tuple
      --interface <TEXT TEXT>...      Multiple interface option Name and Switch
                                      Name tuple
      --help                          Show this message and exit.


start
~~~~~

**topology-yaml mininet start** takes a filename argument which is the path to the topology file that will be read and
spawns a mininet session with the hosts, switches, links between them and controller connection defined within.

::

    Usage: topology-yaml mininet start [OPTIONS] [FILENAME]

    Start Mininet from Topology File

    Options:
      --help  Show this message and exit.

