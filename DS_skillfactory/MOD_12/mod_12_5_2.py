import pandas as pd
import re

pd.set_option('display.max_columns', None)

orders = pd.read_excel('C:/Users/nick-/Documents/DS/projects/SF_tasks/orders.xlsx', sheet_name='orders', index_col=0)
products = pd.read_excel('C:/Users/nick-/Documents/DS/projects/SF_tasks/products.xlsx')

print(orders.info())
