import requests
from bs4 import BeautifulSoup as BS

html_code = requests.get('https://www.gucci.com/int/ru/ca/whats-new/new-in/this-week-men-c-new-men').text

soup = BS(html_code, 'lxml')
page = soup.find('div', {'class': 'content search-result new-4-cols-layout'})
items = page.find('div', {'class': 'product-tiles-grid'})
print(items.text)
for item in items.FindAll('a', {'class': 'product-tiles-grid-item-info'}):
    print(item.get('aria-label'))
    print(item.get('href'))
    

