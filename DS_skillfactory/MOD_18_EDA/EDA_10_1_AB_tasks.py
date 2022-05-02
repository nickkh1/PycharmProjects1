import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)


sample_a = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ab_test-redesign_sample_a.csv', sep=',')
sample_b = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ab_test-redesign_sample_b.csv', sep=',')

sample_a['date'] = pd.to_datetime(sample_a['date'])
sample_a_grouped = sample_a.groupby('date').agg({'cid': ['count'], 'transactions': ['sum'], 'revenue': ['sum']})

sample_b['date'] = pd.to_datetime(sample_b['date'])
sample_b_grouped = sample_b.groupby('date').agg({'cid': ['count'], 'transactions': ['sum'], 'revenue': ['sum']})

'''делаем кумулятивную статистику'''
sample_a_grouped['cum_users_count'] = sample_a_grouped['cid'].cumsum()
sample_a_grouped['cum_trans_sum'] = sample_a_grouped['transactions'].cumsum()
sample_a_grouped['cum_rev_sum'] = sample_a_grouped['revenue'].cumsum()

sample_b_grouped['cum_users_count'] = sample_b_grouped['cid'].cumsum()
sample_b_grouped['cum_trans_sum'] = sample_b_grouped['transactions'].cumsum()
sample_b_grouped['cum_rev_sum'] = sample_b_grouped['revenue'].cumsum()

'''считаем конверсии'''
sample_a_grouped['convers_trans'] = sample_a_grouped['cum_trans_sum']/sample_a_grouped['cum_users_count']
sample_a_grouped['ARPU'] = sample_a_grouped['cum_rev_sum']/sample_a_grouped['cum_trans_sum']

sample_b_grouped['convers_trans'] = sample_b_grouped['cum_trans_sum']/sample_a_grouped['cum_users_count']
sample_b_grouped['ARPU'] = sample_b_grouped['cum_rev_sum']/sample_a_grouped['cum_trans_sum']

# print(round(sample_a_grouped['convers_trans'].mean()*100,2))
# print(sample_b_grouped['convers_trans'].mean()*100)

'''строим график кумулятивной конверсии'''
fig = plt.figure(figsize=(12, 6))
# добавляем систему координат
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
# строим lineplot для кумулятивной конверсии во времени в каждой группе
sns.lineplot(x='date', y='ARPU', data=sample_a_grouped, ax=ax)
# задаём подпись к графику
ax.set_title('График кумулятивной конверсии по дням')
# задаём поворот меток на оси абсцисс
ax.xaxis.set_tick_params(rotation = 45)
# задаём отображение сетки
ax.grid(True)
plt.show()


fig = plt.figure(figsize=(12, 6))
# добавляем систему координат
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
# строим lineplot для кумулятивной конверсии во времени в каждой группе
sns.lineplot(x='date', y='ARPU', data=sample_b_grouped, ax=ax)
# задаём подпись к графику
ax.set_title('График кумулятивной конверсии по дням')
# задаём поворот меток на оси абсцисс
ax.xaxis.set_tick_params(rotation = 45)
# задаём отображение сетки
ax.grid(True)
plt.show()
