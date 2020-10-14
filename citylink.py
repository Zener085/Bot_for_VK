import requests
from bs4 import BeautifulSoup as BS

search = input().split()
name = ''

for i in search:
    name = name + '+' + i

name = name[1:]

html_code = requests.get('https://www.citilink.ru/search/?text=' + name).text
soup = BS(html_code, 'lxml')


page = soup.find('div', {'class': "main_content_wrapper search"})
items = page.find('div', {'class': 'main_content_inner'})
items = items.find('div', {'class': 'block_data__gtm-js block_data__pageevents-js listing_block_data__pageevents-js'})

for item in items.findAll('div', {'class': 'subcategory-product-item__body'}):
    title = item.find('span', {'class': 'h3'})
    print(title.a.get('title'))
    print(title.a.get('href'))
    Text = item.find('p', {'class': 'short_description'}).text
    print(Text)
    
