import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

full_url = 'https://www.cian.ru/cat.php?currency=2&deal_type=sale&decorations_list%5B0%5D=without&engine_version=2&house_material%5B0%5D=2&maxfloor=10&maxprice=15000000&maxtarea=100&minfloor=2&minprice=5000000&mintarea=60&object_type%5B0%5D=2&offer_type=flat&only_flat=1&region=4593&room3=1&year%5B0%5D=2026'
url = 'https://www.cian.ru/cat.php'
headers = Headers(os="win", headers=True).generate()
params = {'currency': '2', 'deal_type': 'sale',
          'decorations_list%5B0%5D': 'without', 'engine_version': '2',
          'house_material%5B0%5D': '2', 'maxfloor': '10',
          'maxprice': '15000000', 'maxtarea': '100', 'minfloor': '2',
          'minprice': '6000000', 'mintarea': '60', 'object_type%5B0%5D': '2',
          'offer_type': 'flat', 'only_flat': '1', 'region': '4593',
          'room3': '1', 'year%5B0%5D': '2026'}

response = requests.get(url, headers=headers, params=params)

soup = BeautifulSoup(response.text, 'lxml')
