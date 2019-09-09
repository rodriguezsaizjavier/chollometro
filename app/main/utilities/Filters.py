

def filter_by_rate(data, rate):
    list_by_rate = []
    for item in data:
        if item['rate'][2:-2].isnumeric() and int(item['rate'][2:-2]) > rate:
            list_by_rate.append(item)

    return list_by_rate


def filter_by_name(data, name):
    list_by_name = []
    for item in data:
        if name in item['name'] or item['msg']:
            list_by_name.append(item)

    return list_by_name
