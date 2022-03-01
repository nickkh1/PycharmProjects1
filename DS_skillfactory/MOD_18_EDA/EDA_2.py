import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/wine_cleared.csv', sep=',')
# print(df.info())
# count_price = len(df['price']) # количество записей цен
# sorted_price = sorted(df['price']) # отсортированные цены
#
# if count_price % 2: # при нечетном кол-ве элементов выбираем средний по индексу
#     median = sorted_price[round(0.5*(count_price-1))]
# else: # при четном кол-ве элементов выбираем 2 средних по индексу и считаем между ними среднее арифметическое
#     index = sorted(x), round(0.5 * count_price)
#     median_ = 0.5 * (sorted_price[index-1] + sorted_price[index])
# print(median)

# print(df.corr())


# визуализируем
# import matplotlib.pyplot as plt # библиотека визуализации
# from scipy import stats # библиотека для расчетов
#
# plt.subplot(1, 2, 1) # задаем сетку рисунка количество строк и столбцов
# stats.probplot(df['points'], plot=plt) # qq plot
#
# plt.subplot(1, 2, 2) # располагаем второй рисунок рядом
# plt.hist(df['points']) # гистограмма распределения признака
#
# plt.tight_layout() # чтобы графики не наезжали другу на друга, используем tight_layout
#
# plt.show() # просмотр графика


print(df.corr(method='kendall'))