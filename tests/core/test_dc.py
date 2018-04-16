import pytest
from mn_topo.core import dc


@pytest.fixture(scope='module')
def mock_get_host(request):
    return {
      'gw': "10.1.0.1",
      'ip': "10.1.1.1/16",
      'mac': "00:00:10:01:01:01",
      'name': "h11001"
    }


@pytest.fixture(scope='module')
def mock_get_switch(request):
    return {
        'name': 's15001',
        'dpid': '3a99',
        'protocol': 'OpenFlow13'
    }


def test_default_dc(mock_get_host, mock_get_switch):
    data = dc.create_dc_topology()
    assert len(data['hosts']) == 4
    assert data['hosts'][0] == mock_get_host
    assert len(data['switches']) == 6
    assert data['switches'][0] == mock_get_switch
    assert len(data['links']) == 12
    assert data['links'][0] == {'destination':'l10001', 'source': 'h11001'}