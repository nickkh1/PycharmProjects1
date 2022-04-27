import numpy as np
import pandas as pd

np.random.seed(34)

# для нормализации, стандартизации
from sklearn import preprocessing

# Для графиков
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


matplotlib.style.use('ggplot')

# сгенерируем датасет из случайных чисел
df = pd.DataFrame({
    # Бета распределение, 5 – значение альфа, 1 – значение бета, 1000 – размер
    'beta': np.random.beta(5, 1, 1000) * 60,

    # Экспоненциальное распределение, 10 – "резкость" экспоненты, 1000 – размер
    'exponential': np.random.exponential(10, 1000),

    # Нормальное распределение, 10 – среднее значение р., 2 – стандартное отклонение, 1000 – количество сэмплов
    'normal_p': np.random.normal(10, 2, 1000),

    # Нормальное распределение, 10 – среднее значение р., 10 – стандартное отклонение, 1000 – количество сэмплов
    'normal_l': np.random.normal(10, 10, 1000),
})

# Копируем названия столбцов, которые теряются при использовании fit_transform()
col_names = list(df.columns)

'''визуализируем'''
# зададим параметры холста, название и визуализируем кривые распределения:
# fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
# ax1.set_title('Исходные распределения')

# kdeplot() (KDE – оценка плотности ядра) – специальный метод для графиков распределений
# sns.kdeplot(df['beta'], ax=ax1, label ='beta')
# sns.kdeplot(df['exponential'], ax=ax1, label ='exponential')
# sns.kdeplot(df['normal_p'], ax=ax1, label ='normal_p')
# sns.kdeplot(df['normal_l'], ax=ax1, label ='normal_l')
# plt.legend()
# plt.show()


'''minmaxscaler'''
# инициализируем нормализатор MinMaxScaler
# mm_scaler = preprocessing.MinMaxScaler()
#
# # копируем исходный датасет
# df_mm = mm_scaler.fit_transform(df)
#
# # Преобразуем промежуточный датасет в полноценный датафрейм для визуализации
# df_mm = pd.DataFrame(df_mm, columns=col_names)
#
# fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
# ax1.set_title('После нормализации MinMaxScaler')
#
# sns.kdeplot(df_mm['beta'], ax=ax1)
# sns.kdeplot(df_mm['exponential'], ax=ax1)
# sns.kdeplot(df_mm['normal_p'], ax=ax1)
# sns.kdeplot(df_mm['normal_l'], ax=ax1)
# plt.show()


'''robust scaler'''
# # инициализируем нормализатор RobustScaler
# r_scaler = preprocessing.RobustScaler()
#
# # копируем исходный датасет
# df_r = r_scaler.fit_transform(df)
#
# # Преобразуем промежуточный датасет в полноценный датафрейм для визуализации
# df_r = pd.DataFrame(df_r, columns=col_names)
#
# fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
# ax1.set_title('Распределения после RobustScaler')
#
# sns.kdeplot(df_r['beta'], ax=ax1)
# sns.kdeplot(df_r['exponential'], ax=ax1)
# sns.kdeplot(df_r['normal_p'], ax=ax1)
# sns.kdeplot(df_r['normal_l'], ax=ax1)
# plt.show()


'''стандартизация'''
# инициализируем стандартизатор StandardScaler
s_scaler = preprocessing.StandardScaler()

# копируем исходный датасет
df_s = s_scaler.fit_transform(df)

# Преобразуем промежуточный датасет в полноценный датафрейм для визуализации
df_s = pd.DataFrame(df_s, columns=col_names)

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('Распределения после StandardScaler')

sns.kdeplot(df_s['beta'], ax=ax1)
sns.kdeplot(df_s['exponential'], ax=ax1)
sns.kdeplot(df_s['normal_p'], ax=ax1)
sns.kdeplot(df_s['normal_l'], ax=ax1)
plt.show()
