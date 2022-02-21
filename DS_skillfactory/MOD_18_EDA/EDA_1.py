import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/wine.csv', sep=',')

# ищем дубликаты
# mask = df.duplicated(subset=df.columns) # маска для фильтрации
# data_duplicates = df[mask] # фильтруем наш датасет
# print(f'Число найденных дубликатов: {data_duplicates.shape[0]}')

df = df.drop(['region_2'], axis=1)

# fig = plt.figure(figsize=(10, 7))
# sns.heatmap(df.isnull())
# plt.show()

# обрабатываем пропуски в категориальных признаках самым простым вариантом, замена на unknown

df['designation'] = df['designation'].fillna('unknown')
df['region_1'] = df['region_1'].fillna('unknown')
df['taster_name'] = df['taster_name'].fillna('unknown')
df['taster_twitter_handle'] = df['taster_twitter_handle'].fillna('unknown')

# признаки с маленьким количеством пропусков заменим на самые частовречающиеся значения
df['country'] = df['country'].fillna('US')
df['price'] = df['price'].fillna(df['price'].mean())
df['province'] = df['province'].fillna('California')
df['variety'] = df['variety'].fillna('Pinot Noir')



# df = df.to_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/wine_cleared.csv', index=False)