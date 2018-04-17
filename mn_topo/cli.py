import click
import api
from .core.constants import DEFAULT_CONTROLLERS
from .core.cli_types import IPAddressType
from .core.utility import merge_two_dicts, u_to_ascii

IP_ADDRESS = IPAddressType()


def format_controller_option(controller):
    if controller:
        return [merge_two_dicts(DEFAULT_CONTROLLERS[0], {'name': u_to_ascii(i[0]), 'ip': i[1]}) for i in controller]
    return DEFAULT_CONTROLLERS


def format_interface_option(interface):
    if interface:
        return [{'name': u_to_ascii(i[0]), 'switch': u_to_ascii(i[1])} for i in interface]
    return []


@click.group()
def mininet(name='mininet'):
    """Mininet Topology Commands"""
    pass


@mininet.command()
@click.argument('filename', type=click.Path(), default='topo.yml')
@click.option('--rows', type=click.INT, default=3, show_default=True)
@click.option('--columns', type=click.INT, default=3, show_default=True)
@click.option('--links-per-row', type=click.INT, default=1, show_default=True)
@click.option('--links-per-column', type=click.INT, default=1, show_default=True)
@click.option('--controller', type=click.Tuple([click.STRING, IP_ADDRESS]), multiple=True,
              help='Multiple controller option Name and IP tuple')
@click.option('--interface', type=click.Tuple([click.STRING, click.STRING]), multiple=True,
              help='Multiple interface option Name and Switch Name tuple')
def table(filename, rows, columns, links_per_row, links_per_column, controller, interface):
    """Create Table Topology File For Mininet"""
    controllers = format_controller_option(controller)
    interfaces = format_interface_option(interface)
    api.create_table_topology(filename, rows, columns, links_per_row, links_per_column, controllers, interfaces)


@mininet.command()
@click.argument('filename', type=click.Path(), default='topo.yml')
@click.option('--data-centres', type=click.INT, default=1, show_default=True)
@click.option('--spines', type=click.INT, default=2, show_default=True)
@click.option('--leaves', type=click.INT, default=4, show_default=True)
@click.option('--hosts', type=click.INT, default=1, show_default=True)
@click.option('--controller', type=click.Tuple([click.STRING, IP_ADDRESS]), multiple=True,
              help='Multiple controller option Name and IP tuple')
@click.option('--interface', type=click.Tuple([click.STRING, click.STRING]), multiple=True,
              help='Multiple interface option Name and Switch Name tuple')
def dc(filename, data_centres, spines, leaves, hosts, controller, interface):
    """Create DC Topology File For Mininet"""
    controllers = format_controller_option(controller)
    interfaces = format_interface_option(interface)
    api.create_dc_topology(filename, data_centres, spines, leaves, hosts, controllers, interfaces)


@mininet.command()
@click.argument('filename', type=click.Path(), default='topo.yml')
def start(filename):
    """Start Mininet from Topology File"""
    api.start_mn_from_topo(filename)

if __name__ == '__main__':
    mininet()