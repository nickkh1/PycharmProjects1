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

melb_data['Postcode'] = melb_data['Postcode'].astype('int64')
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')


# mask = melb_data['Price'] > 2000000
# print(mask)
# print(melb_data[mask].head())
# print(melb_data[melb_data['Rooms'] == 3].shape[0])

# нас будут интересовать дома с ценой менее 300 тысяч, у которых либо число комнат равно 3
# либо площадь домов более 100 квадратных метров
# print(melb_data[((melb_data['Rooms'] == 3) | (melb_data['BuildingArea'] > 100)) & (melb_data['Price'] < 300000)].shape[0])

# А теперь более сложный трюк: найдём медианную площадь здания у объектов, чья цена выше средней.
# Для того чтобы оградить наш код от нагромождений, предварительно создадим переменную со средней ценой:
# mean_price = melb_data['Price'].mean()
# print(melb_data[melb_data['Price'] > mean_price]['BuildingArea'].median())

# print(melb_data[melb_data['Bathroom'] == 0].shape[0])
# print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3000000)].shape[0])
# print(melb_data[melb_data['BuildingArea'] == 0]['Price'].min())

melb_data_2 = melb_data[melb_data['Price']<1000000]
print(round(melb_data_2[(melb_data_2['Rooms'] > 5) | (melb_data_2['YearBuilt'] > 2015)]['Price'].mean()))

print(melb_data[(melb_data['Price'] < 3000000) & (melb_data['Type'] == 'h')]['Regionname'].mode())