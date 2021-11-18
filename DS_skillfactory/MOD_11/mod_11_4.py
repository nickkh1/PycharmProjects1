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
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]


def get_street_type(address):
# Создаём список географических пометок exclude_list.
    exclude_list = ['N', 'S', 'W', 'E']
# Метод split() разбивает строку на слова по пробелу.
# В результате получаем список слов в строке и заносим его в переменную address_list.
    address_list = address.split(' ')
# Обрезаем список, оставляя в нём только последний элемент,
# потенциальный подтип улицы, и заносим в переменную street_type.
    street_type = address_list[-1]
# Делаем проверку на то, что полученный подтип является географической пометкой.
# Для этого проверяем его на наличие в списке exclude_list.
    if street_type in exclude_list:
# Если переменная street_type является географической пометкой,
# переопределяем её на второй элемент с конца списка address_list.
        street_type = address_list[-2]
# Возвращаем переменную street_type, в которой хранится подтип улицы.
    return street_type

street_types = melb_df['Address'].apply(get_street_type)
popular_stypes =street_types.value_counts().nlargest(10).index
melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
melb_df = melb_df.drop('Address', axis=1)


def get_weekend(weekday):
    weekend_list = [5,6]

    if weekday in weekend_list:
        return 1
    else:
        return 0

melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)

popular_seler = melb_df['SellerG'].value_counts().nlargest(49).index
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_seler else 'other')
# a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()
# b = melb_df[melb_df['SellerG'] == 'other']['Price'].min()
# print(a/b)

# создаём пустой список
unique_list = []
# пробегаемся по именам столбцов в таблице
for col in melb_df.columns:
    # создаём кортеж (имя столбца, число уникальных значений)
    item = (col, melb_df[col].nunique(),melb_df[col].dtype)
    # добавляем кортеж в список
    unique_list.append(item)
# создаём вспомогательную таблицу и сортируем её
unique_counts = pd.DataFrame(
    unique_list,
    columns=['Column_Name', 'Num_Unique', 'Type']
).sort_values(by='Num_Unique',  ignore_index=True)
# выводим её на экран

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in melb_df.columns: # цикл по именам столбцов
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df[col] = melb_df[col].astype('category') # преобразуем тип столбца

# print(melb_df['Regionname'].cat.categories)
# print(melb_df['Regionname'].cat.codes)

popular_suburbs =melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in popular_suburbs else 'other')
print(melb_df.info())

