import pandas as pd
import re
pd.set_option('display.max_columns', None)

joined = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ratings_movies.csv', sep=',')

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg)
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None

print(joined.columns)

joined['year_release'] = joined['title'].apply(get_year_release)
# print(joined.info())

# mask = joined['year_release'] == 1999
# print(joined[mask].groupby('title')['rating'].mean().sort_values())

# mask = joined['year_release'] == 2010
# print(joined[mask].groupby('genres')['rating'].mean().sort_values())

# print(joined.groupby('userId')['genres'].nunique().sort_values(ascending=False))

# print(joined.groupby('userId')['rating'].agg(
#     ['count', 'mean']
# ).sort_values(['count', 'mean'], ascending=[True, False]))


# mask = joined['year_release'] == 2018
# grouped = joined[mask].groupby('genres')['rating'].agg(
#     ['mean', 'count']
# )
# print(grouped)
# print(grouped[grouped['count']>10].sort_values(
#     by=['mean', 'count'],
#     ascending=[False, False]
# ))


joined['date'] = pd.to_datetime(joined['date'])
joined['year_rating'] = joined['date'].dt.year
pivot = joined.pivot_table(
    index='year_rating',
    columns='genres',
    values='rating',
    aggfunc='mean'
)

pivot_1 = joined.pivot_table(
    index='genres',
    columns='year_rating',
    values='rating',
    aggfunc='mean'
)
print(pivot_1[2018].sort_values().head(30))