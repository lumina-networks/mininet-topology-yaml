
def create_dc_topology(data_centres=1, spines=2, leaves=4, hosts=1):
    data = {
        'hosts': [],
        'switches': [],
        'links': [],
    }
    for data_center in range(0, data_centres):
        dc_base = (data_center + 1) * 10000
        for spine in range(0, spines):
            name = str(dc_base + (spine + 5001))
            switch = 's' + name
            data['switches'].append({'name': switch, 'dpid': format(int(name), 'x'), 'protocol': 'OpenFlow13'})

        for leaf in range(0, leaves):
            name = str(dc_base + (leaf + 1))
            switch = 'l' + name
            data['switches'].append({'name': switch, 'dpid': format(int(name), 'x'), 'protocol': 'OpenFlow13'})

            for host in range(0, hosts):
                compute_name = 'h' + str(dc_base + ((leaf + 1) * 1000) + (host + 1))
                data['hosts'].append({'name': compute_name,
                                     'ip': '10.' + str(data_center + 1) + "." + str(leaf + 1) + '.' + str(
                                         host + 1) + '/16',
                                     'gw': '10.' + str(data_center + 1) + '.0.1',
                                     'mac': "00:00:10:{:02d}:{:02d}:{:02d}".format(data_center + 1, leaf + 1,
                                                                                   host + 1),
                                     })
                data['links'].append({'source': compute_name, 'destination': switch})

            for spine in range(0, spines):
                spine_name = 's' + str(dc_base + (spine + 5001))
                data['links'].append({'source': switch, 'destination': spine_name})

    return data
