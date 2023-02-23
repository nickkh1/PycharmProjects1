import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/'
                 'leads_0109_1510.csv', sep=',')

print(df.info())
'''делаем анализ по всему периоду с января по май 2022'''
df['Created Time'] = pd.to_datetime(df['Created On'])
# df.set_index('Date_Time').groupby(pd.Grouper(freq='D')).mean()
# df_group = df.set_index('Created Time').groupby(pd.Grouper(freq='H'))['Id'].count()
df_group = df.groupby([df['Created Time'].dt.hour])['Owner'].count().reset_index()
df_group['cum_sum'] = df_group['Owner'].cumsum()
df_group['percent'] = df_group['Owner']/df_group['Owner'].sum()*100
df_group['cum_sum_percent'] = df_group['percent'].cumsum()
print(df_group)


fig = plt.figure(figsize=(12, 6))
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
sns.barplot(data=df_group, x='Created Time', y='percent')
ax.set_title('% лидов по времени суток - all')
plt.show()

fig = plt.figure(figsize=(12, 6))
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
sns.barplot(data=df_group, x='Created Time', y='cum_sum_percent')
ax.set_title('кумулятивный % лидов по времени суток - all')
plt.show()





'''делаем анализ данных только для тех, которые в итоге купили'''
df_sales = df[(df['Lead Stage'] == 'Closed Won') | (df['Lead Stage'] == 'Downpayment made') | (df['Lead Stage'] == 'Internal EMI in progress')]
df_sales_group = df_sales.groupby([df_sales['Created Time'].dt.hour])['Owner'].count().reset_index()
df_sales_group['cum_sum'] = df_sales_group['Owner'].cumsum()
df_sales_group['percent'] = df_sales_group['Owner']/df_sales_group['Owner'].sum()*100
df_sales_group['cum_sum_percent'] = df_sales_group['percent'].cumsum()


fig = plt.figure(figsize=(12, 6))
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
sns.barplot(data=df_sales_group, x='Created Time', y='percent')
ax.set_title('% лидов по времени суток - DP, CW, Internal EMI')
plt.show()


fig = plt.figure(figsize=(12, 6))
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
sns.barplot(data=df_sales_group, x='Created Time', y='cum_sum_percent')
ax.set_title('кумулятивный % лидов по времени суток - DP, CW, Internal EMI')
plt.show()

