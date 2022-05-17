import numpy as np
import string
import pandas as pd
pd.set_option('display.max_columns', None)


#подгружаем информацию из airtable
at_df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Airtable/All_students_16_05_2022.csv', sep=',')

# print(at_df.info())


#оставляем только интересующие колонки
new_at_df = at_df.reindex(columns=['Email / login','batch','Day of payment','Owner','Name', 'Phone',
'Payment Comment', 'Status', 'Student referral', 'Employee referral', 'Mode of payment', 'Course Kick-Off',
'NOT Reason', 'Refund reasons', 'Refund call status', 'Refund', 'Primary refund reason', 'TL Refund comment']
)

#проверяем есть ли пустые emails
new_at_df = new_at_df.dropna(subset=['Email / login'])
new_at_df = new_at_df.dropna(subset=['Student referral', 'Employee referral'], how='all')
# new_at_df['was_referred_st'] = new_at_df['Student referral'].apply(lambda x: 1 if x is not None else 0)
# new_at_df['was_referred_em'] = new_at_df['Employee referral'].apply(lambda x: 1 if x is not None else 0)
# new_at_df['was_referred'] = new_at_df['was_referred_em'] + new_at_df['was_referred_st']
# referred_at_dt = new_at_df[new_at_df['was_referred'] == 1]


new_at_df = new_at_df.drop(['Mode of payment', 'Course Kick-Off',
'NOT Reason', 'Refund reasons', 'Refund call status', 'Refund', 'Primary refund reason', 'TL Refund comment',
'Name', 'Phone', 'Payment Comment'
],
axis=1)


# print(new_at_df)
# print(new_at_df.info())

print(new_at_df['Email / login'])


#подгружаем информацию из Revenue Ledger
# rev = pd.read_excel('C:/Users/nick-/Desktop/CI/4.Analytics section/Airtable/Revenue_ledger.xlsx')
#
#объединяем таблицы
# rev_at = rev.merge(new_at_df, left_on='Email', right_on='Email / login', how='left')
# print(rev_at.tail())



