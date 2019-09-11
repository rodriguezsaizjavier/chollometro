import urllib
import urllib.request as request

import bs4
from bs4 import BeautifulSoup


def try_it(text):
    return None if text is None or len(text) is 0 else text[0].text


def get_data():

    products_catalog_json = []
    url = 'https://www.chollometro.com/nuevos'
    req = urllib.request.Request(url, headers={'User-Agent': ""})

    data = urllib.request.urlopen(req)

    soup = BeautifulSoup(data, "lxml")

    CATALOG = soup.select('section.gridLayout > div.gridLayout-item > article')

    for item in CATALOG:
        # a:bs4.element.Tag = item
        # a.get()
        category = try_it(item.select('section.gridLayout > div.gridLayout-item > article > div > div > span'))

        if len(item.select('.thread-image')) is 0:
            image = "None"
        else:
            image = item.select('.thread-image')[0].get('src')

        name = try_it(item.select('.thread-title'))

        price = try_it(item.select('.thread-price'))

        old_price = try_it(item.select('section.gridLayout > div.gridLayout-item > article > div:nth-child(4) > span:nth-child(2) > span:nth-child(1)'))

        rate = try_it(item.select('section.gridLayout > div.gridLayout-item > article > div:nth-child(4) > span:nth-child(2) > span:nth-child(2)'))

        delivery = try_it(item.select('section.gridLayout > div.gridLayout-item > article > div:nth-child(4) > span:nth-child(3) > span > span'))

        msg = try_it(item.select('section.gridLayout > div.gridLayout-item > article > div:nth-child(5) > div > div'))

        user = try_it(item.select('.thread-username'))

        if len(item.select('.thread-image')) is 0:
            link = "None"
        else:
            link = item.select('section.gridLayout > div.gridLayout-item > article > div:nth-child(7) > a')[0].get('href')

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
