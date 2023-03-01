import matplotlib.pyplot as plt
import pandas as pd
import string
# from wordcloud import WordCloud
pd.set_option('display.max_columns', None)

df = pd.read_excel('C:/Users/nick-/Desktop/TG_test/2023-01-22—2023-02-20_Зоотовары_Для_собак_Корм_и_лакомства_лакомства.xlsx')
text = ' '.join(df['Товар'])
print(len(text))
print(text[:300])

text = text.lower()
print(string.punctuation)
# goods = df['Товар'].copy()
# goods = goods.astype('string')
# dict_text = goods.to_dict()
# print(df.info())
# print(goods.head())
# print(len(goods))
# print(dict_text)