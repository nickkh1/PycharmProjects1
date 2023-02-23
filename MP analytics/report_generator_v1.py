import numpy as np
import string
import pandas as pd
import os

pd.set_option('display.max_columns', None)


'выбираем файл'
# dirName = 'C:/Users/nick-/Desktop/TG_test'
# listOfFiles = list()
# for(dirpath, dirnames, filenames) in os.walk(dirName):
#     listOfFiles += [os.path.join(dirpath, file) for file in filenames]
# for elem in listOfFiles:
#     print(elem)



df = pd.read_excel('C:/Users/nick-/Desktop/TG_test/2023-01-22—2023-02-20_Мебель_Мебель_для_прихожей_Вешалки_для_одежды_напольная.xlsx')
# print(db_1.info())
print(df.columns)

sellers_df_sorted = df.pivot_table(index=['Продавец'],
                                values=['Выручка', 'Отзывы','Рейтинг','Товар'],
                                aggfunc={'Выручка': np.sum, 'Отзывы': np.mean, 'Рейтинг': np.mean, 'Товар': len}).sort_values(by='Выручка', ascending=False)

print(sellers_df_sorted.head())
print(sellers_df_sorted['Выручка'].sum())
# print(df['Выручка'].sum())