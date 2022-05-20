import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)

deals_initial = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/for_Python/Student_analytics/Deals_17_15_22.csv', sep=',')
deals_reformat = deals_initial[['Id', 'Deal Owner Name', 'Created Time', 'Stage', 'Lead Source', 'Category',
                                'Current salary', 'Education', 'Employment status', 'Goal for study', 'Lead quality',
                                'Online education experience', 'Work experience']].\
                                dropna(subset=['Goal for study'])


# dict = {}
# for i in list(deals_reformat.columns):
#     dict[i] = deals_reformat[i].value_counts().shape[0]
#
# print(pd.DataFrame(dict, index=["unique count"]).transpose())



print(deals_reformat['Online education experience'].value_counts())
print(deals_reformat['Education'].value_counts())
print(deals_reformat['Employment status'].value_counts())
print(deals_reformat['Current salary'].value_counts())
print(deals_reformat['Category'].value_counts())
print(deals_reformat['Goal for study'].value_counts())
print(deals_reformat['Lead quality'].value_counts())
print(deals_reformat['Work experience'].value_counts())

'''форматируем датасет'''
list_was_success = ['Downpayment made (upfront)', 'Downpayment made', 'Internal EMI in progress', 'Closed Won']
deals_reformat['success'] = deals_reformat['Stage'].apply(lambda x: 1 if x in list_was_success else 0)

print(deals_reformat.info())

'''обрабатываем goal_for_study'''
goal_for_study = deals_reformat.groupby(by=['Goal for study'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
goal_for_study['proportion'] = round(goal_for_study['sum'] / goal_for_study['count']*100,1)
goal_for_study = goal_for_study.sort_values(by='sum', ascending=False)
print(goal_for_study)
# если добавить тех, кто сделал рефанд в list_was_sucess - результаты распределены примерно так же, только выше пропорции

# Функция для преобразования dataframe в Markdown Table
# def pandas_df_to_markdown_table(df):
#     from IPython.display import Markdown, display
#     fmt = ['---' for i in range(len(df.columns))]
#     df_fmt = pd.DataFrame([fmt], columns=df.columns)
#     df_formatted = pd.concat([df_fmt, df])
#     display(Markdown(df_formatted.to_csv(sep="|", index=False)))
#
# pandas_df_to_markdown_table(goal_for_study)


# sns.set(style="darkgrid")
#
# # Set the figure size
# plt.figure(figsize=(12, 7))
#
# goal_for_study_plt = goal_for_study.loc[goal_for_study['sum']>5].sort_values(by='proportion', ascending=False)
#
# # plot a bar chart
# ax = sns.barplot(
#     x="proportion",
#     y='Goal for study',
#     data=goal_for_study_plt,
#     estimator=sum,
#     ci=None,
#     color='#69b3a2')
#
# ax.set_title('"Goal for study" conversion to success, %', size=20)
#
# # plt.show()



'''обрабатываем Lead quality'''
lead_qual = deals_reformat.groupby(by=['Lead quality'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
lead_qual['proportion'] = round(lead_qual['sum'] / lead_qual['count']*100,1)
lead_qual = lead_qual.sort_values(by='sum', ascending=False)
print(lead_qual)


# # Set the figure size
# plt.figure(figsize=(12, 7))
#
# lead_qual_plt = lead_qual.sort_values(by='proportion', ascending=False)
#
# # plot a bar chart
# ax = sns.barplot(
#     x="proportion",
#     y='Lead quality',
#     data=lead_qual_plt,
#     estimator=sum,
#     ci=None,
#     color='#69b3a2')
#
# ax.set_title('"Lead Quality" conversion to success, %', size=20)
#
# plt.show()


''' обрабатываем Current salary'''
salary_category_dict = {'0': 'low', '2': 'low', '3-4': 'low', '5-6': 'high', '7-8': 'high', '8+': 'high'}
deals_reformat_upd1 = deals_reformat.replace({"Current salary": salary_category_dict})
cur_salary = deals_reformat_upd1.groupby(by=['Current salary'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
cur_salary['proportion'] = round(cur_salary['sum'] / cur_salary['count']*100,1)
cur_salary = cur_salary.sort_values(by='sum', ascending=False)
# salary_category_dict = {'0': 'low', '2': 'low', '3-4': 'low', '5-6': 'high', '7-8': 'high', '8+': 'high'}
# cur_salary = cur_salary.replace({"Current salary": salary_category_dict})
print(cur_salary)

# plt.figure(figsize=(12, 7))
#
# cur_salary_plt = cur_salary.loc[cur_salary["Current salary"] != 'Dont know'].sort_values(by='proportion', ascending=False)
#
# # plot a bar chart
# ax = sns.barplot(
#     x="proportion",
#     y='Current salary',
#     data=cur_salary_plt,
#     estimator=sum,
#     ci=None,
#     color='#69b3a2')
#
# plt.show()


''' обрабатываем Current salary'''


'''строим общий рисунок'''
sns.set(style="darkgrid")

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(14, 8),
                       gridspec_kw={
                            'width_ratios': [1, 1, 1],
                           'wspace': 0.4}
                       )

# goal for study
goal_for_study_plt = goal_for_study.loc[goal_for_study['sum']>5].sort_values(by='proportion', ascending=False)

ax[0] = sns.barplot(
    x="proportion",
    y='Goal for study',
    ax=ax[0],
    data=goal_for_study_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

# lead quality
lead_qual_plt = lead_qual.sort_values(by='proportion', ascending=False)

ax[1] = sns.barplot(
    x="proportion",
    y='Lead quality',
    ax=ax[1],
    data=lead_qual_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

# current salary
cur_salary_plt = cur_salary.loc[cur_salary["Current salary"] != 'Dont know'].sort_values(by='proportion', ascending=False)

ax[2] = sns.barplot(
    x="proportion",
    y='Current salary',
    ax=ax[2],
    data=cur_salary_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax[0].set_title('"Goal for study" conversion to success, %', size=14)
ax[1].set_title('"Lead Quality" conversion to success, %', size=14)
ax[2].set_title('"Current salary" conversion to success, %', size=14)

plt.show()



'''дальнейшие шаги исследования'''
# сделать тесты для пропорций, где можно
# собрать данные по полу
# собрать данные по взаимодействию признаков
# подгрузить даты создания лида и собрать новые признаки - конверсии по созданию лида в течение дня, в течение недели
