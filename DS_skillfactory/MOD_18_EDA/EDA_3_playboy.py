import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

pd.set_option('display.max_columns', None)


df = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/model.csv', sep=',')

# print(df.describe())
# print(df.head())

# sns.heatmap(df.corr(), annot = True)
# plt.show()


# sns.scatterplot(data=df, x="Waist/Hip", y="Waist")
# plt.show()
#
# sns.scatterplot(data=df, x="Weight", y="Year")
# plt.show()

''' строим график попарных отношений'''
sns.pairplot(df)
plt.show()

# print(df.corr())

# print(df['Height'].mean())
# print(statistics.mean(df['Weight']))