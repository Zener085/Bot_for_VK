import requests
from bs4 import BeautifulSoup as bs 

for i in range(1, 6):
        html_code = requests.get('https://store.playstation.com/ru-ru/grid/STORE-MSF75508-PRICEDROPSCHI/'+str(i)).text

        soup = bs(html_code, 'lxml')
        
        for product in soup.findAll('div', {'class':'grid-cell grid-cell--game'}):
                name_game = product.find('div', {'class': 'grid-cell__body'})
                html_code_game = requests.get('https://store.playstation.com' + name_game.a.get('href')).text
                soup2 = bs(html_code_game, 'lxml')
                
                for game in soup2.findAll('div', {'class': 'pdp__description'}):
                        game_title = game.find('p', {'style': 'direction:ltr'})
                        #print(game_title.text)

                        try:
                                game_photos = soup2.find('div', {'class': 'pdp-carousel__thumbnail-page pdp-carousel__thumbnail-page--center'})
                                game_photo = game_photos.find('div', {'class': 'thumbnail-item'})
                                print(game_photo.img.get('src'))
                        except:
                                continue
        '''
	for product in soup.findAll('div', {'class':'grid-cell grid-cell--game'}):
		product_name = product.find('div', {'class':'grid-cell__title'}).span.text
		product_not_sale_price = product.find('div', {'class':'price'}).text
		product_sale_price = product.find('h3', {'class':'price-display__price'}).text
		product_image = product.find('div', {'class':'product-image__img product-image__img--main'}).img.get('src')
		print(product_image)
		print(product_name)
		print('Цена без скидки '+product_not_sale_price)
		print('Цена со скидкой '+product_sale_price)
		print('https://store.playstation.com' + product.a.get('href'))
'''
