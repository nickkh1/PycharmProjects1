import numpy as np
import string
import pandas as pd
pd.set_option('display.max_columns', None)


#подгружаем информацию из airtable
at_df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Airtable/Students-All students.csv', sep=',')

# print(at_df[at_df['batch'].str.contains('FS')])

#оставляем только интересующие колонки
new_at_df = at_df.reindex(columns=['Email / login','batch','Day of payment','Owner','Name', 'Phone',
'Payment Comment', 'Status']
)

#проверяем есть ли пустые emails
new_at_df = new_at_df.dropna(subset=['Email / login'])

print(new_at_df.info())


#подгружаем информацию из Revenue Ledger
# rev = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/Airtable/Revenue_ledger.xlsx')
#
#объединяем таблицы
# rev_at = rev.merge(new_at_df, left_on='Email', right_on='Email / login', how='left')
# print(rev_at.tail())



