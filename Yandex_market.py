import requests
from bs4 import BeautifulSoup as BS

search = input().split()
name = 'https://market.yandex.ru/search?text='
for i in search:
    name = name + i + '%20'
name = name[:-3] + '&cvredirect=2&suggest_history=1&local-offers-first=0'

source = requests.get(name).text
print(name)
soup = BS(source, 'lxml')
page = soup.find('div', {'class': 'layout layout_type_search i-bem'})
items = page.find('div', {'class': 'layout__col i-bem layout__col_search-results_normal'})
print(items.text)
for item in items.find_all('div', {'class': 'n-snippet-card2 i-bem b-zone b-spy-visible b-spy-events b-spy-visible_js_inited b-zone_js_inited n-snippet-card2_js_inited'}):
    print(item)

'''
https://market.yandex.ru/search?text=intel%20core%20i5&cvredirect=2&suggest_history=1&local-offers-first=0
https://market.yandex.ru/search?text=intel%20core%20i5&cvredirect=2&suggest_history=1&local-offers-first=0
