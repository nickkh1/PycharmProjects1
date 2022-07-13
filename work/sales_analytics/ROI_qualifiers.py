import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

# подгружаем данные
df = ljd = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/ROI_Qualifiers/CI_Initial_owner_Converted_13_07_22.csv', sep=',')

'''выбор месяца'''
month = 6
year = 2022

'''обрабатываем данные'''
df['month'] = pd.to_datetime(df['l.Created Time']).dt.month
df['year'] = pd.to_datetime(df['l.Created Time']).dt.year
df = df.drop_duplicates(subset=['l.Id'])
df = df[(df['month'] == month) & (df['year'] == year)]
df['converted'] = df['l.Is Converted?'].apply(lambda x: 1 if x == 'Yes' else 0)

df_count_leads = df.groupby(by=['u.Full Name'], as_index=False)['l.Id'].count().sort_values(by='l.Id', ascending=False)
df_count_deals = df.groupby(by=['u.Full Name'], as_index=False)['converted'].sum().sort_values(by='converted', ascending=False)
df_final = pd.merge(df_count_leads, df_count_deals, how='outer', on='u.Full Name')
df_final['CRD'] = df_final['converted'] / df_final['l.Id']

print(df.info())
print(df_final)


''' делаем визуализацию'''

df_final_vis =  df_final.dropna(subset=['l.Id']).sort_values(by='l.Id', ascending=False)
df_final_vis = df_final_vis[df_final_vis['l.Id'] >= 15]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 8),
                       gridspec_kw={
                            'width_ratios': [1, 1],
                           'wspace': 0.4}
                       )

ax[0].barh(width=df_final_vis['l.Id'], y=df_final_vis['u.Full Name'])
ax[1].barh(width=df_final_vis['CRD'], y=df_final_vis['u.Full Name'])


ax[0].set_title('Кол-во лидов')
ax[1].set_title('Конверсия из лида в сделку, %')
plt.show()