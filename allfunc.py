# All functions are specified in this module

# Module imports
import cred
import variablein
import humanize    # For making data human-readable


def memoryconv(jsoninput):  # Function to convert memory size to human readable
    max_value = jsoninput['result'][0]['value_min']
    return humanize.naturalsize(max_value, binary=True)


def dataspeedconv(jsoninput):  # Function to convert data transfer speed to human readable
    max_value = jsoninput['result'][0]['value_max']
    return humanize.naturalsize(max_value, binary=True) + "/s"


def zapi_req_item(host):
    request = cred.zapi.do_request(method='item.get', params={
        'output': [
            'itemid'
        ],
        'host': host,
        'application': variablein.application
    })
    return request


def zapi_req_max(item):  # Function to obtain data from Zabbix API through JSON request
    request = cred.zapi.do_request(method='trend.get', params={
        'output': [
            'value_min'
        ],
        'itemids': [
            item
        ],
        'limit': '1',
        'time_from': variablein.unix_yesterday,
        'time_till': variablein.unix_today
    })
    return request




