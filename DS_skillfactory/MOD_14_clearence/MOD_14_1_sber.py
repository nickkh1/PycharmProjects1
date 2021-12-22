import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

sber_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/sber_data.csv', sep=',')


# fig = plt.figure(figsize=(10, 7))
# boxplot = sns.boxplot(
#     data=sber_data,
#     y='price_doc',
#     x='ecology',
#     width=0.9
#

# fig = plt.figure(figsize=(10, 7))
# sns.scatterplot(data=sber_data, y='price_doc', x='kremlin_km');
# plt.show()

cols_null_percent = sber_data.isnull().mean() * 100
cols_with_null = cols_null_percent[cols_null_percent>0].sort_values(ascending=False)
# print(cols_with_null)

# colors = ['blue', 'yellow']
# fig = plt.figure(figsize=(10, 7))
# cols = cols_with_null.index
# ax = sns.heatmap(
#     sber_data[cols].isnull(),
#     cmap=sns.color_palette(colors),
# )
# plt.show()

# #создаем копию исходной таблицы
# drop_data = sber_data.copy()
# #задаем минимальный порог: вычисляем 70% от числа строк
# thresh = drop_data.shape[0]*0.7
# #удаляем столбцы, в которых более 30% (100-70) пропусков
# drop_data = drop_data.dropna(how='any', thresh=thresh, axis=1)
# #удаляем записи, в которых есть хотя бы 1 пропуск
# drop_data = drop_data.dropna(how='any', axis=0)
# #отображаем результирующую долю пропусков
# print(drop_data.isnull().mean())
# print(drop_data.shape)

# cols = cols_with_null.index
# sber_data[cols].hist(figsize=(20, 8))
# plt.show()


# #создаем копию исходной таблицы
# fill_data = sber_data.copy()
# #создаем словарь имя столбца: число(признак) на который надо заменить пропуски
# values = {
#     'life_sq': fill_data['full_sq'],
#     'metro_min_walk': fill_data['metro_min_walk'].median(),
#     'metro_km_walk': fill_data['metro_km_walk'].median(),
#     'railroad_station_walk_km': fill_data['railroad_station_walk_km'].median(),
#     'railroad_station_walk_min': fill_data['railroad_station_walk_min'].median(),
#     'hospital_beds_raion': fill_data['hospital_beds_raion'].mode()[0],
#     'preschool_quota': fill_data['preschool_quota'].mode()[0],
#     'school_quota': fill_data['school_quota'].mode()[0],
#     'floor': fill_data['floor'].mode()[0]
# }
# #заполняем пропуски в соответствии с заявленным словарем
# fill_data = fill_data.fillna(values)
# #выводим результирующую долю пропусков
# print(fill_data.isnull().mean())
# print(fill_data.shape)



# #создаем копию исходной таблицы
# indicator_data = sber_data.copy()
# #в цикле пробегаемся по названиям столбцов с пропусками
# for col in cols_with_null.index:
#     #создаем новый признак-индикатор как col_was_null
#     indicator_data[col + '_was_null'] = indicator_data[col].isnull()
# #создаем словарь имя столбца: число(признак) на который надо заменить пропуски
# values = {
#     'life_sq': indicator_data['full_sq'],
#     'metro_min_walk': indicator_data['metro_min_walk'].median(),
#     'metro_km_walk': indicator_data['metro_km_walk'].median(),
#     'railroad_station_walk_km': indicator_data['railroad_station_walk_km'].median(),
#     'railroad_station_walk_min': indicator_data['railroad_station_walk_min'].median(),
#     'hospital_beds_raion': indicator_data['hospital_beds_raion'].mode()[0],
#     'preschool_quota': indicator_data['preschool_quota'].mode()[0],
#     'school_quota': indicator_data['school_quota'].mode()[0],
#     'floor': indicator_data['floor'].mode()[0]
# }
# #заполняем пропуски в соответствии с заявленным словарем
# indicator_data = indicator_data.fillna(values)
# #выводим результирующую долю пропусков
# print(indicator_data.isnull().mean())
# print(indicator_data.shape)



# #создаём копию исходной таблицы
# combine_data = sber_data.copy()
#
# #отбрасываем столбцы с числом пропусков более 30% (100-70)
# n = combine_data.shape[0] #число строк в таблице
# thresh = n*0.7
# combine_data = combine_data.dropna(how='any', thresh=thresh, axis=1)
#
# #отбрасываем строки с числом пропусков более 2 в строке
# m = combine_data.shape[1] #число признаков после удаления столбцов
# combine_data = combine_data.dropna(how='any', thresh=m-2, axis=0)
#
# #создаём словарь 'имя_столбца': число (признак), на который надо заменить пропуски
# values = {
#     'life_sq': combine_data['full_sq'],
#     'metro_min_walk': combine_data['metro_min_walk'].median(),
#     'metro_km_walk': combine_data['metro_km_walk'].median(),
#     'railroad_station_walk_km': combine_data['railroad_station_walk_km'].median(),
#     'railroad_station_walk_min': combine_data['railroad_station_walk_min'].median(),
#     'preschool_quota': combine_data['preschool_quota'].mode()[0],
#     'school_quota': combine_data['school_quota'].mode()[0],
#     'floor': combine_data['floor'].mode()[0]
# }
# #заполняем оставшиеся записи константами в соответствии со словарем values
# combine_data = combine_data.fillna(values)
# #выводим результирующую долю пропусков
# print(combine_data.isnull().mean())



#### SF14_6
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 4))
# histplot = sns.histplot(data=sber_data, x='full_sq', ax=axes[0]);
# histplot.set_title('Full Square Distribution');
# boxplot = sns.boxplot(data=sber_data, x='full_sq', ax=axes[1]);
# boxplot.set_title('Full Square Boxplot');
# plt.show()

### Функция по методу тьюки
# def outliers_iqr_mod(data, feature, left=1.5, right=1.5):
#     x = data[feature]
#     quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
#     iqr = quartile_3 - quartile_1
#     lower_bound = quartile_1 - (iqr * left)
#     upper_bound = quartile_3 + (iqr * right)
#     outliers = data[(x<lower_bound) | (x > upper_bound)]
#     cleaned = data[(x>lower_bound) & (x < upper_bound)]
#     return outliers, cleaned
#
#
# outliers, cleaned = outliers_iqr_mod(sber_data, 'full_sq', left = 1, right = 6)
# print(f'Число выбросов по методу Тьюки: {outliers.shape[0]}')
# print(f'Результирующее число записей: {cleaned.shape[0]}')



# fig, axes = plt.subplots(1, 2, figsize=(15, 4))
#
# #гистограмма исходного признака
# histplot = sns.histplot(sber_data['mkad_km'], bins=30, ax=axes[0])
# histplot.set_title('MKAD Km Distribution');
#
# #гистограмма в логарифмическом масштабе
# log_mkad_km= np.log(sber_data['mkad_km'] + 1)
# histplot = sns.histplot(log_mkad_km , bins=30, ax=axes[1])
# histplot.set_title('Log MKAD Km Distribution');
# plt.show()



### Функция для нормального распределения
# def outliers_z_score(data, feature, log_scale=False):
#     if log_scale:
#         x = np.log(data[feature]+1)
#     else:
#         x = data[feature]
#     mu = x.mean()
#     sigma = x.std()
#     lower_bound = mu - 3 * sigma
#     upper_bound = mu + 3 * sigma
#     outliers = data[(x < lower_bound) | (x > upper_bound)]
#     cleaned = data[(x > lower_bound) & (x < upper_bound)]
#     return outliers, cleaned
#
# outliers, cleaned = outliers_z_score(sber_data, 'mkad_km', log_scale=True)
# print(f'Число выбросов по методу z-отклонения: {outliers.shape[0]}')
# print(f'Результирующее число записей: {cleaned.shape[0]}')


# def outliers_z_score_mod(data, feature, log_scale=False, left = 3, right = 3):
#     if log_scale:
#         x = np.log(data[feature]+1)
#     else:
#         x = data[feature]
#     mu = x.mean()
#     sigma = x.std()
#     lower_bound = mu - left * sigma
#     upper_bound = mu + right * sigma
#     outliers = data[(x < lower_bound) | (x > upper_bound)]
#     cleaned = data[(x > lower_bound) & (x < upper_bound)]
#     return outliers, cleaned
#
# outliers, cleaned = outliers_z_score_mod(sber_data, 'mkad_km', log_scale=True, right = 3.5)
# print(f'Число выбросов по методу z-отклонения: {outliers.shape[0]}')
# print(f'Результирующее число записей: {cleaned.shape[0]}')




# fig, axes = plt.subplots(1, 2, figsize=(15, 4))
#
# #гистограмма исходного признака
# histplot = sns.histplot(sber_data['price_doc'], bins=30, ax=axes[0])
# histplot.set_title('MKAD Km Distribution');
#
# #гистограмма в логарифмическом масштабе
# log_mkad_km= np.log(sber_data['price_doc'] + 1)
# histplot = sns.histplot(log_mkad_km , bins=30, ax=axes[1])
# histplot.set_title('Log MKAD Km Distribution');
# plt.show()
#
#
# def outliers_z_score_mod(data, feature, log_scale=False, left = 3, right = 3):
#     if log_scale:
#         x = np.log(data[feature]+1)
#     else:
#         x = data[feature]
#     mu = x.mean()
#     sigma = x.std()
#     lower_bound = mu - left * sigma
#     upper_bound = mu + right * sigma
#     outliers = data[(x < lower_bound) | (x > upper_bound)]
#     cleaned = data[(x > lower_bound) & (x < upper_bound)]
#     return outliers, cleaned
#
# outliers, cleaned = outliers_z_score_mod(sber_data, 'price_doc', log_scale=True, right = 3.7)
# print(f'Число выбросов по методу z-отклонения: {outliers.shape[0]}')
# print(f'Результирующее число записей: {cleaned.shape[0]}')



def outliers_iqr_mod(data, feature, log_scale=False, left=1.5, right=1.5):
    if log_scale:
        x = np.log(data[feature])
    else:
        x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x<lower_bound) | (x > upper_bound)]
    cleaned = data[(x>lower_bound) & (x < upper_bound)]
    return outliers, cleaned


outliers, cleaned = outliers_iqr_mod(sber_data, 'price_doc', log_scale=True, left = 3, right = 3)
print(f'Число выбросов по методу Тьюки: {outliers.shape[0]}')
print(f'Результирующее число записей: {cleaned.shape[0]}')