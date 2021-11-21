import pandas as pd
import os
pd.set_option('display.max_columns', None)

''' функция для просмотра названий всех файлов в директории
https://docs-python.ru/standart-library/modul-os-python/funktsija-listdir-modulja-os/
'''
# path = 'C:/Users/nick-/Documents/DS/projects/SF_tasks'
# rez = sorted(os.listdir(path))
# print(rez)



movies = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/movies.csv', sep=',')
ratings1 = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ratings1.csv', sep=',')
ratings2 = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ratings2.csv', sep=',')
dates = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/dates.csv', sep=',')

ratings = pd.concat([ratings1,ratings2], ignore_index=True)
ratings = ratings.drop_duplicates(ignore_index=True)
ratings_dates = pd.concat([ratings, dates], axis=1)
# print(ratings_dates.tail(5))

# joined_false = ratings_dates.join(
#     movies,
#     rsuffix='_right',
#     how='left'
# )
# print(joined_false)

joined = ratings_dates.join(
    movies.set_index('movieId'),
    on='movieId',
    how='left'
)
# print(joined)


merged = ratings_dates.merge(
    movies,
    on='movieId',
    how='left'
)
# print(merged.head())



