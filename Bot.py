import vk_api
import requests
import time
import wikipedia as wiki

from bs4 import BeautifulSoup as BS
from vk_api.longpoll import VkLongPoll, VkEventType

wiki.set_lang("ru")
session = requests.Session()
login, password = 'email', 'password' # It's worked if I print here my email and password
vk_session = vk_api.VkApi(token = '8d6f64df04f40a98e68892e8f222a60dae2b832c49f5122f2c32a9bd4843fb42916df76784dedc10a42f5')
vk_session1 = vk_api.VkApi(login, password)
try:
    vk_session1.auth(token_only = True)
except vk_api.AuthError as error_msg:
    print(error_msg)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk_session1)
photos = []

source = requests.get('https://www.youtube.com/').text
soup = BS(source, 'lxml')

for event in longpoll.listen():
    print(event)
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Привет' or event.text == 'Привет.' or event.text == 'привет' or event.text == 'привет.' or event.text == 'Здравствуй' or event.text == 'здравствуй' or event.text == 'Здравствуйте.' or event.text == 'здравствуйте.' or event.text == 'Здравствуйте':
            vk.messages.send(user_id = event.user_id, message = 'Всем привет. Это, кстати мой бот, а не Митин, потому что мой лучше)', random_id = time.time() * 1000)

        # Для Кости
        elif event.text == 'Ты лох' or event.text == 'Тима лох' or event.text == 'Разработчик лох' or event.text == 'Твой создатель лох':
            vk.messages.send(user_id = event.user_id, message = 'Ты сам лох, тебе деньги платят, а ты такое пишешь, обалдел совсем?!'
                             , random_id = time.time() * 100)

        # Для Майи
        elif event.text == 'Тима кабан':
            vk.messages.send(user_id = event.user_id, message = 'Обалдела?! Сама ты кабан, зараза ты такая'
                             , random_id = time.time() * 100)
        
        elif event.text == 'Обзор':
            vk.messages.send(user_id = event.user_id, message = 'Ты можешь:\n' +
                             ' 1) Сказать мне привет (вот это не надо тестировать);\n' +
                             ' 2) Оскорбить разработчика1;\n ' +
                             ' 3) Написать "Информация о Нью-Йорке"(Сделал, как было в видео, но не успел сравнить текст с тем, который есть в Вики) \n' +
                             'Лучше все писать с большой буквы'
                             , random_id = time.time() * 100)

        elif event.text == 'Информация о Нью-Йорке':
            ny = wiki.page("ny")
            vk.messages.send(user_id = event.user_id, message = 'Можешь все не читать. Просто сравни с тем, что написано в Википедии.\n\n'
                             + wiki.summary("ny")
                             + '\n\nСсылка на статью ' + ny.url,
                             random_id = time.time() * 1000)
        
        elif event.text == 'Работай':
            if event.from_user:
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        if event.text != 'Все':
                            vk.messages.send(user_id = event.user_id, message = 'У меня 3 по русскому еле-еле, ты написал слишком страшные слова. Я загуглил, вот такое нашел: \n' + wiki.summary(event.text), random_id = time.time() * 1000)
                            page = wiki.page(event.text)
                            
                            for i in range(len(page.images)):
                                link_photo = page.images[i]
                                
                                if link_photo[len(link_photo) - 3: len(link_photo)] == 'jpg':
                                    r = requests.get(page.images[i])

                                    with open('WikiImg' + str(i) + '.jpg', 'wb') as f:
                                        f.write(r.content)
                                    
                                    photos.append(upload.photo('WikiImg' + str(i) + '.jpg', album_id = 268947299, group_id = 189290488)) 
                                    photo = photos[-1]
                                    vk.messages.send(user_id = event.user_id, message = str(page.url), attachment = 'photo' + str(photo[0]['owner_id']) + '_' + str(photo[0]['id']), random_id = time.time() * 1000)
                            
                            html_code = requests.get('https://yandex.ru/pogoda/moscow/month?via=ms').text
                            soup = BS(html_code, 'lxml')
                            
                            for day in soup.findAll('div', {'class':'climate-calendar-day climate-calendar-day_with-history'}):
                                day_celc = day.find('div', {'class':'temp climate-calendar-day__temp-day'})
                                night_celc = day.find('div', {'class':'temp climate-calendar-day__temp-night'})
                                vk.messages.send(user_id = event.user_id, message = day.find('h6', {'class':'climate-calendar-day__detailed-day'}).text, random_id = time.time() * 1000)
                                vk.messages.send(user_id = event.user_id, message = 'Температура днем '+ day_celc.find('span', {'class':'temp__value'}).text, random_id = time.time() * 1000)
                                vk.messages.send(user_id = event.user_id, message = 'Температура ночью '+ night_celc.find('span', {'class':'temp__value'}).text, random_id = time.time() * 1000)
                        else:
                            break
        elif event.text == 'ps':
            for i in range(1, 3):
                html_code = requests.get('https://store.playstation.com/ru-ru/grid/STORE-MSF75508-PRICEDROPSCHI/'+str(i)).text
                soup = BS(html_code, 'lxml')

                for product in soup.findAll('div', {'class':'grid-cell grid-cell--game'}):
                    product_name = product.find('div', {'class':'grid-cell__title'}).span.text
                    product_not_sale_price = product.find('div', {'class':'price'}).text
                    product_sale_price = product.find('h3', {'class':'price-display__price'}).text
                    product_image = product.find('div', {'class':'product-image__img product-image__img--main'}).img.get('src')
                        
                    name_game = product.find('div', {'class': 'grid-cell__body'})
                    html_code_game = requests.get('https://store.playstation.com' + name_game.a.get('href')).text
                    soup2 = BS(html_code_game, 'lxml')
                    for game in soup2.findAll('div', {'class': 'pdp__description'}):
                            game_title = game.find('p', {'style': 'direction:ltr'})
                            vk.messages.send(user_id = event.user_id, message = product_name + '\n' + 'https://store.playstation.com' + product.a.get('href') + '\n' + 'Цена без скидки '+product_not_sale_price + '\n' + 'Цена со скидкой '+product_sale_price + '\n' + game_title.text, random_id = time.time() * 1000)
        elif event.text == 'steam':
            for i in range(1, 3):
                html_code = requests.get('https://store.steampowered.com/search/?specials=1&page=1').text
                soup = BS(html_code, 'lxml')
                product_list = soup.find('div', {'id': "search_result_container"})

                for product in product_list.findAll('a'):
                    t = product.find('span', {'class': "title"}).text
                    r2 = product.find('div', {'class': "col search_price discounted responsive_secondrow"}).text
                    r4 = r2.split(".")[1]
                    vk.messages.send(user_id = event.user_id, message = product.get('href') + '\n'
                                     + t + '\n'
                                     + "цена до: " + r2 + '\n'
                                     + "цена после: " + r4, random_id = time.time() * 1000)
        elif event.text == 'интересные статьи':
            html_code = requests.get('https://habr.com/ru/').text
            soup = BS(html_code, 'lxml')

            posts_list = soup.find('div', {'class': 'posts_list'})
            posts = posts_list.find('ul', {'class': 'content-list content-list_posts shortcuts_items'})

            for post in posts.findAll('li', {'class': 'content-list__item content-list__item_post shortcuts_item'}):
                try:
                    title = post.find('h2', {'class', 'post__title'})
                    context = post.find('div', {'class': 'post__text post__text-html'})
                    vk.messages.send(user_id = event.user_id, message = title.text + '\n' + title.a.get('href') + '\n\n'
                                         + context.text + '\n', random_id = time.time() * 1000)
                except:
                    break
        elif event.text == 'Ситилинк' or event.text == 'ситилинк':
            if event.from_user:
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        if event.text != 'Все':
                            search = event.text.split()
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
                                name = title.a.get('title')
                                Text = item.find('p', {'class': 'short_description'}).text

                                vk.messages.send(user_id = event.user_id, message = name + '\n' + title.a.get('href') + '\n'
                                         + Text, random_id = time.time() * 1000)
        elif event.text == 'Бессоница' or event.text == 'бессоница':
            html_code = requests.get('http://xn--90aialyadc0aa3d.xn--p1ai/articles/7-vidov/').text

            soup = BS(html_code, 'lxml')
            wrapper = soup.find('div', {'class': 'wrapper'})
            article = wrapper.find('div', {'class': 'article-wrapper'})
            container = article.find('div', {'class': 'article-container'})
            vk.messages.send(user_id = event.user_id, message = container.text, random_id = time.time() * 1000)
