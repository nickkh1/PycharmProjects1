import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/wine_cleared.csv', sep=',')
print(df.info())
print(df['price'].min())