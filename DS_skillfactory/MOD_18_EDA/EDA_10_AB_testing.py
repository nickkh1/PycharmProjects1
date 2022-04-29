import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)


ab_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ab_data.csv', sep=',')

ab_data['timestamp'] = pd.to_datetime(ab_data['timestamp'], format='%Y-%m-%d')

daily_data = ab_data.groupby(['timestamp', 'group']).agg({
    'user_id':'count',
    'converted':'sum'
})\
    .reset_index().rename(columns={'user_id': 'users_count'})

daily_data['conversion'] = daily_data['converted']/daily_data['users_count']*100


# # создаём фигуру размером 8x4
# fig = plt.figure(figsize=(8, 4))
# # # добавляем систему координат
# # ax = fig.add_axes([8, 4, 1, 1])
# # строим boxplot для conversion по признаку group
# sns.boxplot(data=daily_data, x='conversion', y='group')
#
#
# plt.show()



# conversion_piv = daily_data.groupby('group')['conversion'].agg(
#     ['mean', 'median']
# )
# print(conversion_piv)


'''смотрим конверсии по дням'''
# # создаём фигуру размером 8x4
# fig = plt.figure(figsize=(8,4))
# # добавляем систему координат
# ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
# # строим lineplot для конверсии во времени в каждой группе
# sns.lineplot(
#     data=daily_data,
#     x='timestamp',
#     y='conversion',
#     hue='group',
#     ax=ax
# )
# # задаём подпись к графику
# ax.set_title('График конверсии по дням')
# # задаём поворот меток на оси абсцисс
# ax.xaxis.set_tick_params(rotation=45)
# # задаём отображение сетки
# ax.grid();
# plt.show()

'''смотрим данные кумулятивным итогом'''
# # выделяем данные группы А
# daily_data_a = daily_data[daily_data['group'] == 'A']
# # считаем кумулятивное количество посетителей
# daily_data_a.loc[:, 'cum_users_count'] = daily_data_a['users_count'].cumsum()
# # выводим время, количество посетителей и кумулятивное количество посетителей
# print(daily_data_a[['timestamp', 'users_count', 'cum_users_count']].head())


'''считаем кумултивные данные сразу для двух групп'''
# вычисляем кумулятивную сумму количества посетителей
daily_data['cum_users_count'] = daily_data.groupby(['group'])['users_count'].cumsum()
# вычисляем кумулятивную сумму количества совершённых целевых действий
daily_data['cum_converted'] = daily_data.groupby(['group'])['converted'].cumsum()
# вычисляем кумулятивную конверсию
daily_data['cum_conversion'] = daily_data['cum_converted']/daily_data['cum_users_count'] * 100
# print(daily_data.head())


'''строим график кумулятивной конверсии'''
# создаём фигуру размером 8x4
fig = plt.figure(figsize=(12, 6))
# добавляем систему координат
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
# строим lineplot для кумулятивной конверсии во времени в каждой группе
sns.lineplot(x='timestamp', y='cum_conversion', data=daily_data, hue='group', ax=ax)
# задаём подпись к графику
ax.set_title('График кумулятивной конверсии по дням')
# задаём поворот меток на оси абсцисс
ax.xaxis.set_tick_params(rotation = 45)
# задаём отображение сетки
ax.grid(True)
plt.show()