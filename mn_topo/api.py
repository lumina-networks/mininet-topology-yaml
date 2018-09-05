from topology import api
from core import table, dc
from core.mn_topology import MininetTopology

def create_table_topology(filename, rows=3, columns=3, links_per_row=1,
                          links_per_columns=1, controllers=[], interfaces=[], customers=[]):
    data = table.create_table_topology(rows, columns, links_per_row, links_per_columns)
    data['controllers'] = controllers
    data['interfaces'] = interfaces
    data['customers'] = customers
    return api.create_topology(filename, **data)


def create_dc_topology(filename, data_centres=1, spines=2, leaves=4, hosts=1,
                       controllers=[], interfaces=[], customers=[]):
    data = dc.create_dc_topology(data_centres, spines, leaves, hosts)
    data['controllers'] = controllers
    data['interfaces'] = interfaces
    data['customers'] = customers
    return api.create_topology(filename, **data)


def start_mn_from_topo(filename):
    topo = api.read_topology(filename)
    mn = MininetTopology(topo)
    mn.start()
    mn.cli()
    mn.stop()
