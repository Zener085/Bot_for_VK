import wikipedia
import requests

wikipedia.set_lang("ru")

page = wikipedia.page((input()))

print(page.images)

for i in range(len(page.images)):
    r = requests.get(page.images[i])
    print(r.content)
    with open('C\Desktop\Wiki' + str(i) + '.png', 'wb') as f:
        f.write(r.content)
    
    '''
    link_photo = page.images[i]
    if link_photo[len(link_photo) - 3: len(link_photo)] == 'jpg' or link_photo[len(link_photo) - 3: len(link_photo)] == 'png':
        r = requests.get(page.images[i])
        with open('Wiki' + str(i) + '.png', 'wb') as f:
        f.write(r.content)
    
    else:
        r = requests.get(page.images[i])
        with open('Wiki' + str(i) + '.', 'wb') as f:
            f.write(r.content)
    '''
