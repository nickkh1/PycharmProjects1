import pandas as pd
import numpy as np
import xlsxwriter

pd.set_option('display.max_columns', None)

sales_trans_leads = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Sales/raw_data_for_Py/2022.01.31_lead_with_activity_owners.csv', sep=',')
# print(sales_trans_leads.columns)

sales_trans_leads['l.Created Time'] = pd.to_datetime(sales_trans_leads['l.Created Time'])
sales_trans_leads['c.Created Time'] = pd.to_datetime(sales_trans_leads['c.Created Time'])
sales_trans_leads['l.Converted Time'] = pd.to_datetime(sales_trans_leads['l.Converted Time'])
sales_trans_leads['l.Id'] = sales_trans_leads['l.Id'].astype(str)
sales_trans_leads['Lead_created_month'] = sales_trans_leads['l.Created Time'].dt.month
# print(sales_trans_leads.info())



'''данные по дубликатам по id'''
# mask = sales_trans_leads.duplicated(subset=['l.Id'])
# sales_trans_leads_dupl_id = sales_trans_leads[mask]
# sales_trans_leads_dupl_id.sort_values(by=['l.Id'], ascending=True)
# print(sales_trans_leads_dupl_id.info())
# # print(sales_trans_leads_dupl_id.head(20))
# # print(sales_trans_leads_dupl_id.tail(20))
#
# # избавляемся от дубликатов в id, lead owner name и call owner name - т.к. по сути дубликаты это несколько звонков от call owner (просто увеличивает кол-во данных)
# mask1 = sales_trans_leads_dupl_id.duplicated(subset=['l.Id', 'l.Lead Owner Name', 'c.Call Owner Name'])
# full_dupl = sales_trans_leads_dupl_id[mask1]
# # print(full_dupl.iloc[10])
# # print(full_dupl.loc[full_dupl['l.Id'] == '183084000005881041'])
# leads_dedupped = full_dupl.drop_duplicates(subset=['l.Id', 'l.Lead Owner Name', 'c.Call Owner Name'])
# # print(leads_dedupped.info())
# # print(leads_dedupped.loc[full_dupl['l.Id'] == '183084000005881041'])
#
# # print(sales_trans_leads_dupl_id.head(15))
# # print(sales_trans_leads_dupl_id.iloc[10])
# # print(sales_trans_leads_dupl_id.loc[sales_trans_leads_dupl_id['l.Id'] == '183084000006650885'])
#
# # смотрим где пропуски
# # cols_null_percent = sales_trans_leads.isnull().mean() * 100
# # cols_with_null = cols_null_percent[cols_null_percent>0].sort_values(ascending=False)
# # print(cols_with_null, sales_trans_leads.columns)
#


'''данные по передаче лидов на звонки другим оунерам'''
leads_trans_to_new_owner = sales_trans_leads.copy()
# print(leads_trans_to_new_owner.head(20))
# print(type(leads_trans_to_new_owner.iloc[15,4]))
# mask = leads_trans_to_new_owner.isnull()
# null_pd = leads_trans_to_new_owner[mask]
# print(leads_trans_to_new_owner.isnull().head())
new_owner_na_drop = leads_trans_to_new_owner.dropna(subset=['c.Call Owner Name'])
# print(new_owner_na_drop.info())
mask1 = new_owner_na_drop.duplicated(subset=['l.Id', 'l.Lead Owner Name', 'c.Call Owner Name'])
full_dupl = new_owner_na_drop[mask1]
leads_dedupped = full_dupl.drop_duplicates(subset=['l.Id', 'l.Lead Owner Name', 'c.Call Owner Name'])

'''считаем от кого ушли лиды и к кому пришли'''
# print(leads_dedupped.iloc[4])
print('От кого лиды ушли', leads_dedupped.groupby('c.Call Owner Name')['l.Id'].agg('nunique').sort_values(ascending=False))
print("------------------------------------------------------")
print('Кому пришли альфа-лиды', leads_dedupped.groupby('l.Lead Owner Name')['l.Id'].agg('nunique').sort_values(ascending=False))





'''делаем pivot по сэйлзам кому перетекает лид'''
# print(leads_dedupped.pivot_table(
#     values='l.Id',
#     index= 'c.Call Owner Name',
#     columns='l.Lead Owner Name',
#     aggfunc='count'
# ))







# sales_trans_leads_dupl.to_csv('C:/Users/nick-/Desktop/CI/lead_with_activity_owners_1.csv', sep=',')
# # Specify a writer
# writer = pd.ExcelWriter(path='C:/Users/nick-/Desktop/CI/lead_with_activity_owners.xlsx', engine='xlsxwriter')
# # Write your DataFrame to a file
# sales_trans_leads_dupl.to_excel(writer, 'Sheet1')
# writer.save()




