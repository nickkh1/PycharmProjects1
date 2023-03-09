import os
import pandas as pd

print(os.getcwd())
os.chdir('C:/Users/nick-/Desktop/TG_test/SH')
print(os.getcwd())
# print(os.path.splitext(os.getcwd())[0])

'выбираем файл'
dirName = 'C:/Users/nick-/Desktop/TG_test/SH'
listOfFiles = list()
for(dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

print(len(listOfFiles))
# for elem in listOfFiles:
#     print(elem)
shortlist = listOfFiles.copy()
# print(shortlist)


for each in shortlist:
    # df = pd.read_excel(each)
    test_string = each
    test_string = test_string.rstrip('.xlsx')
    test_string = test_string.lstrip(r'C:\Users\nick-\Desktop\TG_test\SH\Отчет ')
    print(test_string)

# # df = pd.read_excel('C:/Users/nick-/Desktop/TG_test/SH/Отчет Аксессуар для рукоделия.xlsx')
# folder = r'C:/Users/nick-/Desktop/TG_test/SH'
# #папка с файлами
# files = [os.path.join(folder, f) for f in folder] #формируем список путей к файлам
# all_file_frames = []
# print(all_file_frames[0:2])
#
#
#
#
#
#
#
# '''работаем с репортом по товару'''
# df = pd.read_excel('C:/Users/nick-/Desktop/TG_test/SH/Отчет Аксессуар для рукоделия.xlsx')
# df = df.dropna(subset=['Отзывы'])
# df['Отзывы'] = df['Отзывы'].astype(int)
# niche_name = 'Аксессуар для рукоделия'