import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)


df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/'
                 '52b2aab9-8fa7-4afb-910e-7e3eaf119942.csv', sep=',')

print(df.info())
print(df.head())