import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/'
                 'leads_sep22_17112022.csv', sep=',')
# df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/7f3b7a5f-9fe2-4593-ba37-9749efd16c30.csv', sep=',')

# df.to_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/leads_july.xlsx', index= False)

print(df.info())
print(df.head())