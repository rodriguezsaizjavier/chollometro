import urllib
import urllib.request as request

from bs4 import BeautifulSoup

from app.main.data.ProductLocator import *


def try_it(data):
    return None if data is None or len(data) is 0 else data[0].text


def try_with_attribute(data, attribute):
    return None if data is None or len(data) is 0 else data[0].get(attribute)


def create_json(data):
    products_catalog_json = []
    for item in data:
        category = try_it(item.select(CATEGORY))

        image = try_with_attribute(item.select(IMAGE), 'src')

        name = try_it(item.select(NAME))

        price = try_it(item.select(PRICE))

        old_price = try_it(item.select(OLD_PRICE))

        rate = try_it(item.select(RATE))

        delivery = try_it(item.select(DELIVERY))

        msg = try_it(item.select(MSG))

        user = try_it(item.select(USER))

        link = try_with_attribute(item.select(LINK), 'href')

        expired = True if EXPIRED in item.get('class') else False

        if expired is False:
            products_catalog_json.append({
                'category': category,
                'image': image,
                'name': name,
                'price': price,
                'old_price': old_price,
                'rate': rate,
                'delivery': delivery,
                'msg': msg,
                'user': user,
                'link': link
            })

    return products_catalog_json


def get_raw_data(pages):
    html = ''
    for i in range(1, pages):
        url = 'https://www.chollometro.com/nuevos?page=' + str(i)
        req = urllib.request.Request(url, headers={'User-Agent': ""})
        html += str(urllib.request.urlopen(req).read().decode("utf-8"))

    soup = BeautifulSoup(html, 'lxml')

    catalog = soup.select(CATALOG)

    return catalog
