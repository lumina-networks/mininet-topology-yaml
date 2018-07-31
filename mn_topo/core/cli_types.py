import re
import click

IP = 0
IP_V4 = 4
IP_V6 = 6


class IPAddressType(click.ParamType):
    name = 'ip_address'
    ipv4_pattern = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}' \
                   '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
    ipv6_pattern = '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?' \
                   '(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}' \
                   '(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\p{N}\p{L}]+)?'

    def __init__(self, version=IP):
        super(IPAddressType, self).__init__()
        self.version = version

    def convert(self, value, param, ctx):
        if self.version == IP_V4:
            m = re.match(IPAddressType.ipv4_pattern, value)
            error = '%s is not a valid ipv4 address' % value
        elif self.version == IP_V6:
            m = re.match(IPAddressType.ipv6_pattern, value)
            error = '%s is not a valid ipv6 address' % value
        else:
            m = self.convert_any(value, param, ctx)
            error = '%s is not a valid ipv4 or ipv6 address' % value
        if m:
            return m.group(0)
        else:
            self.fail(error, param, ctx)

    def convert_any(self, value, param, ctx):
        for pattern in (IPAddressType.ipv4_pattern, IPAddressType.ipv6_pattern):
            m = re.match(pattern, value)
            if m:
                return m
        return False
