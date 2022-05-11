import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

leads_j_d = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/leads_join_deals_01_09_21_to_10_05_22.csv', sep=',')
#leads_join_deals_01_12_21_to_10_05_22

leads_j_d_new = leads_j_d.drop(['Company', 'Email', 'Last Name', 'Mobile', 'Website', 'Industry', 'Lead Source', 'Lead Status',
                                'Converted Time', 'Converted Contact', 'Converted Account', 'Full Name', 'Phone', 'Created By',
                                'd.Id'
                                ],
                               axis=1)

leads_j_d_new['Description'] = leads_j_d_new['Description'].fillna('')
leads_j_d_new['Description'] = leads_j_d_new['Description'].astype('string')
leads_j_d_new['webinar'] = leads_j_d_new['Description'].apply(lambda x: 1 if 'webin' in x else 0)
leads_j_d_new['Is Converted?'] = leads_j_d_new['Is Converted?'].astype('string')
leads_j_d_new['is_converted'] = leads_j_d_new['Is Converted?'].apply(lambda x: 1 if x == 'Yes' else 0)

#приводим названия курсов к одному значеню и заполняем пропуски
dict_for_courses = {'DA_webinar': 'DA', 'data analyst': 'DA', 'FS': 'FSP', 'FS-test': 'FSP', 'DA_webinar-1': 'DA',
                    'DA_webinar-2': 'DA', 'DA_webinar-3': 'DA', 'QA': 'DA', 'Data Analyst': 'DA', 'FSD': 'FSP',
                    'fsp': 'FSP', 'Test': 'DA', 'kesha':'DA'
                    }
leads_j_d_new = leads_j_d_new.replace({"Course Name": dict_for_courses})
leads_j_d_new['Course Name'] = leads_j_d_new['Course Name'].fillna('DA')
# проверка
# print(leads_j_d_new['Course Name'].value_counts(sort='Asc').reset_index()['index'])


# приводим даты в формат datetime
leads_j_d_new['Created Time'] = pd.to_datetime(leads_j_d_new['Created Time'])
leads_j_d_new['Modified Time'] = pd.to_datetime(leads_j_d_new['Modified Time'])
leads_j_d_new = leads_j_d_new.sort_values(by='Created Time')

# убираем ненужные столбцы
leads_j_d_new = leads_j_d_new.drop(['Description', 'Is Converted?', 'Converted Deal'], axis=1)

'можно сделать слловарь для статусов, которые считаются конверсией'
list_stage = ['Closed Won', 'Internal EMI in progress', 'Refunded / Churned', 'Downpayment made', 'Downpayment made (upfront)']
leads_j_d_new['was_paid'] = leads_j_d_new['d.Stage'].apply(lambda x: 1 if x in list_stage else 0)
# print(leads_j_d_new['d.Stage'].value_counts(sort='Asc'))

# print(leads_j_d_new[leads_j_d_new['Created Time'] == '2022-01-02'])

'''убираем остатки ненужных столбцов для цели расчета кумулятивной конверсии'''
leads_j_d_final = leads_j_d_new.drop(['Lead Owner Name', 'Lead Owner', 'd.Stage'], axis=1)

# print(leads_j_d_final.info())
# print(leads_j_d_final.head())

'''группируем по дням - приводим к нужному виду '''
leads_j_d_final['leads_num'] = leads_j_d_final['Id'].apply(lambda x: 1)
leads_j_d_final = leads_j_d_final.drop(['Id', 'Modified Time'], axis=1)

# разбиваем на курсы
leads_j_d_final_DA = leads_j_d_final[leads_j_d_final['Course Name']=='DA']
leads_j_d_final_FSP = leads_j_d_final[leads_j_d_final['Course Name']=='FSP']

# группируем по дням
leads_j_d_final_DA = leads_j_d_final_DA.groupby(pd.Grouper(key="Created Time", freq="D")).sum().reset_index()
leads_j_d_final_FSP = leads_j_d_final_FSP.groupby(pd.Grouper(key="Created Time", freq="D")).sum().reset_index()
leads_j_d_final_DA['Course_name'] = 'DA'
leads_j_d_final_FSP['Course_name'] = 'FSP'
leads_j_d_final_final = pd.concat([leads_j_d_final_DA, leads_j_d_final_FSP], ignore_index=True).sort_values(by='Created Time')
# print(leads_j_d_final_final.head())

'''считаем кумулятивную конверсию за 4 месяца по CRD и CR2'''
leads_j_d_final_final['cum_users_count'] = leads_j_d_final_final.groupby(['Course_name'])['leads_num'].cumsum()
# вычисляем кумулятивную сумму количества конвертаций в сделку
leads_j_d_final_final['cum_converted_CRD'] = leads_j_d_final_final.groupby(['Course_name'])['is_converted'].cumsum()
# вычисляем кумулятивную сумму количества конвертаций в первую оплату
leads_j_d_final_final['cum_converted_CR2'] = leads_j_d_final_final.groupby(['Course_name'])['was_paid'].cumsum()
# вычисляем кумулятивную конверсию CRD
leads_j_d_final_final['cum_conversion_CRD'] = leads_j_d_final_final['cum_converted_CRD']/leads_j_d_final_final['cum_users_count'] * 100
# вычисляем кумулятивную конверсию CR2
leads_j_d_final_final['cum_conversion_CR2'] = leads_j_d_final_final['cum_converted_CR2']/leads_j_d_final_final['cum_users_count'] * 100

# print(leads_j_d_final_final.head())

'''строим график кумулятивной конверсии CRD'''
# создаём фигуру размером 8x4
fig = plt.figure(figsize=(12, 6))
# добавляем систему координат
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
# строим lineplot для кумулятивной конверсии во времени в каждой группе
sns.lineplot(x='Created Time', y='cum_conversion_CRD', data=leads_j_d_final_final, hue='Course_name', ax=ax)
# задаём подпись к графику
ax.set_title('График кумулятивной конверсии CRD по дням')
# задаём поворот меток на оси абсцисс
ax.xaxis.set_tick_params(rotation = 45)
# задаём отображение сетки
ax.grid(True)
# задаем высоту оси y
ax.set(ylim=(20, 60))
plt.show()


'''строим график кумулятивной конверсии CR2'''
# создаём фигуру размером 8x4
fig = plt.figure(figsize=(12, 6))
# добавляем систему координат
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])
# добавляем кол-во лидов
# ax.barplot('Created Time', 'leads_num', data=leads_j_d_final_final, hue='Course_name')
# ax2 = ax.twinx()
# строим lineplot для кумулятивной конверсии во времени в каждой группе
sns.lineplot(x='Created Time', y='cum_conversion_CR2', data=leads_j_d_final_final, hue='Course_name', ax=ax)
# задаём подпись к графику
ax.set_title('График кумулятивной конверсии CR2 по дням')
# задаём поворот меток на оси абсцисс
ax.xaxis.set_tick_params(rotation = 45)
# задаём отображение сетки
ax.grid(True)
# задаем высоту оси y
ax.set(ylim=(0, 4))
plt.show()

