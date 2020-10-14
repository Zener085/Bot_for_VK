import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as BS

street = input()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.delivery-club.ru/moscow')

page = driver.find_element_by_class_name('wrap')
address = page.find_element_by_class_name('address-input')

actions = ActionChains(driver)
actions.click(address)
actions.perform()

element = driver.find_element_by_class_name('address-suggest__search-input')
element.send_keys(street)
driver.implicitly_wait(5)
element.send_keys(Keys.RETURN)

soup = BS(driver.page_source, 'lxml')
page = soup.find('div', {'class': 'wrap-max-width vendor-list__wrap'})
content = page.find('ul', {'class': 'vendor-list__ul'})

for item in content.find_all('li', {'class': 'vendor-item'}):
    print('')
    
    title = item_content.find('span', {'class': 'vendor-item__title'})
    print(title.text)

    time = item_content.find('span', {'class': 'vendor-item__delivery-info'})
    print('Время ожидания - ' + time.text)

driver.close()
