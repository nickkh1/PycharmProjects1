import numpy as np
import string
import pandas as pd
pd.set_option('display.max_columns', None)


#подгружаем информацию из airtable
# leads_df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/Leads_20_06_2022.csv', sep=',')
leads_df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/leads_16_08_2022.csv', sep=',')
ledger = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/Revenue_ledger_16_08_2022.xlsx')

print(leads_df.info())


new_leads_df = leads_df[['Email', 'Created On', 'Amount', 'lp_url', 'Lead Stage',]]

# new_leads_df['Lead Number'] = new_leads_df['Lead Number'].astype('str')
new_leads_df['Email'] = new_leads_df['Email'].astype('str')
# print(new_leads_df.head())
# new_leads_df = new_leads_df.dropna(subset=['Email'])
ledger_leads = pd.merge(ledger, new_leads_df, left_on='Email', right_on='Email', how='left')
# print(ledger_leads.tail())
ledger_leads['Created On'] = pd.to_datetime(ledger_leads['Created On'])
# ledger_leads['Lead Number'] = ledger_leads['Lead Number'].astype('object')




# print(ledger_leads.info())
#
# ledger_leads['month'] = round(ledger_leads['Created Time'].dt.month, 0)
# ledger_leads['year'] = round(ledger_leads['Created Time'].dt.year, 0)
# ledger_leads['day'] = round(ledger_leads['Created Time'].dt.day, 0)
# ledger_leads = ledger_leads.fillna(0)
# print(ledger_leads.head())

# ledger_leads.to_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/ledger_leads_29_06_22.csv', sep=',')
ledger_leads.to_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Lead_num_date/ledger_leads_16_08_22.xlsx', index= False)
