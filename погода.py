import requests
from bs4 import BeautifulSoup as bs 



html_code = requests.get('https://yandex.ru/pogoda/moscow/month?via=ms').text


soup = bs(html_code, 'lxml')

day = soup.find('div', {'class':'climate-calendar-day climate-calendar-day_with-history'})



for day in soup.findAll('div', {'class':'climate-calendar-day climate-calendar-day_with-history'}):
	print(day.find('h6', {'class':'climate-calendar-day__detailed-day'}).text)
	day_celc = day.find('div', {'class':'temp climate-calendar-day__temp-day'})
	night_celc = day.find('div', {'class':'temp climate-calendar-day__temp-night'})
	print('Температура днем '+ day_celc.find('span', {'class':'temp__value'}).text)
	print('Температура ночью '+ night_celc.find('span', {'class':'temp__value'}).text)
