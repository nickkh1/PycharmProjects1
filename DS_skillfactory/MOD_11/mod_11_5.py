import pandas as pd

data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/citibike-tripdata.csv', sep=',')

data.drop(['start station id', 'end station id'], axis = 1, inplace=True)

data['age'] = 2018 - data['birth year']
data.drop(['birth year'], axis=1, inplace=True)
print(data[data['age'] > 60].shape[0])

data['starttime'] = pd.to_datetime(data['starttime'])
data['stoptime'] = pd.to_datetime(data['stoptime'])
data['trip duration'] = (data['stoptime'] - data['starttime']).dt.seconds
print(round(data['trip duration'].mean(), 2))

weekday = data['starttime'].dt.dayofweek
data['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
print(data['weekend'].sum())


def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
    else:
        return 'else'
data['time_of_day'] = data['starttime'].dt.hour.apply(get_time_of_day)
a = data[data['time_of_day'] == 'day'].shape[0]
b = data[data['time_of_day'] == 'night'].shape[0]
print(round(a / b))