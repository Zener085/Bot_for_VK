import requests
from bs4 import BeautifulSoup as BS

html_code = requests.get('https://www.nike.com/ru/w/mens-shoes-nik1zy7ok').text

soup = BS(html_code, 'lxml')
products = soup.find('main')

for item in products.findAll('div', {'class' : 'product-card css-1m8o4mv ncss-col-sm-6 ncss-col-lg-4 va-sm-t product-grid__card'}):
   prod_info = item.find('div', {'class' : 'product-card__info'})
   prod_name = prod_info.find('div', {'class' : 'product-card__title'}).text
   prod_price = prod_info.find('div', {'class' : 'product-card__price'}).text
   print(prod_name)
