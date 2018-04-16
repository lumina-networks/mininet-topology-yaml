from topology import api
from core import table, dc


def create_table_topology(filename, rows=3, columns=3, links_per_row=1,
                          links_per_columns=1, controllers=[], interfaces=[]):
    data = table.create_table_topology(rows, columns, links_per_row, links_per_columns)
    data['controllers'] = controllers
    data['interfaces'] = interfaces
    return api.create_topology(filename, **data)


def create_dc_topology(filename, data_centres=1, spines=2, leaves=4, hosts=1,
                       controllers=[], interfaces=[]):
    data = dc.create_dc_topology(data_centres, spines, leaves, hosts)
    data['controllers'] = controllers
    data['interfaces'] = interfaces
    return api.create_topology(filename, **data)