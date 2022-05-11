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


'''Считаем Confidence interval'''
ab_data1 = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ab_data.csv', sep=',')
#фильтруем данные группы А
a_data = ab_data1[ab_data1['group'] == 'A']
#фильтруем данные группы B
b_data = ab_data1[ab_data1['group'] == 'B']

from scipy.stats import norm
def proportions_conf_interval(n, x_p, gamma=0.95):
    alpha = 1 - gamma # уровень значимости
    z_crit = -norm.ppf(alpha/2) # z критическое
    eps = z_crit * (x_p * (1 - x_p) / n) ** 0.5 #погрешность
    lower_bound = x_p - eps # левая (нижняя) граница
    upper_bound = x_p + eps # правая (верхняя) граница
    # возвращаем кортеж из округлённых границ интервала
    return round(lower_bound * 100, 2), round(upper_bound * 100, 2)

conf_interval_a = proportions_conf_interval(
n=a_data['user_id'].count(), # размер выборки
x_p=a_data['converted'].mean() # выборочная пропорция
)
conf_interval_b = proportions_conf_interval(
n=b_data['user_id'].count(), # размер выборки
x_p=b_data['converted'].mean() # выборочная пропорция
)
print('Доверительный интервал для конверсии группы А: {}'.format(conf_interval_a))
print('Доверительный интервал для конверсии группы B: {}'.format(conf_interval_b))


'''считаем CI для разницы выборок'''
def diff_proportions_conf_interval(n, xp, gamma=0.95):
    alpha = 1 - gamma # уровень значимости
    diff = xp[1] - xp[0] # выборочная разница конверсий групп B и A
    z_crit = -norm.ppf(alpha/2) # z критическое
    eps = z_crit * (xp[0] * (1 - xp[0])/n[0] + xp[1] * (1 - xp[1])/n[1]) ** 0.5 # погрешность
    lower_bound = diff - eps # левая (нижняя) граница
    upper_bound = diff + eps # правая (верхняя) граница
    # возвращаем кортеж из округлённых границ интервала
    return round(lower_bound *100, 2), round(upper_bound * 100, 2)


n = [1000, 1000]
xp = [45/1000, 50/1000]

# # размеры выборок групп А и B
# n = [a_data['user_id'].count(), b_data['user_id'].count()]
# # выборочная пропорция групп A и B
# xp = [a_data['converted'].mean(), b_data['converted'].mean()]
# # строим доверительный интервал для разности конверсий
diff_inverval = diff_proportions_conf_interval(n, xp)
print(xp)
print('Доверительный интервал для разности конверсий: {}'.format(diff_inverval))