import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)


sample_a = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ab_test-redesign_sample_a.csv', sep=',')
sample_b = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/ab_test-redesign_sample_b.csv', sep=',')

print(sample_a.head())