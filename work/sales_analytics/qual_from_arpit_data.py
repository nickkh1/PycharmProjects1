import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)



info_crm = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Sales_bonus/qualifies/new_funel_with_qualifiers_research1_28_05_2022.csv', sep=',')
# print(info_crm.head())


arpit_info = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Sales_bonus/qualifies/arpit_info_may.xlsx')
arpit_info = arpit_info.dropna(subset=['asdasd'])


def receive_lead_id(string_url):
    req_id = string_url[string_url.rfind('/')+1:]
    return req_id

arpit_info['id_num'] = arpit_info['asdasd'].apply(receive_lead_id)
info_crm['l.Id'] = info_crm['l.Id'].astype('str')
# arpit_info['id_num'] = pd.to_numeric(arpit_info['id_num'], errors='coerce')
arpit_info = arpit_info.dropna(subset=['id_num'])
# print(arpit_info.head())
# print(info_crm.head())
# print(info_crm.info())
info_crm_new = info_crm.merge(arpit_info, left_on='l.Id', right_on='id_num', how='left')
# print(info_crm_new.info())


arpit_info_alpha = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Sales_bonus/qualifies/arpit_info_alpha_may.xlsx')
arpit_info_alpha = arpit_info_alpha.dropna(subset=['Lead_alpha'])
arpit_info_alpha['id_num_alpha'] = arpit_info_alpha['Lead_alpha'].apply(receive_lead_id)
arpit_info_alpha['is_alpha'] = arpit_info_alpha['id_num_alpha'].apply(lambda x: 1 if x is not None else 0)


info_crm_new_incl_alpha = info_crm_new.merge(arpit_info_alpha, left_on='l.Id', right_on='id_num_alpha', how='left')
info_pivot_filter_wo_alpha = info_crm_new_incl_alpha.dropna(subset=['id_num'])
info_pivot_filter_wo_alpha = info_pivot_filter_wo_alpha[info_pivot_filter_wo_alpha['was_in_negotiation'] == 1]
pivot_wo_alpha = pd.pivot_table(info_pivot_filter_wo_alpha, index='qualifier_name', values='id_num', aggfunc='count')
print(pivot_wo_alpha)

info_pivot_filter_alpha = info_crm_new_incl_alpha.dropna(subset=['id_num_alpha'])
pivot_alpha = pd.pivot_table(info_pivot_filter_alpha, index='qualifier_name', values='id_num_alpha', aggfunc='count')
print(pivot_alpha)

