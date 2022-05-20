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

# print(deals_reformat.head())


# dict = {}
# for i in list(deals_reformat.columns):
#     dict[i] = deals_reformat[i].value_counts().shape[0]
#
# print(pd.DataFrame(dict, index=["unique count"]).transpose())


'''форматируем датасет'''
list_was_success = ['Downpayment made (upfront)', 'Downpayment made', 'Internal EMI in progress', 'Closed Won']
deals_reformat['success'] = deals_reformat['Stage'].apply(lambda x: 1 if x in list_was_success else 0)


'''обрабатываем goal_for_study'''
goal_for_study = deals_reformat.groupby(by=['Goal for study'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
goal_for_study['proportion'] = round(goal_for_study['sum'] / goal_for_study['count']*100,1)
goal_for_study = goal_for_study.sort_values(by='sum', ascending=False)
# print(goal_for_study)
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


sns.set(style="darkgrid")

# Set the figure size
plt.figure(figsize=(12, 7))

goal_for_study_plt = goal_for_study.loc[goal_for_study['sum']>5].sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Goal for study',
    data=goal_for_study_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Goal for study" conversion to success, %', size=20)




'''обрабатываем Lead quality'''
lead_qual = deals_reformat.groupby(by=['Lead quality'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
lead_qual['proportion'] = round(lead_qual['sum'] / lead_qual['count']*100,1)
lead_qual = lead_qual.sort_values(by='sum', ascending=False)
# print(lead_qual)


# Set the figure size
plt.figure(figsize=(12, 7))

lead_qual_plt = lead_qual.sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Lead quality',
    data=lead_qual_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Lead Quality" conversion to success, %', size=20)



''' обрабатываем Current salary'''
salary_category_dict = {'0': 'low', '2': 'low', '3-4': 'low', '5-6': 'high', '7-8': 'high', '8+': 'high'}
deals_reformat_upd1 = deals_reformat.replace({"Current salary": salary_category_dict})
cur_salary = deals_reformat_upd1.groupby(by=['Current salary'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
cur_salary['proportion'] = round(cur_salary['sum'] / cur_salary['count']*100,1)
cur_salary = cur_salary.sort_values(by='sum', ascending=False)
# salary_category_dict = {'0': 'low', '2': 'low', '3-4': 'low', '5-6': 'high', '7-8': 'high', '8+': 'high'}
# cur_salary = cur_salary.replace({"Current salary": salary_category_dict})
# print(cur_salary)

plt.figure(figsize=(12, 7))

cur_salary_plt = cur_salary.loc[cur_salary["Current salary"] != 'Dont know'].sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Current salary',
    data=cur_salary_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Current salary" conversion to success, %', size=20)


''' обрабатываем Work Experience'''
work_exp_dict = {'No experience': 'no', '1': 'low', '2-3': 'low', '4-5': 'high', '6-7': 'high', '8+': 'high'}
deals_reformat_upd1 = deals_reformat.replace({"Work experience": work_exp_dict})
work_exp = deals_reformat_upd1.groupby(by=['Work experience'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
work_exp['proportion'] = round(work_exp['sum'] / work_exp['count']*100,1)
work_exp = work_exp.sort_values(by='sum', ascending=False)
# print(work_exp)

plt.figure(figsize=(12, 7))

work_exp_plt = work_exp.loc[work_exp["Work experience"] != 'Dont know'].sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Work experience',
    data=work_exp_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Work experience" conversion to success, %', size=20)


''' обрабатываем Education'''
education = deals_reformat.groupby(by=['Education'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
education['proportion'] = round(education['sum'] / education['count']*100,1)
education = education.sort_values(by='sum', ascending=False)
# print(education)

plt.figure(figsize=(12, 7))

education_plt = education.loc[education['sum']>5].sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Education',
    data=education_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Education" conversion to success, %', size=20)


''' обрабатываем Education'''
employment_status = deals_reformat.groupby(by=['Employment status'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
employment_status['proportion'] = round(employment_status['sum'] / employment_status['count']*100,1)
employment_status = employment_status.sort_values(by='sum', ascending=False)
# print(employment_status)


plt.figure(figsize=(12, 7))

employment_status_plt = employment_status.loc[employment_status['sum']>5].sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Employment status',
    data=employment_status_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Employment status" conversion to success, %', size=20)
# plt.show()


''' обрабатываем Online education experience'''
online_ed_exp = deals_reformat.groupby(by=['Online education experience'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
online_ed_exp['proportion'] = round(online_ed_exp['sum'] / online_ed_exp['count']*100,1)
online_ed_exp = online_ed_exp.sort_values(by='sum', ascending=False)
# print(online_ed_exp)


plt.figure(figsize=(12, 7))

online_ed_exp_plt = online_ed_exp.loc[online_ed_exp['sum']>5].sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Online education experience',
    data=online_ed_exp_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Online education experience" conversion to success, %', size=20)



''' обрабатываем Category'''
category = deals_reformat.groupby(by=['Category'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
category['proportion'] = round(category['sum'] / category['count']*100,1)
category = category.sort_values(by='sum', ascending=False)
# print(category)


plt.figure(figsize=(12, 7))

category_plt = category.loc[category['sum']>5].sort_values(by='proportion', ascending=False)

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Category',
    data=category_plt,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Category" conversion to success, %', size=20)
# plt.show()


'''строим общий рисунок'''
# sns.set(style="darkgrid")
#
# fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(14, 8),
#                        gridspec_kw={
#                             'width_ratios': [1, 1, 1],
#                            'wspace': 0.4}
#                        )
#
# # goal for study
# goal_for_study_plt = goal_for_study.loc[goal_for_study['sum']>5].sort_values(by='proportion', ascending=False)
#
# ax[0] = sns.barplot(
#     x="proportion",
#     y='Goal for study',
#     ax=ax[0],
#     data=goal_for_study_plt,
#     estimator=sum,
#     ci=None,
#     color='#69b3a2')
#
# # lead quality
# lead_qual_plt = lead_qual.sort_values(by='proportion', ascending=False)
#
# ax[1] = sns.barplot(
#     x="proportion",
#     y='Lead quality',
#     ax=ax[1],
#     data=lead_qual_plt,
#     estimator=sum,
#     ci=None,
#     color='#69b3a2')
#
# # current salary
# cur_salary_plt = cur_salary.loc[cur_salary["Current salary"] != 'Dont know'].sort_values(by='proportion', ascending=False)
#
# ax[2] = sns.barplot(
#     x="proportion",
#     y='Current salary',
#     ax=ax[2],
#     data=cur_salary_plt,
#     estimator=sum,
#     ci=None,
#     color='#69b3a2')
#
# # work experience
# work_exp_plt = work_exp.loc[work_exp["Work experience"] != 'Dont know'].sort_values(by='proportion', ascending=False)
#
# # plot a bar chart
# # ax[3] = sns.barplot(
# #     x="proportion",
# #     y='Work experience',
# #     ax=ax[3],
# #     data=work_exp_plt,
# #     estimator=sum,
# #     ci=None,
# #     color='#69b3a2')
#
# ax[0].set_title('"Goal for study" conversion to success, %', size=14)
# ax[1].set_title('"Lead Quality" conversion to success, %', size=14)
# ax[2].set_title('"Current salary" conversion to success, %', size=14)
# # ax[3].set_title('"Work experience" conversion to success, %', size=14)
#
# plt.show()



'''дальнейшие шаги исследования'''
# сделать тесты для пропорций, где можно
# собрать данные по полу
# собрать данные по взаимодействию признаков
# подгрузить даты создания лида и собрать новые признаки - конверсии по созданию лида в течение дня, в течение недели
