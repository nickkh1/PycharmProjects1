import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

pd.set_option('display.max_columns', None)

data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/wine_cleared_.csv', sep=',')

# для удобства сразу преобразуем признак в int
data['price_round'] = data['price'].round().astype(int)

regex = '\d{4}'  # регулярное выражение для нахождения чисел
data['year'] = data['title'].str.findall(regex).str.get(0)

data['is_usa'] = data['country'].apply(lambda x: 1 if x == 'US' else 0)
data['is_france'] = data['country'].apply(lambda x: 1 if x == 'France' else 0)
data['is_italy'] = data['country'].apply(lambda x: 1 if x == 'Italy' else 0)

# преобразуем признак year в объект datetime для удобного сравнения дат
data['year'] = pd.to_datetime(data['year'], errors='coerce')
# для сравнения используем год, заполняем значения признака old_wine, где год вина меньше 2010
data['old_wine'] = data['year'].apply(lambda x: 1 if x.year < 2010 else 0)

regex_1 = '\((.*?)\)'
data['locality'] = data['title'].str.findall(regex_1).str.get(0)
# print(data.head())

country_population = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/country_population.csv', sep=';')
# print(country_population[country_population['country'] == 'Italy'])

data = data.join(country_population.set_index('country'), on='country')
# print(data.head())

country_area = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/country_area.csv', sep=';')
# print(country_area.head())
data = data.join(country_area.set_index('country'), on='country')
# print(data[data['title'] == 'Gård 2014 Grand Klasse Reserve Lawrence Vineyards Viognier (Columbia Valley (WA))'])



'''Для задания'''
data['year'] = pd.to_datetime(data['year'])
data['years_diff'] = (pd.to_datetime("2022-01-12") - data['year']).dt.days
print(data['years_diff'].max())
