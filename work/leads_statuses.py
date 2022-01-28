import pandas as pd
import numpy as np
import xlsxwriter

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/Leads_dec.csv', sep=',')

# print(df.head())

# ищем дубликаты
mask = df.duplicated(subset=['Id'])
df_dup = df[mask]
df_dup.sort_values(by='Id', ascending=False)
print(df_dup.head(15))


# print(df.groupby('Lead Status')['Id'].agg('nunique').sort_values(ascending=False))