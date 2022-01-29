import requests
from bs4 import BeautifulSoup


# url = 'https://nplus1.ru/news/2021/10/11/econobel2021' # Определяем адрес страницы
# response = requests.get(url) # Выполняем GET-запрос, содержимое ответа присваивается переменной response
# page = BeautifulSoup(response.text, 'html.parser') # Создаём объект BeautifulSoup, указывая html-парсер
# # print(page.title) # Получаем тег title, отображающийся на вкладке браузера
# # print(page.title.text) # Выводим текст из полученного тега, который содержится в атрибуте text
#
# # print(page.find('h1').text)
# # print(page.find('time').text)
#
#
# print(page.find('div', class_='body').text)




# url = 'https://en.wikipedia.org/wiki/List_of_programming_languages' # Задаём адрес ресурса
# response = requests.get(url) # Делаем GET-запрос к ресурсу
# page = BeautifulSoup(response.text, 'html.parser') # Создаём объект BeautifulSoup
# # print(page.find('a')) #только первый элемент
#
# links = page.find_all('a') # Ищем все ссылки на странице и сохраняем в переменной links в виде списка
# print(len(links))
# print([link.text for link in links[500:510]])



'''работаем с VK'''
token = '1c73cb561c73cb561c73cb56e51c08db5711c731c73cb567d86a14b1b8168897c98f485' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/users.get' # Указываем адрес страницы к которой делаем запрос
params = {'user_id': 16394856, 'v': 5.95, 'fields': 'sex,bdate', 'access_token': token, 'lang': 'ru'} # Перечисляем параметры нашего запроса в словаре params
response = requests.get(url, params=params) # Отправляем запрос
# print(response.text) # Выводим текст ответа на экран

from pprint import pprint # Импортируем функцию pprint()
# pprint(response.json()) # Выводим содержимое словаря, содержащего ответ, на экран

user = response.json()['response'][0] # Извлекаем из словаря по ключу response информацию о первом пользователе
# print(user['bdate']) # Выводим дату рождения первого пользователя на экран


# ids = ",".join(map(str, range(1, 4))) # Формируем строку, содержащую информацию о поле id первых трёх пользователей
# params = {'user_ids': ids, 'v': 5.95, 'fields': 'bday', 'access_token': token, 'lang': 'ru'} # Формируем строку параметров
# # pprint(requests.get(url, params=params).json()) # Посылаем запрос, полученный ответ в формате JSON-строки преобразуем в словарь и выводим на экран его содержимое, используя функцию pprint()



url = 'https://api.vk.com/method/users.get'
ids = ",".join(map(str, range(1, 501)))
params = {'user_ids': ids, 'v': 5.95, 'fields': 'sex,bdate', 'access_token': token, 'lang': 'ru'}
response = requests.get(url, params=params).json()['response']
men=women=0
for elem in response:
    if elem['sex'] == 2:
        men+=1
    elif elem['sex'] == 1:
        women+=1
    else:
        continue
print(round(women/(men+women),2))