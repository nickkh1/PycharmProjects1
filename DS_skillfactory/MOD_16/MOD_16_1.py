import pandas as pd # Импорт библиотеки pandas — при выполнении последовательно всех примеров ниже, импорт библиотеки pandas выполняется один раз
#
# countries_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/countries.csv', sep=';') # Загружаем данные из файла в переменную, создавая объект DataFrame
# countries_data.to_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/countries.txt', index=False, sep=' ') # Выгружаем данные из DataFrame в CSV-файл и сохраняем файл в папке data
#
# txt_df = pd.read_table('C:/Users/nick-/Documents/DS/projects/SF_tasks/countries.txt', sep=' ', index_col=['country'])# Загружаем данные из файла в переменную, создавая объект DataFrame
# print(txt_df)


# data=pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ErrorEnCoding.csv', header=None)
# print(data)

# from chardet.universaldetector import UniversalDetector # Импортируем субмодуль chardet.universaldetector
# detector = UniversalDetector()
# with open('C:/Users/nick-/Documents/DS/projects/SF_tasks/ErrorEnCoding.csv', 'rb') as fh:
#     for line in fh:
#         detector.feed(line)
#         if detector.done:
#             break
# detector.close()



