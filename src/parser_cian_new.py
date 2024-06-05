import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

url = 'https://www.cian.ru/kupit-kvartiru-novostroyki/'
headers = Headers(os="win", headers=True).generate()

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

print(soup)
