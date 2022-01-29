import json
from pprint import pprint


with open('C:/Users/nick-/Documents/DS/projects/SF_tasks/recipes.json') as f:  # Открываем файл и связываем его с объектом "f"
    recipes = json.load(f)  # Загружаем содержимое открытого файла в переменную recipes

# pprint(len(recipes[0]['ingredients']))  # Выводим на экран содержимое переменной recipes, используя функция pprint()

# for recipe in recipes: # начинаем перебор всех блюд входящих в список
#     if recipe['id'] == 13121: # если id текущего блюда равен заданному для поиска
#         print(recipe['cuisine']) # выводим на экран наименование кухни, к которой относится блюдо
#         break # прерываем выполнение цикла, т.к. нужное блюдо найдено


# cuisines = set()  # создаём пустое множество для хранения уникальных значений кухонь
# for recipe in recipes:  # начинаем перебор всех рецептов
#     cuisines.add(recipe['cuisine']) # добавляем название типа кухни к множеству
# print(len(cuisines)) # Выводим на экран полученное значение


cuisines = []  # Создаём пустой список для хранения уникальных значений кухонь
for recipe in recipes:  # Начинаем перебор всех рецептов
    if not (recipe['cuisine'] in cuisines):  # Если тип кухни текущего блюда ещё не встречался
        cuisines.append(recipe['cuisine'])  # Добавляем его к списку cuisines
valreccuisine = {}  # Создаём пустой словарь для хранения информации об количествах рецептов в каждой кухне
for item in cuisines:  # Перебираем список кухонь
    valreccuisine[item] = 0  # Добавляем в словарь ключ, соответствующий очередной кухне
for recipe in recipes:  # Перебираем список рецептов
    valreccuisine[recipe['cuisine']] += 1  # Увеличиваем значение нужного ключа в словаре на 1

print(max(valreccuisine, key=valreccuisine.get))