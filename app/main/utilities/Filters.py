def filter_by_rate(item, rate):
    return True if item['rate'] is not None and item['rate'][2:-2].isnumeric() and int(
        item['rate'][2:-2]) > rate else False


def filter_by_name(item, name):
    return True if name in item['name'] or name in item['msg'] else False


def filter_by_not_expired(item):
    return False if item['expired'] is True else True
