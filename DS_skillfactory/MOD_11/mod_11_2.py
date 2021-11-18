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

melb_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)

total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
# print(total_rooms)

melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms

diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area

melb_df['Date'] = pd.to_datetime(melb_df['Date'])
# years_sold = melb_df['Date'].dt.year
# print(years_sold)
# print('Min year sold:', years_sold.min())
# print('Max year sold:', years_sold.max())
# print('Mode year sold:', years_sold.mode()[0])

# melb_df['MonthSale'] = melb_df['Date'].dt.month
# print(melb_df['MonthSale'].value_counts(normalize=True))

# про работу с интервалами и timedelta
# delta_days = melb_df['Date'] - pd.to_datetime('2016-01-01')
# print(delta_days)
# print(delta_days.dt.days)

# melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
# weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]
# print(weekend_count)


