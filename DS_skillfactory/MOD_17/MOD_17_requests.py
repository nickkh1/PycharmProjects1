import requests
from pprint import pprint

import requests # Импортируем библиотеку requests
url = 'https://www.cbr-xml-daily.ru/daily_json.js' # Определяем значение URL страницы для запроса
response = requests.get(url) # Делаем GET-запрос к ресурсу и результат ответа сохраняем в переменной response
# print(response)
# print(response.text)


currencies = response.json() # Применяем метод json()
# pprint(currencies)
pprint(currencies['Valute']['EUR'])

print(currencies['Valute']['CZK']['Name'])