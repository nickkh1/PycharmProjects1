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


# print(deals_reformat.info())
# print(deals_reformat['Online education experience'].value_counts())
# print(deals_reformat['Education'].value_counts())
# print(deals_reformat['Employment status'].value_counts())
# print(deals_reformat['Current salary'].value_counts())
# print(deals_reformat['Category'].value_counts())
# print(deals_reformat['Goal for study'].value_counts())
# print(deals_reformat['Lead quality'].value_counts())
# print(deals_reformat['Work experience'].value_counts())
# print(deals_reformat['Stage'].value_counts())

list_was_success = ['Downpayment made (upfront)', 'Downpayment made', 'Internal EMI in progress', 'Closed Won']
deals_reformat['success'] = deals_reformat['Stage'].apply(lambda x: 1 if x in list_was_success else 0)

goal_for_study = deals_reformat.groupby(by=['Goal for study'], as_index=False)['success'].agg(['sum', 'count']).reset_index()
goal_for_study['proportion'] = round(goal_for_study['sum'] / goal_for_study['count']*100,1)
goal_for_study = goal_for_study.loc[goal_for_study['sum']>5].sort_values(by='proportion', ascending=False)
print(goal_for_study)
# если добавить тех, кто сделал рефанд в list_was_sucess - результаты распределены примерно так же, только выше пропорции

'''строим график'''
sns.set(style="darkgrid")

# Set the figure size
plt.figure(figsize=(12, 7))

# plot a bar chart
ax = sns.barplot(
    x="proportion",
    y='Goal for study',
    data=goal_for_study,
    estimator=sum,
    ci=None,
    color='#69b3a2')

ax.set_title('"Goal for study" conversion to success, %', size=20)

plt.show()



