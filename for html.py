import requests
from bs4 import BeautifulSoup as BS

base = 'https://www.youtube.com/results?search_query='
search = '+'.join(input().split())

#search = '+'.join(search)
html = requests.get(base + search).text

#print(html)

soup = BS(html, 'lxml')

a = soup.find('div', {'id':'content'})

for b in a.findAll('div', {'class': 'yt-lockup-content'}):
    print(b.h3.a.text)
    print(b.h3.a.get('href'))
    print('')
