

def get_host(row, column):
    return {
        'name': 'h' + get_node_id(row, column),
        'ip': '10.0.' + str(row + 1) + '.' + str(column + 1) + '/16',
        'mac': "00:00:10:00:{:02d}:{:02d}".format(row + 1, column + 1),
        'gw': '10.0.0.1'
    }


def get_switch(row, column):
    return {
        'name': get_switch_name(row, column),
        'dpid': format(int(get_node_id(row, column)), 'x'),
        'protocol': 'OpenFlow13'
    }


def get_switch_name(row, column):
    return 's' + get_node_id(row, column)


def get_node_id(row, column):
    return str(((row + 1) * 100) + (column + 1))


def create_table_topology(rows=3, columns=3, links_per_row=1, links_per_columns=1):
    data = {
        'hosts': [],
        'switches': [],
        'links': [],
    }
    # we first calculate the host to ensure they are created in port 1 on all switches
    for row in range(0, rows):
        for column in range(0, columns):
            if row > 0 and row < rows - 1 and column > 0 and column < columns - 1:
                continue
            host = get_host(row, column)
            switch_name = get_switch_name(row, column)
            data['hosts'].append(get_host(row, column))
            data['links'].append({'source': host['name'], 'destination': switch_name})

    for row in range(0, rows):
        for column in range(0, columns):

            switch = get_switch(row, column)
            right = get_switch_name(row, column + 1)
            bottom = get_switch_name(row + 1, column)

            data['switches'].append(switch)

            if column < columns - 1:
                for repeat in range(0, links_per_row):
                    data['links'].append({'source': switch['name'], 'destination': right})

            if row < rows - 1:
                for repeat in range(0, links_per_columns):
                    data['links'].append({'source': switch['name'], 'destination': bottom})

    return data
