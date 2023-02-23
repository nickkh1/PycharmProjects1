import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/'
                 'leads_0109_1510.csv', sep=',')

print(df.info())
# leads_info = df.groupby(by=['Owner'], as_index=False)['First Name'].count().sort_values(by='First Name', ascending=False)
# d_new['month'] = pd.to_datetime(ljd_new['Created Time']).dt.month
# print(leads_info)