import os
import pytest
from mn_topo import api
from mn_topo.core.constants import DEFAULT_CONTROLLERS, DEFAULT_CUSTOMERS

def read(filename):
    output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open(output_file, 'r') as fin:
        return fin.read()


def test_create_table_topology(tmpdir):
    p = tmpdir.mkdir("sub").join("topo.yml")
    api.create_table_topology(p.strpath, controllers=DEFAULT_CONTROLLERS, customers=DEFAULT_CUSTOMERS)
    content = p.read()
    assert content == read('./mocks/mock_table_topo.yml')


def test_create_dc_topology(tmpdir):
    p = tmpdir.mkdir("sub").join("topo.yml")
    api.create_dc_topology(p.strpath, controllers=DEFAULT_CONTROLLERS, customers=DEFAULT_CUSTOMERS)
    content = p.read()
    assert content == read('./mocks/mock_dc_topo.yml')

