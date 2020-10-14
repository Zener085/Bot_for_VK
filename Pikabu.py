import requests
from bs4 import BeautifulSoup as BS


source = requests.get('https://www.reddit.com/').text
soup = BS(source, 'lxml')

