from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)


ab_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ab_data.csv', sep=',')

ab_data['timestamp'] = pd.to_datetime(ab_data['timestamp'], format='%Y-%m-%d')

# daily_data = ab_data.groupby(['timestamp', 'group']).agg({
#     'user_id':'count',
#     'converted':'sum'
# })\
#     .reset_index().rename(columns={'user_id': 'users_count'})
#
# daily_data['conversion'] = daily_data['converted']/daily_data['users_count']*100
#
# '''считаем кумултивные данные сразу для двух групп'''
# # вычисляем кумулятивную сумму количества посетителей
# daily_data['cum_users_count'] = daily_data.groupby(['group'])['users_count'].cumsum()
# # вычисляем кумулятивную сумму количества совершённых целевых действий
# daily_data['cum_converted'] = daily_data.groupby(['group'])['converted'].cumsum()
# # вычисляем кумулятивную конверсию
# daily_data['cum_conversion'] = daily_data['cum_converted']/daily_data['cum_users_count'] * 100
# # print(daily_data.head())




converted_piv= ab_data.groupby('group')['converted'].agg(
    ['sum', 'count'])
# print(converted_piv)

# нулевая и альтернативная гипотезы
H0 = 'Конверсии в группах А и B равны'
H1 = 'Конверсия в группе А выше, чем конверсия в группе B'
alpha = 0.05  # уровень значимости
# вычисляем значение p-value для z-теста для пропорций
_, p_value = proportions_ztest(
    count=converted_piv['sum'],  # число "успехов"
    nobs=converted_piv['count'],  # общее число наблюдений
    alternative='larger',
)
# выводим результат на экран
print('p-value: ', round(p_value, 2))
# сравниваем полученное p-value с уровнем значимости
if (p_value < alpha):
    print("Отвергаем нулевую гипотезу. {}".format(H0))
    print("Альтернативная гипотеза. H1: {}".format(H1))
else:
    print("Принимаем нулевую гипотезу. {}".format(H0))

# p-value:  0.1
# Принимаем нулевую гипотезу. Конверсии в группах А и B равны
