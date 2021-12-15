import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

sber_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/sber_data.csv', sep=',')


# fig = plt.figure(figsize=(10, 7))
# boxplot = sns.boxplot(
#     data=sber_data,
#     y='price_doc',
#     x='ecology',
#     width=0.9
#

# fig = plt.figure(figsize=(10, 7))
# sns.scatterplot(data=sber_data, y='price_doc', x='kremlin_km');
# plt.show()

cols_null_percent = sber_data.isnull().mean() * 100
cols_with_null = cols_null_percent[cols_null_percent>0].sort_values(ascending=False)
print(cols_with_null)

colors = ['blue', 'yellow']
fig = plt.figure(figsize=(10, 7))
cols = cols_with_null.index
ax = sns.heatmap(
    sber_data[cols].isnull(),
    cmap=sns.color_palette(colors),
)
plt.show()