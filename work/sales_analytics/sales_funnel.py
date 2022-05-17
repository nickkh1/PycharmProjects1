import pandas as pd
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

pd.set_option('display.max_columns', None)

df_douplicated = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Funnel/'
                 'leads_join_deals_v2_02_05_22_to_08_05_22.csv', sep=',')

# после SQL запроса дублируются некоторые лиды, видимо из-за одинаковых статусов в таблицах для выборки
df = df_douplicated.drop_duplicates()

df['is_lead'] = df['Id'].apply(lambda x: 1 if x is not None else 0)

df_dropped = df.dropna(axis=1).drop(columns=['Id', 'Last Name', 'Lead Owner Name', 'Lead Owner', 'Is Converted?',
                                             'Full Name', 'Modified Time', 'Created By', 'Lead Status'])
df_dropped["Created Time"] = pd.to_datetime(df_dropped["Created Time"])
df_dropped['month'] = df_dropped['Created Time'].dt.month
df_dropped = df_dropped.drop(columns=['Created Time'])
'''выбираем месяц'''
df_series = df_dropped[df_dropped['month']==5].drop(columns=['month']).sum()

df_df = pd.DataFrame(data=df_series).reset_index().rename(columns={'index': 'Name', 0: 'Sum'})
df_df = df_df.sort_values(by='Sum', ascending=False)
# print(df_df)

#добавляем визуал
fig = px.funnel(df_df, y='Name', x='Sum')
fig.show()
# получаются какие-то странные неправильные данные