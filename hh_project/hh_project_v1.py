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
            return None
        else:
            if line_splited[3].find('не') != -1:
                return False
            else:
                return True
    else:
        if len(line_splited) < 3:
            return None
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
print(round(copy_hh['ЗП (руб)'].median()/1000))


# print(currency_tag.value_counts(normalize=True))
# print(currency_data.info())
# print(copy_hh['ЗП'].head(15))

