import pandas as pd

# index — номер строки
# Suburb — наименование пригорода
# Address — адрес
# Rooms — количество комнат в помещении
# Type — тип здания (h — дом, коттедж, вилла, терраса; u — блочный, дуплексный дом; t — таунхаус)
# Price — цена помещения
# Method — метод продажи
# SellerG — риэлторская компания
# Date — дата продажи (в формате день/месяц/год)
# Distance — расстояния до объекта от центра Мельбурна
# Postcode — почтовый индекс
# Bedroom — количество спален
# Bathroom — количество ванных комнат
# Car — количество парковочных мест
# Landsize — площадь прилегающей территории
# BuildingArea — площадь здания
# YearBuilt — год постройки
# CouncilArea — региональное управление
# Lattitude — географическая широта
# Longitude — географическая долгота
# Regionname — наименование района Мельбурна
# Propertycount — количество объектов недвижимости в районе
# Coordinates — широта и долгота, объединённые в кортеж
melb_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/melb_data.csv', sep=',')

# print(round(melb_data.loc[3521, 'Landsize'] / melb_data.loc[1690, 'Landsize']))

# print(melb_data.head(10))
# print(melb_data.shape)

melb_data['Postcode'] = melb_data['Postcode'].astype('int64')
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
# print(melb_data.describe().loc[:, ['Distance', 'BuildingArea' , 'Price']])
'''
На самом деле метод describe() можно применять не только к числовым признакам. 
С помощью параметра include можно указать тип данных, для которого нужно вывести описательную информацию.'''
print(melb_data.describe(include=['object']))
print(melb_data['Type'].value_counts())

# print(melb_data.describe().loc[:, ['CouncilArea']])
print(melb_data.info())
print(melb_data.describe().loc[:, ['Distance', 'BuildingArea' , 'Price']])
print(melb_data['Regionname'].value_counts(normalize=True))
print(melb_data['Type'].value_counts(normalize=True))