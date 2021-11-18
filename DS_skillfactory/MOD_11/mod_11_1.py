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
# print(melb_df.info())

#функция для удаления столбцов из df
# def delete_columns(df, col=[]):
#     for cc in col:
#         if cc not in df.columns:
#             return None
#     return df.drop(col, axis=1)


countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})
countries_df['density'] = countries_df['population']*1000000/countries_df['square']
print(countries_df['density'].mean())

