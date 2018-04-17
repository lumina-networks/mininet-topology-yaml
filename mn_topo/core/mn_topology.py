from mininet.topo import Topo
from mininet.node import OVSSwitch, RemoteController
from mininet.net import Mininet
from mininet.link import Intf
from mininet.cli import CLI
from mininet.clean import cleanup
from functools import partial


class MininetTopology(object):
    def __init__(self, topology):
        self.topology = topology
        self.mininet_topology = Topo()

        self.add_hosts()
        self.add_switches()
        self.add_links()

        self.mininet = Mininet(topo=self.mininet_topology,
                               switch=partial(OVSSwitch, datapath='user'),
                               controller=None)
        self.add_controllers()
        self.add_interfaces()

    def add_hosts(self):
        for host in self.topology.hosts:
            mac = None if 'mac' not in host else host['mac']
            self.mininet_topology.addHost(host['name'], ip=host['ip'], defaultRoute='via ' + host['gw'], mac=mac)

    def add_switches(self):
        for switch in self.topology.switches:
            if 'type' not in switch or switch['type'] == 'ovs':
                self.mininet_topology.addSwitch(switch['name'], dpid=switch['dpid'], protocols=switch['protocol'])

    def add_links(self):
        for link in self.topology.links:
            src_name = link['source']
            dst_name = link['destination']
            # All of this is because we don't want to add a link to an interface
            source = None
            sw_src_index = self.topology.find_index_by_value('switches', 'name', src_name)
            if sw_src_index is not None:
                source = self.topology.switches[sw_src_index]
            else:
                host_src_index = self.topology.find_index_by_value('hosts', 'name', src_name)
                source = self.topology.hosts[host_src_index]

            destination = None
            sw_dst_index = self.topology.find_index_by_value('switches', 'name', dst_name)
            if sw_dst_index is not None:
                destination = self.topology.switches[sw_dst_index]
            else:
                host_dst_index = self.topology.find_index_by_value('hosts', 'name', dst_name)
                destination = self.topology.hosts[host_dst_index]

            if ('type' not in source or source['type'] == 'ovs') \
                    and ('type' not in destination or destination['type'] == 'ovs'):
                self.mininet_topology.addLink(source['name'], destination['name'])

    def add_controllers(self):
        for controller in self.topology.controllers:
            self.mininet.addController(RemoteController(controller['name'], ip=controller['ip']))

    def add_interfaces(self):
        for interface in self.topology.interfaces:
            Intf(interface['name'], node=self.mininet.nameToNode[interface['switch']])

    def start(self):
        self.mininet.start()

    def cli(self):
        CLI(self.mininet)

    def stop(self):
        self.mininet.stop()
        cleanup()