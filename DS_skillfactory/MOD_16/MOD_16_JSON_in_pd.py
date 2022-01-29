import json
from pprint import pprint
import pandas as pd


# # with open('C:/Users/nick-/Documents/DS/projects/SF_tasks/recipes.json') as f:  # Открываем файл и связываем его с объектом "f"
# #     recipes = json.load(f)
# #
# # df = pd.DataFrame(recipes) # Создаём объект DataFrame из списка recipes
# # print(df.head())
#
#
# # import pandas as pd # Импортируем модуль pandas
# # df = pd.read_json('C:/Users/nick-/Documents/DS/projects/SF_tasks/recipes.json') # Создаём объект DataFrame, загружая содержимое файла recipes.json
# # print(df.head())
#
# '''6.4'''
# with open('C:/Users/nick-/Documents/DS/projects/SF_tasks/recipes.json') as f:  # Открываем файл и связываем его с объектом "f"
#     recipes = json.load(f)  # Загружаем содержимое открытого файла в переменную recipes
#
# all_ingredients = set()  # Создаем пустое множество для хранения реестра уникальных ингредиентов
# for recipe in recipes:  # Начинаем перебор всех блюд входящих в список
#     for ingredient in recipe['ingredients']:  # Начинаем перебор всех ингредиентов входящих в состав текущего блюда
#         all_ingredients.add(ingredient)  # Добавляем уникальный ингредиент в реестр
# # print(len(all_ingredients))
#
#
# df = pd.DataFrame(recipes)
#
# def contains(ingredient_list): # Определяем имя функции и передаваемые аргументы
#     if ingredient_name in ingredient_list: # Если ингредиент есть в текущем блюде,
#         return 1 # возвращаем значение 1
#     else: # Если ингредиента нет в текущем блюде,
#         return 0 # возвращаем значение 0
#
#
# for ingredient_name in all_ingredients: # Последовательно перебираем ингредиенты в реестре all_ingredients
#     df[ingredient_name] = df['ingredients'].apply(contains) # В DataFrame cоздаем столбец с именем текущего ингредиента и заполняем его единицами и нулями, используя ранее созданную функцию contains
#
# df['ingredients'] = df['ingredients'].apply(len)
# # print(df.head())
#
# # df.to_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/recipes.csv', index = False)

df = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/recipes.csv')
ids = list(df['id'].unique())
ingredients=list(df.columns)[3:]

def make_list(row): # Определяем имя функции и передаваемые аргументы
    ingredient_list=[] # Создаем пустой список ингредиентов текущего блюда
    for ingredient in ingredients: # Последовательно перебираем ингредиенты из реестра
        if row[ingredient].item()==1: # Если текущий ингредиент входит в состав текущего блюда
            ingredient_list.append(ingredient) # Добавляем ингредиент в список ингредиентов текущего блюда
    return ingredient_list # Возвращаем сформированный список ингредиентов


new_recipes = [] # Создаём пустой список для хранения итоговой структуры
for current_id in ids: # Организуем цикл с параметром current_id
    cuisine = df[df['id'] == current_id]['cuisine'].iloc[0] # Получаем значение соответствующей кухни, применив фильтр по текущему значению параметра цикла к DataFrame;
    current_ingredients = make_list(df[df['id'] == current_id]) # Получаем перечень ингредиентов, входящих в состав текущего блюда
    current_recipe = {'cuisine': cuisine, 'id': int(current_id), 'ingredients': current_ingredients} # Создаём текущий словарь
    new_recipes.append(current_recipe) # Добавляем созданный словарь к списку

import json # Импорт модуля json
new_recipes = json.dumps(new_recipes) # Функция dumps() модуля json сериализирует объект Python в строку формата JSON.
with open("C:/Users/nick-/Documents/DS/projects/SF_tasks/new_recipes.json", "w") as write_file: # Откроем файл new_recipes.json для записи
    write_file.write(new_recipes)