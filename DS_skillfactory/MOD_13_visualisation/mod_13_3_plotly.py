import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px

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
covid_df['death_rate'] = covid_df['deaths'] / covid_df['confirmed'] * 100
covid_df['recover_rate'] = covid_df['recovered'] / covid_df['confirmed'] * 100


# countries = ['Russia', 'Australia', 'Germany', 'Canada', 'United Kingdom']
# croped_covid_df = covid_df[covid_df['country'].isin(countries)]
#
# populations = pd.DataFrame([
#     ['Canada', 37664517],
#     ['Germany', 83721496],
#     ['Russia', 145975300],
#     ['Australia', 25726900],
#     ['United Kingdom', 67802690]
#     ],
#     columns=['country', 'population']
# )
# croped_covid_df = croped_covid_df.merge(populations, on=['country'])
# croped_covid_df['daily_confirmed_per_hundred'] = croped_covid_df['daily_confirmed'] / croped_covid_df['population'] * 100
#
# croped_covid_df['death_rate'] = croped_covid_df['deaths'] / croped_covid_df['confirmed'] * 100
# croped_covid_df['recover_rate'] = croped_covid_df['recovered'] / croped_covid_df['confirmed'] * 100


# строим линейный график
# line_data = covid_df.groupby('date', as_index=False).sum()
# print(line_data.head())
# fig = px.line(
#     data_frame=line_data, #DataFrame
#     x='date', #ось абсцисс
#     y=['confirmed', 'recovered', 'deaths', 'active'], #ось ординат
#     height=500, #высота
#     width=1000, #ширина
#     title='Confirmed, Recovered, Deaths, Active cases over Time' #заголовок
# )
# fig.show()



# #считаем средний процент выздоровлений для каждой страны
# bar_data = covid_df.groupby(
#     by='country',
#     as_index=False
# )[['recover_rate']].mean().nlargest(10, columns=['recover_rate'])
#
# #строим график
# fig = px.bar(
#     data_frame=bar_data, #DataFrame
#     x="country", #ось x
#     y="recover_rate", #ось y
#     color='country', #расцветка в зависимости от страны
#     text = 'recover_rate', #текст на столбцах
#     orientation='v', #ориентация графика
#     height=500, #высота
#     width=1000, #ширина
#     title='Top 10 Countries for Recovery Rate' #заголовок
# )
#
# #отображаем график
# fig.show()



# #считаем среднее ежедневно фиксируемое количество выздоровевших по странам
# treemap_data = covid_df.groupby(
#     by='country',
#     as_index=False
# )[['daily_recovered']].mean()
#
# #строим график
# fig = px.treemap(
#     data_frame=treemap_data, #DataFrame
#     path=['country'], #категориальный признак, для которого строится график
#     values='daily_recovered', #параметр, который сравнивается
#     height=500, #высота
#     width=1000, #ширина
#     title='Daily Recovered Cases by Country' #заголовок
# )
#
# #отображаем график
# fig.show()


# #преобразуем даты в строковый формат
# choropleth_data = covid_df.sort_values(by='date')
# choropleth_data['date'] = choropleth_data['date'].astype('string')
#
# #строим график
# fig = px.choropleth(
#     data_frame=choropleth_data, #DataFrame
#     locations="country", #столбец с локациями
#     locationmode = "country names", #режим сопоставления локаций с базой Plotly
#     color="confirmed", #от чего зависит цвет
#     animation_frame="date", #анимационный бегунок
#     range_color=[0, 30e6], #диапазон цвета
#     title='Global Spread of COVID-19', #заголовок
#     width=800, #ширина
#     height=500, #высота
#     color_continuous_scale='Reds' #палитра цветов
# )
#
# #отображаем график
# fig.show()



# #фильтруем таблицу по странам
# countries=['United States', 'Russia', 'United Kingdom', 'Brazil', 'France']
# scatter_data = covid_df[covid_df['country'].isin(countries)]
#
# #строим график
# fig = px.scatter_3d(
#     data_frame=scatter_data, #DataFrame
#     x = 'daily_confirmed', #ось абсцисс
#     y = 'daily_deaths', #ось ординат
#     z = 'daily_vaccinations', #ось аппликат
#     color='country', #расцветка в зависимости от страны
#     log_x=True,
#     log_y=True,
#     width=1000,
#     height=700
# )
#
# #отображаем график
# fig.show()
# # fig.write_html("plotly/scatter_3d.html")



# line_data = covid_df.groupby('date', as_index=False).sum()
# fig = px.line(
#     data_frame=line_data, #DataFrame
#     x='date', #ось абсцисс
#     y='daily_vaccinations', #ось ординат
#     height=500, #высота
#     width=1000, #ширина
#     title='Daily vaccination' #заголовок
# )
# fig.show()

choropleth_data = covid_df.sort_values(by='date')
choropleth_data['date'] = choropleth_data['date'].astype('string')
fig = px.choropleth(
    data_frame=choropleth_data, #DataFrame
    locations="country", #столбец с локациями
    locationmode = "country names", #режим сопоставления локаций с базой Plotly
    color="total_vaccinations", #от чего зависит цвет
    animation_frame="date", #анимационный бегунок
    range_color=[0, 30e6], #диапазон цвета
    title='Global Spread of COVID-19', #заголовок
    width=800, #ширина
    height=500, #высота
    color_continuous_scale='Reds' #палитра цветов
)

#отображаем график
fig.show()