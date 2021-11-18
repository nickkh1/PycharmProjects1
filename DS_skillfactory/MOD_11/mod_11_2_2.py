import pandas as pd

ufo_df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')
ufo_df['Time'] = pd.to_datetime(ufo_df['Time'])
# ufo_year = ufo_df['Time'].dt.year
# print(ufo_year.mode())

ufo_df['Date'] = ufo_df['Time'].dt.date
print(ufo_df[ufo_df['State']=='NV']['Date'].diff().dt.days.mean())