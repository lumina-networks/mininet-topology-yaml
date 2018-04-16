import pytest
import click
from mn_topo.core.cli_types import IPAddressType


def test_ipv4():
    addr_type = IPAddressType(version=4)
    ipv4_addresses = ('0.0.0.0', '224.0.0.0', '10.0.0.1', '192.168.1.1')
    for addr in ipv4_addresses:
        assert addr == addr_type.convert(addr, 'test', 'test')
    with pytest.raises(click.BadParameter) as e:
        addr_type.convert('abcd', 'test', 'test')
    assert e.value.message == 'abcd is not a valid ipv4 address'


def test_ipv6():
    addr_type = IPAddressType(version=6)
    ipv6_addresses = ('2001:cdba:0000:0000:0000:0000:3257:9652',
                      '2001:cdba:0:0:0:0:3257:9652', '2001:cdba::3257:9652')
    for addr in ipv6_addresses:
        assert addr == addr_type.convert(addr, 'test', 'test')
    with pytest.raises(click.BadParameter) as e:
        addr_type.convert('abcd', 'test', 'test')
    assert e.value.message == 'abcd is not a valid ipv6 address'


def test_ip():
    addr_type = IPAddressType()
    ip_addresses = ('0.0.0.0', '224.0.0.0', '10.0.0.1', '192.168.1.1',
                    '2001:cdba:0000:0000:0000:0000:3257:9652',
                    '2001:cdba:0:0:0:0:3257:9652', '2001:cdba::3257:9652')
    for addr in ip_addresses:
        assert addr == addr_type.convert(addr, 'test', 'test')
    with pytest.raises(click.BadParameter) as e:
        addr_type.convert('abcd', 'test', 'test')
    assert e.value.message == 'abcd is not a valid ipv4 or ipv6 address'
