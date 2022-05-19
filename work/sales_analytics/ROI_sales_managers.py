import numpy as np
import string
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

# подгружаем лэджер
ledger = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Sales_managers/Revenue_ledger_17_05_22.xlsx')
# подгружаем отчет leads_join_deals
ljd = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Sales_managers/leads_join_deals_01_02_22_to_30_04_22.csv', sep=',')
# подгружаем список соотношения имен в разных базах
name_dict = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Sales_managers/names_dict.xlsx')


'''выбор месяца'''
month = 4


'''обрабатываем ledger и создаем список продаж'''
ledger_new = ledger[['Email', 'Owner', 'lead creation date', 'lead creaction month', 'Course type', 'Student status',
                     'Refund (if applicable)', 'Payment type', 'Full payment']].copy()
ledger_new['Discontinued'] = ledger_new['Student status'].apply(lambda x: 1 if x == 'Discontinued' else 0)
ledger_new['Refund (if applicable)'] = ledger_new['Refund (if applicable)'].fillna(0)
ledger_new['Full payment'] = pd.to_numeric(ledger_new['Full payment'], errors='coerce').fillna(0)
ledger_new['Paid'] = ledger_new['Email'].apply(lambda x: 1)

ledger_new = ledger_new.drop(columns=['Email', 'lead creation date', 'Student status'], axis=1)
ledger_new_req_month = ledger_new[ledger_new['lead creaction month'] == month]

sales_info = ledger_new_req_month.groupby(by=['Owner'], as_index=False)[['Paid', 'Full payment', 'Discontinued']].sum().sort_values(by='Paid', ascending=False)
# print(sales_info['Owner'])


''' обрабатываем лиды и создаем список '''
ljd_new = ljd[['Id', 'Lead Owner Name', 'd.Stage', 'Created Time']].copy()
ljd_new['month'] = pd.to_datetime(ljd_new['Created Time']).dt.month
ljd_new_req_month = ljd_new[ljd_new['month'] == month]
leads_info = ljd_new_req_month.groupby(by=['Lead Owner Name'], as_index=False)['Id'].count().sort_values(by='Id', ascending=False)


''' обрабатываем сделки и создаем список'''
deals = ljd[['d.Id', 'd.Deal Owner Name', 'Id', 'Created Time']].copy()
deals = deals.dropna(subset=['d.Id'])
deals['month'] = pd.to_datetime(deals['Created Time']).dt.month
deals_req_month = deals[deals['month'] == month]
deals_info = deals_req_month.groupby(by=['d.Deal Owner Name'], as_index=False)['d.Id'].count()


'''собираем все данные вместе'''
df_leads_deals = pd.merge(leads_info, deals_info, how='outer', left_on='Lead Owner Name', right_on='d.Deal Owner Name')
df_leads_deals_names = pd.merge(df_leads_deals, name_dict, how='left', left_on='Lead Owner Name', right_on='Names_CRM')
df_final = pd.merge(df_leads_deals_names, sales_info, how='outer', left_on='Names_Ledger', right_on='Owner')


'''обрабатываем конверсии'''
df_final['cr_L2S'] = df_final['Paid'] / df_final['Id']*100
df_final['cr_D2S'] = df_final['Paid'] / df_final['d.Id']*100
df_final['cr_D2FS'] = df_final['Full payment'] / df_final['d.Id']*100
df_final['cr_S2FS'] = df_final['Full payment'] / df_final['Paid']*100
df_final['cr_s2Churn'] = df_final['Discontinued'] / df_final['Paid']*100
print(df_final)


''' делаем визуализацию'''
df_final_vis = df_final.dropna(subset=['Paid']).sort_values(by='d.Id', ascending=False)

# вариант с доп осью
# fig = plt.figure(figsize=(12,8)) # Create matplotlib figure
#
# ax = fig.add_subplot(111,) # Create matplotlib axes
# ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.
#
# width = 0.4
#
# df_final_vis.plot(x='Lead Owner Name', y='d.Id', kind='bar', color='red', ax=ax, width=width, position=1)
# df_final_vis.plot(x='Lead Owner Name', y='cr_D2S', kind='bar', color='blue', ax=ax2, width=width, position=0)
#
# ax.set_ylabel('Number of Deals')
# ax2.set_ylabel('CR deal to sale, %')
#
# plt.show()


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 8),
                       gridspec_kw={
                            'width_ratios': [1, 1],
                           'wspace': 0.4}
                       )

ax[0].barh(width=df_final_vis['d.Id'], y=df_final_vis['Lead Owner Name'])
ax[1].barh(width=df_final_vis['cr_D2S'], y=df_final_vis['Lead Owner Name'])


ax[0].set_title('Кол-во лидов')
ax[1].set_title('Конверсия из сделки в продажу, %')
plt.show()







# нужно еще настроить проверку невхождения кого-то из разных списков
# более красивый график *-  https://www.python-graph-gallery.com/web-horizontal-barplot-with-labels-the-economist




