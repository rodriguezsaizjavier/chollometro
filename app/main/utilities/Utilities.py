import urllib
import urllib.request as request

from bs4 import BeautifulSoup

from app.main.data.Data2 import try_with_attribute, try_it
from app.main.data.ProductLocator import *


def reloaded(data):
    if get_first()['name'] == data[0]['name']:
        return data
    else:
        return data.append(get_first())


def get_first():
    html = ''
    url = 'https://www.chollometro.com/nuevos'
    req = urllib.request.Request(url, headers={'User-Agent': ""})
    html += str(urllib.request.urlopen(req).read())
    soup = BeautifulSoup(html)

    item = soup.select(CATALOG)[0]

    first_product = {}

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
        first_product = ({
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
    return first_product
