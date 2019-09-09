from app.main.data.Data import get_catalog


def filter_by_rate(data, rate):
    list = []
    for item in data:
        if item['rate'][2:-2].isnumeric() and int(item['rate'][2:-2]) > rate:
            list.append({
                'name': item['name'],
                'rate': item['rate'],
                'link': item['link'],
                'price': item['price']
            })

    return list
