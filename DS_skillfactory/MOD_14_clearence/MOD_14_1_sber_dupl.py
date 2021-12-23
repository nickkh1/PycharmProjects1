import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

sber_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/sber_data.csv', sep=',')


# cols_null_percent = sber_data.isnull().mean() * 100
# cols_with_null = cols_null_percent[cols_null_percent>0].sort_values(ascending=False)
# # print(cols_with_null)



dupl_columns = list(sber_data.columns)
dupl_columns.remove('id')


# mask = sber_data.duplicated(subset=dupl_columns)
# sber_duplicates = sber_data[mask]
# print(f'Число найденных дубликатов: {sber_duplicates.shape[0]}')

sber_dedupped = sber_data.drop_duplicates(subset=dupl_columns)
# print(f'Результирующее число записей: {sber_dedupped.shape[0]}')

#список неинформативных признаков
low_information_cols = []

#цикл по всем столбцам
for col in sber_data.columns:
    #наибольшая относительная частота в признаке
    top_freq = sber_data[col].value_counts(normalize=True).max()
    #доля уникальных значений от размера признака
    nunique_ratio = sber_data[col].nunique() / sber_data[col].count()
    # сравниваем наибольшую частоту с порогом
    if top_freq > 0.95:
        low_information_cols.append(col)
        print(f'{col}: {round(top_freq*100, 2)}% одинаковых значений')
    # сравниваем долю уникальных значений с порогом
    if nunique_ratio > 0.95:
        low_information_cols.append(col)
        print(f'{col}: {round(nunique_ratio*100, 2)}% уникальных значений')

information_sber_data = sber_data.drop(low_information_cols, axis=1)
print(f'Результирующее число признаков: {information_sber_data.shape[1]}')



