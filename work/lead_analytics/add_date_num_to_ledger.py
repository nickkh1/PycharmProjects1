import numpy as np
import string
import pandas as pd
pd.set_option('display.max_columns', None)


#подгружаем информацию из airtable
leads_df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/Leads_17_05_22.csv', sep=',')
ledger = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/revenue_ledger_17_05_22.xlsx')



new_leads_df = leads_df[['Email', 'Id', 'Created Time']]
new_leads_df = new_leads_df.dropna(subset=['Email'])
ledger_leads = pd.merge(ledger, new_leads_df, on='Email', how='left')

ledger_leads['Created Time'] = pd.to_datetime(ledger_leads['Created Time'])
ledger_leads['Id'] = ledger_leads['Id'].astype('object')
# print(ledger_leads.info())
#
# ledger_leads['month'] = round(ledger_leads['Created Time'].dt.month, 0)
# ledger_leads['year'] = round(ledger_leads['Created Time'].dt.year, 0)
# ledger_leads['day'] = round(ledger_leads['Created Time'].dt.day, 0)
# ledger_leads = ledger_leads.fillna(0)
# print(ledger_leads.head())

ledger_leads.to_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/ledger_leads_17_05_22.csv', sep=',')

