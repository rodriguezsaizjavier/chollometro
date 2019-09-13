from app.main.data.Data2 import create_json, get_raw_data


def reloaded(data):
    new_data = create_json(get_raw_data(2))
    aux = []

    for item in new_data:

        if item['name'] == data[0]['name']:
            return aux + data
        aux += item

    return create_json(get_raw_data(11))
