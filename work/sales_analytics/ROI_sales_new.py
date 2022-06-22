import numpy as np
import string
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

# подгружаем лэджер
ledger = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Sales_managers/Revenue_ledger_20_06_2022.xlsx')
# подгружаем отчет leads_join_deals
ljd = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Sales_managers/leads_join_deals_01_04to_01_06_22.csv', sep=',')
# подгружаем список соотношения имен в разных базах
name_dict = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Sales_managers/names_dict.xlsx')


'''выбор месяца'''
month = 5
year = 2022

'''обрабатываем ledger и создаем список продаж'''
ledger_new = ledger[['Email', 'Owner', 'lead creation date', 'lead creation year', 'lead creaction month', 'Course type', 'Student status',
                     'Refund (if applicable)', 'Payment type', 'Full payment', 'lead_Id']].copy()
ledger_new['lead_Id'] = ledger_new['lead_Id'].astype('object')
# print(ledger_new.info())
ledger_new['Discontinued'] = ledger_new['Student status'].apply(lambda x: 1 if x == 'Discontinued' else 0)
ledger_new['Refund (if applicable)'] = ledger_new['Refund (if applicable)'].fillna(0)
ledger_new['Full payment'] = pd.to_numeric(ledger_new['Full payment'], errors='coerce').fillna(0)
ledger_new['Paid'] = ledger_new['Email'].apply(lambda x: 1)

ledger_new = ledger_new.drop(columns=['Email', 'lead creation date', 'Student status'], axis=1)

ledger_new_req_month = ledger_new[(ledger_new['lead creation year'] == year) & (ledger_new['lead creaction month'] == month)]

sales_info = ledger_new_req_month.groupby(by=['Owner'], as_index=False)[['Paid', 'Full payment', 'Discontinued']].sum().sort_values(by='Paid', ascending=False)
# print(ledger.info())


''' обрабатываем лиды и создаем список '''
ljd_new = ljd[['Id', 'd.Id', 'Lead Owner Name', 'd.Stage', 'Created Time', 'Is Converted?', 'd.Deal Owner Name']].copy()
ljd_new['Id'] = ljd_new['Id'].astype('object')
ljd_new = ljd_new.dropna(subset=['d.Deal Owner Name'])
# print(ljd_new.info())
ljd_new['month'] = pd.to_datetime(ljd_new['Created Time']).dt.month
ljd_new_req_month = ljd_new[ljd_new['month'] == month]
# сверим кол-во сделок
# deals_info = ljd_new_req_month.groupby(by=['d.Deal Owner Name'], as_index=False)['d.Id'].count().sort_values(by='d.Id', ascending=False)
leads_info = ljd_new_req_month.groupby(by=['d.Deal Owner Name'], as_index=False)['Id'].count().sort_values(by='Id', ascending=False)
# print(deals_info)


'''собираем все данные вместе'''
df_leads_deals_names = pd.merge(leads_info, name_dict, how='left', left_on='d.Deal Owner Name', right_on='Names_CRM')
df_final = pd.merge(df_leads_deals_names, sales_info, how='outer', left_on='Names_Ledger', right_on='Owner')


'''обрабатываем конверсии'''
df_final['cr_L2S'] = df_final['Paid'] / df_final['Id']*100
df_final['cr_D2S'] = df_final['Paid'] / df_final['Id']*100
df_final['cr_D2FS'] = df_final['Full payment'] / df_final['Id']*100
df_final['cr_S2FS'] = df_final['Full payment'] / df_final['Paid']*100
df_final['cr_s2Churn'] = df_final['Discontinued'] / df_final['Paid']*100
# print(df_final)


''' делаем визуализацию'''
df_final_vis = df_final.dropna(subset=['Paid']).sort_values(by='Id', ascending=False)
df_final_vis = df_final_vis[df_final_vis['Position'] == 'SC']
print(df_final_vis)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 8),
                       gridspec_kw={
                            'width_ratios': [1, 1],
                           'wspace': 0.4}
                       )

ax[0].barh(width=df_final_vis['Id'], y=df_final_vis['d.Deal Owner Name'])
ax[1].barh(width=df_final_vis['cr_D2S'], y=df_final_vis['d.Deal Owner Name'])


ax[0].set_title('Кол-во лидов')
ax[1].set_title('Конверсия из сделки в продажу, %')
plt.show()


'''записываем excel'''
df_final.to_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Sales_managers/dataset_22_06_22.xlsx', index= False)