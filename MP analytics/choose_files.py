import os

'выбираем файл'
dirName = 'C:/Users/nick-/Desktop/TG_test'
listOfFiles = list()
for(dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
for elem in listOfFiles:
    print(elem)