# import requests # Импортируем модуль requests
# token = '1c73cb561c73cb561c73cb56e51c08db5711c731c73cb567d86a14b1b8168897c98f485' # Указываем свой сервисный токен
# url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес обращения
# params = {'group_id': 'vk', 'v': 5.95, 'access_token': token} # Формируем строку параметров
# response = requests.get(url, params = params) # Посылаем запрос
# data = response.json() # Ответ сохраняем в переменной data в формате словаря
# print(data) # Выводим содержимое переменной data на экран (отображён фрагмент)
# print(len(data['response']['items'])) # Выводим на экран количество элементов словаря


'''выгружаем по 5 человек - можно также сделать для тысячи'''
# import requests # Импортируем модуль requests
# token = '1c73cb561c73cb561c73cb56e51c08db5711c731c73cb567d86a14b1b8168897c98f485' # Указываем свой сервисный токен
# url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес обращения
# count = 5
# offset = 0
# user_ids = []
# max_count = 20
# while offset < max_count:
#     # Будем выгружать по count=5 пользователей,
#     # начиная с того места, где закончили на предыдущей итерации (offset)
#     print('Выгружаю {} пользователей с offset = {}'.format(count, offset))
#     params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token}
#     response = requests.get(url, params = params)
#     data = response.json()
#     user_ids += data['response']['items']
#     # Увеличиваем смещение на количество строк, которое мы уже выгрузили
#     offset += count
# print(user_ids)


'''делаем задержку в выгрузке, чтобы не кикнули'''
import requests # Импортируем модуль requests
# import time # Импортируем модуль time
# token = '1c73cb561c73cb561c73cb56e51c08db5711c731c73cb567d86a14b1b8168897c98f485' # Указываем свой сервисный токен
# url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес страницы, к которой делаем запрос
# count = 1000
# offset = 0
# user_ids = []
# while offset < 5000:
#     params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token}
#     response = requests.get(url, params = params)
#     data = response.json()
#     user_ids += data['response']['items']
#     offset += count
#     print('Ожидаю 0.5 секунды...')
#     time.sleep(0.5)
# print('Цикл завершен, offset =',offset)


'''работаем с содержимым стены'''
import requests # Импортируем модуль requests
from pprint import pprint # Импортируем функцию pprint()
token = '1c73cb561c73cb561c73cb56e51c08db5711c731c73cb567d86a14b1b8168897c98f485' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/wall.get' # Указываем адрес страницы, к которой делаем запрос
params = {'domain': 'vk', 'filter': 'owner', 'count': 1000, 'offset': 0, 'access_token': token, 'v': 5.95}
response = requests.get(url, params = params)
# pprint(response.json())

stats = {}
count_post = 0 # Счётчик «непустых» сообщений
for record in response.json()['response']['items'][:]:
    title = record['text'][:30]
    if title:
        stats[title] = [record['comments']['count'], record['likes']['count'], record['reposts']['count'], record['date']]
        count_post += 1
    if count_post < 10:
        continue
    else:
        break
pprint(stats)