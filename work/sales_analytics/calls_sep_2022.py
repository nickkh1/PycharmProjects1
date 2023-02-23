import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)


df = pd.read_csv('C:/Users/nick-/Desktop/CI/4.Analytics section/Leads_and_deals/Phone_Call_Metrics_By_Users.csv', sep=',')

print(df.info())