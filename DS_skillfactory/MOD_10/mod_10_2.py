# import pandas as pd
#
# """
#    Создайте функцию create_companyDF(income, expenses, years), которая  возвращает DataFrame,
#    составленный из входных данных со столбцами “Income” и “Expenses” и индексами, соответствующим годам рассматриваемого периода.
#    """
# def create_companyDF(income, expenses, years):
#     df = pd.DataFrame({
#         'Income': income,
#         'Expenses': expenses
#         },
#         index = years
#     )
#     return df
#
# """
#     А также напишите функцию get_profit(df, year), которая возвращает разницу между доходом и расходом, записанных в таблице df, за год year.
#     Учтите, что если информация за запрашиваемый год не указана в вашей таблице вам необходимо вернуть None.
#     """
# def get_profit(df, year):
#     if year in df.index:
#         profit = df.loc[year, 'Income'] - df.loc[year, 'Expenses']
#     else:
#         profit=None
#     return profit
#
#
# if __name__ == '__main__':
#     expenses = [156, 130, 270]
#     income = [478, 512, 196]
#     years = [2018, 2019, 2020]
#
#     scienceyou = create_companyDF(income, expenses, years)
#     print(get_profit(scienceyou, 2020))  # -74

import pandas as pd

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

countires_data = pd.read_csv('C:/Users/nick-/Documents/Python Scripts/countries.csv', sep=';')
print(countires_data)