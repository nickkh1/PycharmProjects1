import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

covid_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/covid_data.csv', sep=',')

vaccinations_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/country_vaccinations.csv', sep=',')
vaccinations_data = vaccinations_data[
    ['country', 'date', 'total_vaccinations',
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]

covid_data = covid_data.groupby(
    ['date', 'country'],
    as_index=False
)[['confirmed', 'deaths', 'recovered']].sum()

covid_data['date'] = pd.to_datetime(covid_data['date'])

covid_data['active'] = covid_data['confirmed'] - covid_data['deaths'] - covid_data['recovered']

covid_data = covid_data.sort_values(by=['country', 'date'])
covid_data['daily_confirmed'] = covid_data.groupby('country')['confirmed'].diff()
covid_data['daily_deaths'] = covid_data.groupby('country')['deaths'].diff()
covid_data['daily_recovered'] = covid_data.groupby('country')['recovered'].diff()

vaccinations_data['date'] = pd.to_datetime(vaccinations_data['date'])

# print(covid_data['date'].min(), covid_data['date'].max())
# print(vaccinations_data['date'].min(), vaccinations_data['date'].max())

covid_df = covid_data.merge(vaccinations_data, on=['date', 'country'], how='left')

countries = ['Russia', 'Australia', 'Germany', 'Canada', 'United Kingdom']
croped_covid_df = covid_df[covid_df['country'].isin(countries)]

populations = pd.DataFrame([
    ['Canada', 37664517],
    ['Germany', 83721496],
    ['Russia', 145975300],
    ['Australia', 25726900],
    ['United Kingdom', 67802690]
    ],
    columns=['country', 'population']
)
croped_covid_df = croped_covid_df.merge(populations, on=['country'])
croped_covid_df['daily_confirmed_per_hundred'] = croped_covid_df['daily_confirmed'] / croped_covid_df['population'] * 100

croped_covid_df['death_rate'] = croped_covid_df['deaths'] / croped_covid_df['confirmed'] * 100
croped_covid_df['recover_rate'] = croped_covid_df['recovered'] / croped_covid_df['confirmed'] * 100



# Гистограмма
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
# sns.histplot(
#     data=croped_covid_df,
#     x='daily_confirmed_per_hundred',
#     bins=25,
#     kde=True,
#     ax=axes[0]
# );
# axes[0].set_title('Гистограмма ежедневной заболеваемости на 100 человек', fontsize=16)
# sns.histplot(
#     data=croped_covid_df,
#     x='daily_confirmed_per_hundred',
#     y='country',
#     bins=25,
#     color='red',
#     ax=axes[1]
# )

# boxplot
# fig = plt.figure(figsize=(10, 7))
# boxplot = sns.boxplot(
#     data=croped_covid_df,
#     y='country',
#     x='death_rate',
#     orient='h',
#     width=0.9
# )
# boxplot.set_title('Распределение летальности по странам');
# boxplot.set_xlabel('Летальность');
# boxplot.set_ylabel('Страна');
# boxplot.grid()

# # диаграмма
# fig = plt.figure(figsize=(10, 7))
# croped_covid_df['quarter'] = croped_covid_df['date'].dt.quarter
# barplot = sns.barplot(
#     data=croped_covid_df,
#     x='country',
#     y='daily_confirmed_per_hundred',
#     hue='quarter',
# )
# barplot.set_title('Средний процент болеющего населения по кварталам');

# # делаем joinplot
# jointplot = sns.jointplot(
#     data=croped_covid_df,
#     x='people_fully_vaccinated_per_hundred',
#     y='daily_confirmed_per_hundred',
#     hue='country',
#     xlim = (0, 40),
#     ylim = (0, 0.1),
#     height=8,
# )

#делаем тепловую карту
# pivot = croped_covid_df.pivot_table(
#     values='people_vaccinated_per_hundred',
#     columns='date',
#     index='country',
# )
# pivot.columns = pivot.columns.astype('string')
#
# fig = plt.figure(figsize=(12, 9))
# heatmap = sns.heatmap(data=pivot, cmap='YlGnBu')
# heatmap.set_title('Тепловая карта вакцинации', fontsize=16);


# для heatmap чаще всего нужен пивот тэйбл
# croped_covid_df['confirmed_per_hundred'] = croped_covid_df['confirmed'] / croped_covid_df['population'] *100
#
# fig = plt.figure(figsize=(12, 8))
# pivot = croped_covid_df.pivot_table(values='confirmed_per_hundred', columns='date', index='country')
# pivot.columns = pivot.columns.astype('string')
# heatmap = sns.heatmap(data=pivot, cmap='YlGnBu')



fig = plt.figure(figsize=(10, 7))
boxplot = sns.boxplot(
    data=croped_covid_df,
    y='country',
    x='recover_rate',
    orient='h',
    width=0.9
)
boxplot.set_title('Распределение летальности по странам');
boxplot.set_xlabel('Летальность');
boxplot.set_ylabel('Страна');
boxplot.grid()
plt.show()
