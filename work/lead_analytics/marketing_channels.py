import numpy as np
import string
import matplotlib.pyplot as plt
import re
import pandas as pd
pd.set_option('display.max_columns', None)

# # подгружаем лэджер
# ledger = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Sales_profile/Revenue_ledger_20_06_22.xlsx', dtype='str')
# # подгружаем отчет leads_join_deals
ljd = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Marketing/leads_join_deals_v2_mar_jun_2022.csv', sep=',')
print(ljd.info())

''' обрабатываем лиды и создаем список '''
ljd_new = ljd[['l.Id', 'l.Created Time', 'l.Is Converted?', 'd.Lead quality', 'd.Category', 'd.Current salary',
               'd.Education', 'd.Employment status', 'd.Goal for study', 'd.Work experience', 'l.Description',
               'was_in_EMI_CI', 'was_in_deal', 'was_in_qualification', 'was_in_negotiation', 'was_in_DP',
               'was_in_full_p']].copy()
ljd_new['month'] = pd.to_datetime(ljd_new['l.Created Time']).dt.month
ljd_new = ljd_new.dropna(subset=['l.Description'])


def receive_utm_source(text):
    try:
        found = re.search('utm_source=(.+?)&', text).group(1)
    except AttributeError:
    #     # AAA, ZZZ not found in the original string
        found = '' # apply your error handling
    return found

'''делаем поле с utm source'''
ljd_new['utm_source'] = ljd_new['l.Description'].apply(receive_utm_source)

dp_source = ljd_new.groupby(by=['utm_source'], as_index=False)['was_in_DP'].agg(['sum', 'count']).reset_index()
dp_source['CR'] = dp_source['sum'] / dp_source['count'] *100
print(dp_source)


ljd_copy = ljd_new.dropna(subset=['d.Lead quality']).copy()
ljd_copy['d.Lead quality'] = ljd_copy['d.Lead quality'].astype('category')
pp = pd.pivot_table(ljd_copy, index=['utm_source'], columns=['d.Lead quality'], values=['was_in_DP'], aggfunc=['count'], margins=True)
print(pp)