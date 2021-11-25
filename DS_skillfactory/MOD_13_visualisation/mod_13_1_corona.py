import pandas as pd
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
# print('Число строк: ', covid_df.shape[0])
# print('Число столбцов: ', covid_df.shape[1])

covid_df['death_rate'] = covid_df['deaths']/covid_df['confirmed'] * 100
covid_df['recovery_rate'] = covid_df['recovered']/covid_df['confirmed'] * 100
print(round(covid_df[covid_df['country'] == 'United States']['death_rate'].max(),2))
print(round(covid_df[covid_df['country'] == 'Russia']['recovery_rate'].mean(),2))