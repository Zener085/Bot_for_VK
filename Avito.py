import requests
from bs4 import BeautifulSoup as BS

html_code = requests.get('https://www.avito.ru/moskva/rabota?cd=1').text

soup = BS(html_code, 'lxml')

page = soup.find('div', {'class': 'js-catalog_serp'})


for item in page.find_all('div', {'class': 'snippet-horizontal item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended'}):
    content = item.find('div', {'class': 'item_table-wrapper'})
    title = content.find('div', {'class': 'snippet-title-row'})
    print(title.text)
    print(title.a.get('href'))
    print(item.meta.get('content'))

