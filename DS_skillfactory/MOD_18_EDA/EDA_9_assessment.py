import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)


heart = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/heart.csv', sep=',')
# print(heart.head())
# print(heart.info())
# print(heart.describe())

# heart['old'] = heart['age'].apply(lambda x: 1 if x>60 else 0)
# print(heart['old'].sum())

# sns.heatmap(heart.corr(), annot=True)
# plt.show()

from sklearn import preprocessing

# инициализируем нормализатор RobustScaler
r_scaler = preprocessing.RobustScaler()
col_names = list(heart.columns)

# копируем исходный датасет
heart_r = r_scaler.fit_transform(heart)

heart_r = pd.DataFrame(heart_r, columns=col_names)

# смотрим описательные статистики, ответ 0.816232
print(heart_r.describe())