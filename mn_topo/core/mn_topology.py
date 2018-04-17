import mininet
from functools import partial


class MininetTopology(object):
    def __init__(self, topology):
        self.topology = topology
        self.mininet_topology = mininet.topo.MNTopo()

        self.add_hosts()
        self.add_switches()
        self.add_links()

        self.mininet = mininet.net.Mininet(topo=self.mininet_topology,
                                           switch=partial(mininet.node.OVSSwitch, datapath='user'))
        self.add_controllers()
        self.add_interfaces()

    def add_hosts(self):
        for host in self.topology['hosts']:
            mac = None if 'mac' not in host else host['mac']
            self.mininet_topology.addHost(host['name'], ip=host['ip'], defaultRoute='via ' + host['gw'], mac=mac)

    def add_switches(self):
        for switch in self.topology['switches']:
            if 'type' not in switch or switch['type'] == 'ovs':
                self.mininet_topology.addSwitch(switch['name'], dpid=switch['dpid'], protocols=switch['protocol'])

    def add_links(self):
        for link in self.topology['links']:
            src_name = link['source']
            dst_name = link['destination']

            source = None
            if src_name in self.topology['switches']:
                source = self.topology['switches'][src_name]
            else:
                source = self.topology['hosts'][src_name]

            destination = None
            if dst_name in self.topology['switches']:
                destination = self.topology['switches'][dst_name]
            else:
                destination = self.topology['hosts'][dst_name]

            if ('type' not in source or source['type'] == 'ovs') \
                    and ('type' not in destination or destination['type'] == 'ovs'):
                self.mininet_topology.addLink(source, destination)

    def add_controllers(self):
        for controller in self.topology['controllers']:
            self.mininet.addController(mininet.node.RemoteController(controller['name'], ip=controller['ip']))

    def add_interfaces(self):
        for interface in self.topology['interfaces']:
            mininet.link.Intf(interface['name'], node=self.mininet.nameToNode[interface['switch']])

    def start(self):
        self.mininet.start()

    def cli(self):
        mininet.cli.CLI(self.mininet)

    def stop(self):
        self.mininet.stop()
        mininet.clean.cleanup()