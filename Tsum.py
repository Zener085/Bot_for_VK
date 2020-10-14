import requests
from bs4 import BeautifulSoup as BS

html_code = requests.get('https://www.yoox.com/ru').text

soup = BS(html_code, 'lxml')

page = soup.find('div', {'class': 'fixed-width relative'})

print(page)
