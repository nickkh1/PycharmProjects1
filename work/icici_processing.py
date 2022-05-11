import numpy as np
import string
import pandas as pd

pd.set_option('display.max_columns', None)

bank_sheet = pd.read_excel('C:/Users/nick-/Desktop/CI/1.Payments/icic/arch/DetailedStatement_11_05_2022.xlsx',skiprows=16)

#создаем словарь имя столбца: число(признак) на который надо заменить пропуски
values = {
    'Withdrawal Amt (INR)': 0,
    'Deposit Amt (INR)':0,
    'Cheque. No./Ref. No.': '-'
}
bank_sheet = bank_sheet.fillna(values)


# делаем преобразвоание (удление запятой), чтобы склеить два столбца в один
def repalce_comma(text):
    new_text = text.replace(',','')
    return new_text

bank_sheet = bank_sheet.astype({'Withdrawal Amt (INR)': str})
bank_sheet = bank_sheet.astype({'Deposit Amt (INR)': str})
bank_sheet = bank_sheet.astype({'Balance (INR)': str})

bank_sheet['Withdrawal Amt (INR)'] = bank_sheet['Withdrawal Amt (INR)'].apply(repalce_comma)
bank_sheet['Deposit Amt (INR)'] = bank_sheet['Deposit Amt (INR)'].apply(repalce_comma)
bank_sheet['Balance (INR)'] = bank_sheet['Balance (INR)'].apply(repalce_comma)

bank_sheet = bank_sheet.astype({'Withdrawal Amt (INR)': float})
bank_sheet = bank_sheet.astype({'Deposit Amt (INR)': float})
bank_sheet = bank_sheet.astype({'Balance (INR)': float})

#удаляем нижнюю часть
bank_sheet = bank_sheet.dropna(subset=['Value Date'],axis=0)

#приводим дату в нужный формат
bank_sheet['Value Date'] = pd.to_datetime(bank_sheet['Value Date'],dayfirst=True)
bank_sheet['year'] = bank_sheet['Value Date'].dt.year
bank_sheet['month'] = bank_sheet['Value Date'].dt.month
bank_sheet['day'] = bank_sheet['Value Date'].dt.day
# bank_sheet = bank_sheet.astype({'year': str})
# bank_sheet = bank_sheet.astype({'month': str})
# bank_sheet = bank_sheet.astype({'day': str})
# bank_sheet = bank_sheet.astype({'Value Date': str})
bank_sheet['New date'] = bank_sheet['day'].astype(str) + '/' + bank_sheet['month'].astype(str) + '/' + bank_sheet['year'].astype(str)


#внизу есть футер с комментариями к операциям за период
# bank_sheet = bank_sheet.astype({'S.N.': float})




#создаем столбец как в нашем файле
bank_sheet['Transaction Amount(INR)'] = bank_sheet['Withdrawal Amt (INR)'] + bank_sheet['Deposit Amt (INR)']

#создаем столюец DR/CR
bank_sheet['Cr/Dr'] = bank_sheet['Withdrawal Amt (INR)'].apply(lambda x: 'DR' if x>0 else 'CR')

#делаем структуру для занесения в файл
new_bank_sheet = bank_sheet.reindex(columns=['S.N.','Tran. Id','New date','Transaction Posted Date',
'Cheque. No./Ref. No.','Transaction Remarks','Cr/Dr','Transaction Amount(INR)','Balance (INR)']
)

new_bank_sheet.to_excel('C:/Users/nick-/Desktop/CI/1.Payments/icic/arch/from_py/DetailedStatement_2022_05_11.xlsx', index= False)
# print(bank_sheet.head())
# print(bank_sheet.info())
# print(new_bank_sheet.head())