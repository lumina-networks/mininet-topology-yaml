import pytest
from mn_topo.core import table


def test_default_table():
    data = table.create_table_topology()
    assert len(data['hosts']) > 0
    assert len(data['switches']) > 0
    assert len(data['links']) > 0
