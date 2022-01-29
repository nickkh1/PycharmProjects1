import pandas as pd

# grades = pd.read_excel('C:/Users/nick-/Documents/DS/projects/SF_tasks/grades.xlsx')
# grades = pd.read_excel('C:/Users/nick-/Documents/DS/projects/SF_tasks/grades.xlsx', sheet_name='Maths')
# print(grades.head())
# grades.to_excel()
# data = pd.read_excel('https://github.com/asaydn/test/raw/master/january.xlsx')
# print(data)


# запись эксель
# grades.to_excel('data/grades_new.xlsx', sheet_name='Example',
#                 index=False)  # Сохраняем данные из DataFrame grades в файл grades_new.xlsx (на листе 'Example') в папке data

ratings = pd.read_excel('C:/Users/nick-/Documents/DS/projects/SF_tasks/ratings+movies.xlsx', sheet_name='ratings')
movies = pd.read_excel('C:/Users/nick-/Documents/DS/projects/SF_tasks/ratings+movies.xlsx', sheet_name='movies')

# print(ratings.info(), movies.info())
merged = ratings.merge(
    movies,
    on='movieId',
    how='left'
)

print(merged.shape[0])
