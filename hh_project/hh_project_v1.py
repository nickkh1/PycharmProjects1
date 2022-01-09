import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

pd.set_option('display.max_columns', None)

hh_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/dst-3.0_16_1_hh_database.csv', sep=';')
# print(hh_data.info())
# print(hh_data.shape)
# print(hh_data.head(5))
# print(hh_data.describe())

# выделяем тип образования ['неоконченное высшее' 'высшее' 'среднее специальное' 'среднее']

copy_hh = hh_data.copy()


# print(copy_hh.loc[150,'Образование и ВУЗ'])


def get_edu(education):
    edu_list = education.split(' ')
    if edu_list[1] == 'образование':
        edu_type = edu_list[0].lower()
    else:
        edu_type = edu_list[0].lower() + " " + edu_list[1].lower()
    return edu_type


edu_type = copy_hh['Образование и ВУЗ'].apply(get_edu)
copy_hh['Образование'] = edu_type
# print(copy_hh['Образование'].unique())
copy_hh = copy_hh.drop(['Образование и ВУЗ'], axis=1)
# print(copy_hh[copy_hh['Образование'] == 'среднее']['Образование'].count())

# выделяем пол, возраст

# def get_sex(sex):
#     sex_list = sex.split(' ')
#     if sex_list[0] == 'Мужчина':
#         sex_type = 'М'
#     else:
#         sex_type = 'Ж'
#     return sex_type
#
# sex_type = copy_hh['Пол, возраст'].apply(get_sex)
# type_list = copy_hh['Пол, возраст'].apply(lambda x: x.split(' ')[:])
sex_type_new = copy_hh['Пол, возраст'].apply(lambda x: 'М' if x.split(' ')[0] == 'Мужчина' else 'Ж')
age_type = copy_hh['Пол, возраст'].apply(lambda x: int(x.split(' ')[3]))
copy_hh['Пол'] = sex_type_new
copy_hh['Возраст'] = age_type
copy_hh = copy_hh.drop(['Пол, возраст'], axis=1)


# print(copy_hh[copy_hh['Пол'] == 'Ж']['Пол'])
# print(round(copy_hh['Пол'].value_counts(normalize=True)['Ж'] * 100, 2))
# print(copy_hh[copy_hh['Пол'] == 'Ж']['Пол'].count()/copy_hh['Пол'].count())
# print(round(copy_hh['Возраст'].mean(),1))


# получаем опыт работы

# print(copy_hh.loc[155,'Опыт работы'])
# print(copy_hh.loc[1562,'Опыт работы'])
# print(copy_hh.loc[28381,'Опыт работы'])
#


def get_experience(exp):
    month_key_words = ['месяц', 'месяцев', 'месяца']
    year_key_words = ['год', 'лет', 'года']
    if isinstance(exp, float):
        return True
    else:
        args_splited = exp.split(' ')
        month = 0
        year = 0
        if len(args_splited) < 7:
            for i in range(len(args_splited)):
                if args_splited[i] in month_key_words:
                    month = args_splited[i - 1]
                if args_splited[i] in year_key_words:
                    year = args_splited[i - 1]
        else:
            for i in range(7):
                if args_splited[i] in month_key_words:
                    month = args_splited[i - 1]
                if args_splited[i] in year_key_words:
                    year = args_splited[i - 1]
        tot_m = int(year) * 12 + int(month)
        return tot_m


total_months = copy_hh['Опыт работы'].apply(get_experience)
copy_hh['Опыт работы (месяц)'] = total_months
copy_hh = copy_hh.drop(['Опыт работы'], axis=1)


# определяем город


def get_city(city):
    capital_cities = ['Москва', 'Санкт-Петербург']
    million_cities = ['Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань', 'Челябинск', 'Омск', 'Самара',
                      'Ростов-на-Дону', 'Уфа', 'Красноярск', 'Пермь', 'Воронеж', 'Волгоград']
    line_splited = city.split(' , ')
    if line_splited[0] in capital_cities:
        return line_splited[0]
    elif line_splited[0] in million_cities:
        return 'город-миллионник'
    else:
        return 'другие'


city_list = copy_hh['Город, переезд, командировки'].apply(get_city)
copy_hh['Город'] = city_list


#  определяем готовность к переезду, готовность к командировкам


def get_move(move):
    line_splited = move.split(' , ')
    if line_splited[1].find('м.') != -1:
        if line_splited[2].find('не') != -1:
            return False
        else:
            return True
    else:
        if line_splited[1].find('не') != -1:
            return False
        else:
            return True


ready_move = copy_hh['Город, переезд, командировки'].apply(get_move)
copy_hh['Готовность к переезду'] = ready_move


# готовность к командировкам

# print(copy_hh['Город, переезд, командировки'].loc[16].split(' , ')[1].find('м.') != -1)
# print(copy_hh['Город, переезд, командировки'].loc[15].split(' , ')[1].find('м.') != -1)


# split_lines = copy_hh['Город, переезд, командировки'].apply(lambda x: x.split(' , '))
# print(split_lines.head(35))
# split_lines_len = split_lines.apply(lambda x: len(x))
# print(split_lines_len[split_lines_len<3])
# print(split_lines.iloc[198])
# print(copy_hh['Город, переезд, командировки'].loc[198])
# print(copy_hh['Город, переезд, командировки'].loc[2927])
# print(copy_hh['Город, переезд, командировки'].loc[27530])
# print(copy_hh['Город, переезд, командировки'].loc[40165])

def get_visit(move):
    line_splited = move.split(' , ')
    if line_splited[1].find('м.') != -1:
        if len(line_splited) < 4:
            return True
        else:
            if line_splited[3].find('не') != -1:
                return False
            else:
                return True
    else:
        if len(line_splited) < 3:
            return True
        else:
            if line_splited[2].find('не') != -1:
                return False
            else:
                return True


ready_visit = copy_hh['Город, переезд, командировки'].apply(get_visit)
copy_hh['Готовность к командировкам'] = ready_visit
copy_hh = copy_hh.drop(['Город, переезд, командировки'], axis=1)


# print(copy_hh.info())
# print(copy_hh['Занятость'])
# print(copy_hh['График'])



# определяем график и занятость


work_occupancy = ['полная занятость', 'частичная занятость', 'проектная работа', 'волонтерство', 'стажировка']
for occupancy in work_occupancy:
    copy_hh[occupancy] = copy_hh['Занятость'].apply(lambda x: occupancy in x)


work_schedule = ['полный день', 'сменный график', 'гибкий график', 'удаленная работа', 'вахтовый метод']
for schedule in work_schedule:
    copy_hh[schedule] = copy_hh['График'].apply(lambda x: schedule in x)
copy_hh = copy_hh.drop(['Занятость'], axis=1)
copy_hh = copy_hh.drop(['График'], axis=1)
# print(copy_hh.info())


# mask_fly_in_fly = copy_hh['проектная работа'] == True
# mask_flexible = copy_hh['волонтерство'] == True
# print(copy_hh[mask_fly_in_fly & mask_flexible].shape[0])
#
#
# mask_fly_in_fly_1 = copy_hh['вахтовый метод'] == True
# mask_flexible_1 = copy_hh['гибкий график'] == True
# print(copy_hh[mask_fly_in_fly_1 & mask_flexible_1].shape[0])



# определяем ЗП


currency_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ExchangeRates.csv', sep=',')
currency_data['date'] = pd.to_datetime(currency_data['date']).dt.date
copy_hh['Обновление резюме'] = pd.to_datetime(copy_hh['Обновление резюме']).dt.date

copy_hh['ЗП (temp)'] = copy_hh['ЗП'].apply(lambda x: float(x.split(' ')[0]))


def get_currencies(arg):
    currencies = {'грн.':'UAH','USD':'USD','EUR':'EUR','бел.руб.':'BYN','KGS':'KGS','сум':'UZS','AZN':'AZN','KZT':'KZT','руб.':'руб.'}
    arg = arg.split(' ')
    value = currencies[arg[1]]
    return value


copy_hh['Курс (temp)'] = copy_hh['ЗП'].apply(get_currencies)

merged_hh = copy_hh.merge(
    currency_data,
    left_on=['Курс (temp)', 'Обновление резюме'],
    right_on=['currency', 'date'],
    how='left')

merged_hh['close'] = merged_hh['close'].fillna(1)
merged_hh['proportion'] = merged_hh['proportion'].fillna(1)
copy_hh['ЗП (руб)'] = merged_hh['close'] * merged_hh['ЗП (temp)'] / merged_hh['proportion']
copy_hh = copy_hh.drop(['ЗП', 'ЗП (temp)', 'Курс (temp)'], axis=1)
# print(round(copy_hh['ЗП (руб)'].median()/1000))


# print(currency_tag.value_counts(normalize=True))
# print(currency_data.info())
# print(copy_hh['ЗП'].head(15))




# визуализация

# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
# sns.histplot(
#     data=copy_hh,
#     x='Возраст',
#     bins=20,
#     kde=True,
#     ax=axes[0]
# );
# axes[0].set_title('Возраст сосискателей', fontsize=16)
# sns.boxplot(
#     data=copy_hh,
#     x='Возраст',
#     orient='h',
#     width=0.9,
#     ax=axes[1]
# );
# axes[1].set_title('Распределение возраста');
# axes[1].grid()
# # plt.show()

# print(copy_hh['Возраст'].describe())
# print(copy_hh['Возраст'].mode())

# fig.show()
# fig_1 = px.box(
#     data_frame=copy_hh,
#     x='Возраст',
#     orientation='h',
#     title='Распределение возраста'
# )
# fig_1.show()



# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
# sns.histplot(
#     data=copy_hh,
#     x='Опыт работы (месяц)',
#     bins=20,
#     kde=True,
#     ax=axes[0]
# );
# axes[0].set_title('Опыт сосискателей', fontsize=16)
# sns.boxplot(
#     data=copy_hh,
#     x='Опыт работы (месяц)',
#     orient='h',
#     width=0.9,
#     ax=axes[1]
# );
# axes[1].set_title('Распределение опыта');
# axes[1].grid()
# # plt.show()

# print(copy_hh['Опыт работы (месяц)'].describe())
# print(copy_hh['Опыт работы (месяц)'].mode())
#
#
# fig_1 = px.box(
#     data_frame=copy_hh,
#     x='Опыт работы (месяц)',
#     orientation='h',
#     title='Распределение опыта'
# )
# fig_1.show()




# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
# sns.histplot(
#     data=copy_hh,
#     x='ЗП (руб)',
#     bins=20,
#     kde=True,
#     ax=axes[0]
# );
# axes[0].set_title('ЗП сосискателей', fontsize=16)
# sns.boxplot(
#     data=copy_hh,
#     x='ЗП (руб)',
#     orient='h',
#     width=0.9,
#     ax=axes[1]
# );
# axes[1].set_title('Распределение ЗП');
# axes[1].grid()
# plt.show()

# print(copy_hh['ЗП (руб)'].describe())
# print(copy_hh['ЗП (руб)'].mode())
#
#
# fig_1 = px.box(
#     data_frame=copy_hh,
#     x='ЗП (руб)',
#     orientation='h',
#     title='Распределение ЗП'
# )
# fig_1.show()






# # Зп и образование
# fig = plt.figure(figsize=(10, 7))
# boxplot = sns.boxplot(
#     data=copy_hh[copy_hh['ЗП (руб)']<1000000],
#     y='Образование',
#     x='ЗП (руб)',
#     orient='h',
#     width=0.9
# )
# boxplot.set_title('Распределение ЗП по уровню образования');
# boxplot.set_xlabel('ЗП');
# boxplot.set_ylabel('Уровень образования');
# boxplot.grid()
# plt.show()
#
#
# bar_data = copy_hh[copy_hh['ЗП (руб)']<1000000].groupby(
#     by='Образование',
#     as_index=False
# )[['ЗП (руб)']].median().round(2)
# print(bar_data)
#
# fig = px.bar(
#     data_frame=bar_data, #датафрейм
#     x="Образование", #ось x
#     y="ЗП (руб)", #ось y
#     color='Образование', #расцветка в зависимости от страны
#     orientation='v', #ориентация графика
#     height=500, #высота
#     width=1000, #ширина
#     title='Медианная ЗП в зависимости от уровня образования' #заголовок
# )
# fig.show()



# ЗП и город
# fig = plt.figure(figsize=(10, 7))
# boxplot = sns.boxplot(
#     data=copy_hh[copy_hh['ЗП (руб)']<1000000],
#     y='Город',
#     x='ЗП (руб)',
#     orient='h',
#     width=0.9
# )
# boxplot.set_title('Распределение ЗП по городам');
# boxplot.set_xlabel('ЗП');
# boxplot.set_ylabel('город');
# boxplot.grid()
# plt.show()
#
#
# bar_data = copy_hh[copy_hh['ЗП (руб)']<1000000].groupby(
#     by='Город',
#     as_index=False
# )[['ЗП (руб)']].median().round(2)
# print(bar_data)
#
# fig = px.bar(
#     data_frame=bar_data, #датафрейм
#     x="Город", #ось x
#     y="ЗП (руб)", #ось y
#     color='Город', #расцветка в зависимости от страны
#     orientation='v', #ориентация графика
#     height=500, #высота
#     width=1000, #ширина
#     title='Медианная ЗП в зависимости от города' #заголовок
# )
# fig.show()



# # ЗП от переезда и командировок
# from numpy import median
# fig = plt.figure(figsize=(10, 7))
# barplot = sns.barplot(
#     data=copy_hh[copy_hh['ЗП (руб)']<1000000],
#     estimator=median,
#     x='Готовность к переезду',
#     y='ЗП (руб)',
#     hue='Готовность к командировкам'
# );
# barplot.set_title('Зависимость ЗП от готовности к переезду и коммандировкам');
# plt.show()



# ЗП от образования и возраста - тепловая карта
# pivot = copy_hh.pivot_table(
#     values='ЗП (руб)',
#     columns='Возраст',
#     index='Образование',
# )
# pivot.columns = pivot.columns.astype('string')
# print(pivot)
#
# heatmap = sns.heatmap(data=pivot, cmap='YlGnBu')
# heatmap.set_title('Тепловая карта ЗП по возрасту и образованию', fontsize=16);
# plt.show()


# точечная диграмма Опыт работы (месяц)») от возраста


# fig = plt.figure(figsize=(10, 5))
# scatter_data = copy_hh.copy()
# scatter_data['Опыт работы (год)'] = scatter_data['Опыт работы (месяц)']/12
# sns.lineplot(x=[0, 100], y=[0, 100])
# ax = sns.scatterplot(
#     data=scatter_data,
#     x='Возраст',
#     y='Опыт работы (год)',
# )
# ax.set_title('Зависимость опыта работы от возраста');
# plt.show()

#



# тупой график




# from numpy import median
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
# sns.barplot(
#     data=copy_hh[copy_hh['ЗП (руб)']<1000000],
#     estimator=median,
#     x='полная занятость',
#     y='ЗП (руб)',
#     ax=axes[0,0]
# );
# sns.barplot(
#     data=copy_hh[copy_hh['ЗП (руб)']<1000000],
#     estimator=median,
#     x='частичная занятость',
#     y='ЗП (руб)',
#     ax=axes[0,1]
# );
# sns.barplot(
#     data=copy_hh[copy_hh['ЗП (руб)']<1000000],
#     estimator=median,
#     x='проектная работа',
#     y='ЗП (руб)',
#     ax=axes[1,0]
# );
# sns.barplot(
#     data=copy_hh[copy_hh['ЗП (руб)']<1000000],
#     estimator=median,
#     x='волонтерство',
#     y='ЗП (руб)',
#     ax=axes[1,1]
# );
# plt.show()
