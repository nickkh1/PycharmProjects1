import pandas as pd
import numpy as np
import xlsxwriter

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Sales/raw_data_for_Py/Leads_jan_2022.csv', sep=',')

print(df[df['Email'] == 'skandask82@gmail.com'])

# ищем дубликаты
# mask = df.duplicated(subset=['Id'])
# df_dup = df[mask]
# df_dup.sort_values(by='Id', ascending=False)
# print(df_dup.head(15))


# print(df.groupby('Lead Status')['Id'].agg('nunique').sort_values(ascending=False))