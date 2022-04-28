import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)


iris = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/iris.csv', sep=',')
# print(iris.head())
# sns.heatmap(iris.corr(), annot=True)
# plt.show()

iris = iris.drop(['petal.width'], axis=1)
iris = iris.drop(['petal.length'], axis=1)
print(iris.head())