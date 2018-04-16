import pytest
from mn_topo.core import table


@pytest.fixture(scope='module')
def mock_get_host(request):
    return {
        'name': 'h101',
        'ip': '10.0.1.1/16',
        'mac': "00:00:10:00:01:01",
        'gw': '10.0.0.1'
    }


@pytest.fixture(scope='module')
def mock_get_switch(request):
    return {
        'name': 's101',
        'dpid': '65',
        'protocol': 'OpenFlow13'
    }


def test_default_table(mock_get_host, mock_get_switch):
    data = table.create_table_topology()
    assert len(data['hosts']) == 8
    assert data['hosts'][0] == mock_get_host
    assert len(data['switches']) == 9
    assert data['switches'][0] == mock_get_switch
    assert len(data['links']) == 20
    assert data['links'][0] == {'destination':'s101', 'source': 'h101'}


def test_get_node_id():
    node_id = table.get_node_id(0,0)
    assert '101' == node_id


def test_get_switch_name():
    node_id = table.get_switch_name(0, 0)
    assert 's101' == node_id


def test_get_host(mock_get_host):
    data = table.get_host(0,0)
    assert data == mock_get_host


def test_get_switch(mock_get_switch):
    data = table.get_switch(0,0)
    assert data == mock_get_switch