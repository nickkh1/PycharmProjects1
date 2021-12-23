import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

diabetes = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/diabetes_data.csv', sep=',')
# print(f'Изначальный шэйп: {diabetes.shape}')
# print(diabetes.info())
# diabetes_yes = diabetes[diabetes['Outcome']== 1]
# diabetes_no = diabetes[diabetes['Outcome'] == 0]
# print(diabetes_yes.describe())
# print(diabetes_no.describe())

diabetes_col = list(diabetes.columns)

diabetes_duppled = diabetes.drop_duplicates(subset=diabetes_col)
# print(f'Стало строк после удаление дупликадов: {diabetes_duppled.shape[0]}')

low_information_cols = []

#цикл по всем столбцам
for col in diabetes_duppled.columns:
    #наибольшая относительная частота в признаке
    top_freq = diabetes_duppled[col].value_counts(normalize=True).max()
    #доля уникальных значений от размера признака
    nunique_ratio = diabetes_duppled[col].nunique() / diabetes_duppled[col].count()
    # сравниваем наибольшую частоту с порогом
    if top_freq > 0.99:
        low_information_cols.append(col)
        # print(f'{col}: {round(top_freq*100, 2)}% одинаковых значений')
    # сравниваем долю уникальных значений с порогом
    if nunique_ratio > 0.99:
        low_information_cols.append(col)
        # print(f'{col}: {round(nunique_ratio*100, 2)}% уникальных значений')

information_diabetes = diabetes_duppled.drop(low_information_cols, axis=1)
# print(f'Результирующий шейп: {information_diabetes.shape}')


# col_list_diabetes = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
# col_data = information_diabetes[col_list]
# print(col_data.head())

# def remove_zero_indata(data, col_list):
#     for col in data[col_list].columns:
#         x_series = data[col]
#         for i in x_series:
#             if i == 0:
#                 i = np.nan
#     return data

def remove_zeroo(i):
    if i == 0:
        return np.nan
    else:
        return i

information_diabetes['Glucose'] = information_diabetes['Glucose'].apply(remove_zeroo)
information_diabetes['BloodPressure'] = information_diabetes['BloodPressure'].apply(remove_zeroo)
information_diabetes['SkinThickness'] = information_diabetes['SkinThickness'].apply(remove_zeroo)
information_diabetes['Insulin'] = information_diabetes['Insulin'].apply(remove_zeroo)
information_diabetes['BMI'] = information_diabetes['BMI'].apply(remove_zeroo)
# print(np.count_nonzero(np.isnan(information_diabetes['Insulin']))/information_diabetes['Insulin'].count())
# print(information_diabetes.isnull().mean().round(2).sort_values(ascending=False))

dupp_diab = information_diabetes
too_low_information_cols = []

#цикл по всем столбцам
for col in dupp_diab.columns:
    #наибольшая относительная частота в признаке
    top_nan = dupp_diab[col].isnull().mean().round(2)
    if top_nan > 0.3:
        too_low_information_cols.append(col)
        # print(f'{col}: {round(top_nan*100, 2)}%')

new_information_diabetes = dupp_diab.drop(too_low_information_cols, axis=1)

thresh = new_information_diabetes.shape[1]-2
drop_data = new_information_diabetes.dropna(how='any', thresh=thresh, axis=0)

#заполняем пропуски в остальных ячейках
fill_data = drop_data.copy()
#создаем словарь имя столбца: число(признак) на который надо заменить пропуски
values = {
    'Pregnancies': fill_data['Pregnancies'].median(),
    'Glucose': fill_data['Glucose'].median(),
    'BloodPressure': fill_data['BloodPressure'].median(),
    'SkinThickness': fill_data['SkinThickness'].median(),
    'BMI': fill_data['BMI'].median(),
    'DiabetesPedigreeFunction': fill_data['DiabetesPedigreeFunction'].median(),
    'Age': fill_data['Age'].median(),
    'Outcome': fill_data['Outcome'].median()
}
#заполняем пропуски в соответствии с заявленным словарем
fill_data = fill_data.fillna(values)



# def outliers_z_score_mod(data, feature, log_scale=False, left = 3, right = 3):
#     if log_scale:
#         x = np.log(data[feature]+1)
#     else:
#         x = data[feature]
#     mu = x.mean()
#     sigma = x.std()
#     lower_bound = mu - left * sigma
#     upper_bound = mu + right * sigma
#     outliers = data[(x < lower_bound) | (x > upper_bound)]
#     cleaned = data[(x > lower_bound) & (x < upper_bound)]
#     return outliers, cleaned
#
# outliers, cleaned = outliers_z_score_mod(fill_data, 'SkinThickness')
# print(f'Число выбросов по методу z-отклонения: {outliers.shape[0]}')


def outliers_iqr_mod(data, feature, log_scale=False, left=1.5, right=1.5):
    if log_scale:
        x = np.log(data[feature])
    else:
        x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x<lower_bound) | (x > upper_bound)]
    cleaned = data[(x>lower_bound) & (x < upper_bound)]
    return outliers, cleaned


outliers, cleaned = outliers_iqr_mod(fill_data, 'DiabetesPedigreeFunction', log_scale=True)
print(f'Число выбросов по методу Тьюки: {outliers.shape[0]}')


