import numpy as np
import string
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

# подгружаем лэджер
ledger = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Sales_profile/Revenue_ledger_20_06_22.xlsx', dtype='str')
# подгружаем отчет leads_join_deals
ljd = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Sales_profile/leads_join_deals_v2_20_06_2022.csv', sep=',')
# подгружаем список соотношения имен в разных базах
# name_dict = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Sales_profile/names_dict.xlsx')
# print(ljd.info())

'''обрабатываем ledger'''
ledger_new = ledger[['Email', 'Owner', 'lead creation date', 'lead creaction month', 'Course type', 'Student status',
                     'Refund (if applicable)', 'Payment type', 'Full payment', 'lead_Id']].copy()
ledger_new = ledger_new.dropna(subset=['lead_Id'])
ledger_new['lead_Id'] = ledger_new['lead_Id'].astype('int64')
ledger_new['Discontinued'] = ledger_new['Student status'].apply(lambda x: 1 if x == 'Discontinued' else 0)
ledger_new['Refund (if applicable)'] = ledger_new['Refund (if applicable)'].fillna(0)
ledger_new['Full payment'] = pd.to_numeric(ledger_new['Full payment'], errors='coerce').fillna(0)
ledger_new['Paid'] = ledger_new['Email'].apply(lambda x: 1)


''' обрабатываем лиды и создаем список '''
ljd_new = ljd[['l.Id', 'l.Created Time', 'l.Is Converted?', 'd.Lead quality', 'd.Category', 'd.Current salary',
               'd.Education', 'd.Employment status', 'd.Goal for study', 'd.Work experience']].copy()
# ljd_new['l.Id'] = ljd_new['l.Id'].astype('object')
# print(ljd_new.head())
ljd_new['month'] = pd.to_datetime(ljd_new['l.Created Time']).dt.month


df = pd.merge(ledger_new, ljd_new, left_on='lead_Id', right_on='l.Id', how='left')
print(df.info())


'''смотрим churn по типам оплат'''
sales_info = df.groupby(by=['Payment type'], as_index=False)[['Paid', 'Discontinued']].sum().sort_values(by='Paid', ascending=False).reset_index()
sales_info['CR_churn'] = sales_info['Discontinued'] / sales_info['Paid']
print(sales_info)


'''смотрим churn по goal study'''
sales_info = df.groupby(by=['d.Goal for study'], as_index=False)[['Paid', 'Discontinued']].sum().sort_values(by='Paid', ascending=False).reset_index()
sales_info['CR_churn'] = sales_info['Discontinued'] / sales_info['Paid']
print(sales_info)


'''смотрим churn по cur salary DA'''
df_DA = df[df['Course type'] == 'DA']
sales_info_DA = df_DA.groupby(by=['d.Current salary'], as_index=False)[['Paid', 'Discontinued']].sum().sort_values(by='Paid', ascending=False).reset_index()
sales_info_DA['CR_churn'] = sales_info_DA['Discontinued'] / sales_info_DA['Paid']
sales_info_DA = sales_info_DA.sort_values(by='CR_churn', ascending=False)
print(sales_info_DA)

'''смотрим churn по cur salary FS'''
df_FS = df[df['Course type'] == 'FS']
sales_info_FS = df_FS.groupby(by=['d.Current salary'], as_index=False)[['Paid', 'Discontinued']].sum().sort_values(by='Paid', ascending=False).reset_index()
sales_info_FS['CR_churn'] = sales_info_FS['Discontinued'] / sales_info_FS['Paid']
sales_info_FS = sales_info_FS.sort_values(by='CR_churn', ascending=False)
print(sales_info_FS)



