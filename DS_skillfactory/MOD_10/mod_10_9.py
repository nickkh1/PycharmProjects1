import pandas as pd
#  0   gender                       1000 non-null   object
#  1   race/ethnicity               1000 non-null   object
#  2   parental level of education  1000 non-null   object
#  3   lunch                        1000 non-null   object
#  4   test preparation course      1000 non-null   object
#  5   math score                   1000 non-null   int64
#  6   reading score                1000 non-null   int64
#  7   writing score
student_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/students_performance.csv', sep=',')
# print(student_data.info())
#
# print(student_data.describe())
# print(student_data.describe(include=object))
#
# print(student_data.loc[155,'writing score'])

# print(student_data['math score'].mean())
# print(student_data['race/ethnicity'].value_counts())
# print(student_data['test preparation course'].head(15))
# print(round(student_data[student_data['test preparation course'] == 'completed']['reading score'].mean()))
# print(student_data[student_data['math score'] == 0].shape[0])
# print(student_data[student_data['lunch'] == 'standard']['math score'].mean())
# print(student_data[student_data['lunch'] == 'free/reduced']['math score'].mean())

# print(student_data['parental level of education'].value_counts(normalize=True))
# print(student_data['race/ethnicity'].value_counts())
print(student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()-student_data[student_data['race/ethnicity'] == 'group C']['writing score'].mean())
