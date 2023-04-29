# импорт пакетов
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure


matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)


# чтение данных
df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/leads_1122_0423_DA.csv', sep=',')

# shape and data types of the data
# print(df.shape)
# print(df.dtypes)

# отбор числовых колонок
# df_numeric = df.select_dtypes(include=[np.number])
# numeric_cols = df_numeric.columns.values
# print(numeric_cols)

# отбор нечисловых колонок
# df_non_numeric = df.select_dtypes(exclude=[np.number])
# non_numeric_cols = df_non_numeric.columns.values
# print(non_numeric_cols)

# cols = df.columns[:] # первые 30 колонок
# # определяем цвета
# # желтый - пропущенные данные, синий - не пропущенные
# colours = ['#000099', '#ffff00']
# sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
# plt.show()


# for col in df.columns:
#     pct_missing = np.mean(df[col].isnull())
#     print('{} - {}%'.format(col, round(pct_missing*100)))


cols_to_drop = ['Last Name', 'Amount', 'Email', 'Course Name', 'Created By', 'Created On',
                'Gender', 'Follow Up', 'Profession', 'is_night',
                'Owner', 'Owner Email', 'Prospect ID', 'Lead Number', 'Lead Name',
                'English level', 'First Name', 'Laptop']
df_less = df.drop(cols_to_drop, axis=1)
'''убрали Laptop, т.к. в основном у всех есть - неинформативный признак'''
# for col in df_less.columns:
#     pct_missing = np.mean(df_less[col].isnull())
#     print('{} - {}%'.format(col, round(pct_missing*100)))

# print(df_no_NA['Current salary'].value_counts())
# print(df_no_NA['Goal for Study'].value_counts())
# print(df_no_NA['Education'].value_counts())
# print(df_no_NA['Work experience'].value_counts())

'''нужно сделать переход в Negotiation таргетным показателем'''
print(df_less.info())
print(df_less['Lead Stage'].value_counts())

def convert_to_qual(row):
    if row['Lead Stage'] == 'Closed Lost':
        val = 'Qualificated'
    elif row['Lead Stage'] == 'ALPHA':
        val = 'Qualificated'
    return val

df_less['result'] = df_less.apply(convert_to_qual, axis=1)

print(df_less.head(5))








'''
# print(df_less['Lead Stage'].value_counts())

df_less['Lead Stage'] = np.where((df_less['Lead Stage'] == 'Closed Won') | (df_less['Lead Stage'] == 'Down Payment Made') |
            (df_less['Lead Stage'] == 'Internal EMI in Progress'), 1, 0)

# df_less.loc[(df_less['Lead Stage'] != 'Closed Won') | (df_less['Lead Stage'] != 'Down Payment Made') |
#             (df_less['Lead Stage'] != 'Internal EMI in Progress'), 'Lead Stage'] = 0
# df_less.loc[(df_less['Lead Stage'] == 'Closed Won') | (df_less['Lead Stage'] == 'Down Payment Made') |
#             (df_less['Lead Stage'] == 'Internal EMI in Progress'), 'Lead Stage'] = 1

# print(df_less['Lead Stage'].value_counts())
# print(df_less.head(20))

df_no_NA = df_less.dropna(thresh=2)
# print(df_no_NA['Lead Stage'].value_counts())
# print(df_no_NA.head(20))

# for col in df_no_NA.columns:
#     pct_missing = np.mean(df_no_NA[col].isnull())
#     print('{} - {}%'.format(col, round(pct_missing*100)))

df_no_NA.loc[(df_no_NA['Education'] == 'Graduation') | (df_no_NA['Education'] == 'Post Graduation') |
            (df_no_NA['Education'] == '12th pass') | (df_no_NA['Education'] == 'Pursuing Graduation') |
            (df_no_NA['Education'] == 'Diploma') | (df_no_NA['Education'] == 'Post graduation') |
            (df_no_NA['Education'] == 'Pursuing graduation') | (df_no_NA['Education'] == '10th pass'), 'Education'] = 'Other'

df_no_NA['Work experience'] = df_no_NA['Work experience'].fillna('0-3')
df_no_NA = df_no_NA.dropna(subset=['Current salary'])
df_no_NA['Goal for Study'] = df_no_NA['Goal for Study'].fillna('Switch career')
# df_no_NA['Current salary'] = df_no_NA['Current salary'].fillna('3-5')


for col in df_no_NA.columns:
    pct_missing = np.mean(df_no_NA[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
print(df_no_NA['Current salary'].value_counts())
print(df_no_NA['Goal for Study'].value_counts())
print(df_no_NA['Education'].value_counts())
print(df_no_NA['Work experience'].value_counts())
# print(df_no_NA.dtypes)
print(df_no_NA.shape)
# print(df_no_NA.head(20))

'''