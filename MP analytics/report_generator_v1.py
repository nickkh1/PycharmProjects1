import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

pd.set_option('display.max_columns', None)


'выбираем файл'
# dirName = 'C:/Users/nick-/Desktop/TG_test'
# listOfFiles = list()
# for(dirpath, dirnames, filenames) in os.walk(dirName):
#     listOfFiles += [os.path.join(dirpath, file) for file in filenames]
# for elem in listOfFiles:
#     print(elem)



df = pd.read_excel('C:/Users/nick-/Desktop/TG_test/2023-01-22—2023-02-20_Мебель_Мебель_для_прихожей_Вешалки_для_одежды_напольная.xlsx')

# print(df.columns)
# print(df.describe())

df_sorted = df.sort_values(by='Выручка', ascending=False)

sellers_df_sorted = df.pivot_table(index=['Продавец'],
                                values=['Выручка', 'Отзывы','Рейтинг','Товар'],
                                aggfunc={'Выручка': np.sum, 'Отзывы': np.mean, 'Рейтинг': np.mean, 'Товар': len}).sort_values(by='Выручка', ascending=False).reset_index()

brands_df_sorted = df.pivot_table(index=['Бренд'],
                                values=['Выручка', 'Отзывы','Рейтинг','Товар'],
                                aggfunc={'Выручка': np.sum, 'Отзывы': np.mean, 'Рейтинг': np.mean, 'Товар': len}).sort_values(by='Выручка', ascending=False).reset_index()

'считаем общую выручку'
total_revenue = df_sorted['Выручка'].sum()
total_missed_revenue = df_sorted['Упущенная выручка'].sum()

''' ТОВАРЫ '''

'выручки на карточку товара'
total_num_goods = len(df_sorted['Выручка'])
goods_10_perc = round(total_num_goods*0.1)
goods_50_perc = round(total_num_goods*0.5)

rev_per_good_all = round(np.mean(df_sorted['Выручка'])) # средняя выручка на карточку
rev_per_good_top100 = round(np.mean(df_sorted.loc[:99, 'Выручка'])) # средняя выручка на карточку из топ 100
rev_per_good_10percentile = round(np.mean(df_sorted.loc[:goods_10_perc, 'Выручка'])) # средняя выручка на карточку из первого 10% персентиля
rev_per_good_50percentile = round(np.mean(df_sorted.loc[:goods_50_perc, 'Выручка'])) # средняя выручка на карточку из первого 50% персентиля

'% выручки товары'
perc_rev_top100 = round(df_sorted.loc[:99, 'Выручка'].sum()/total_revenue, 2) # какую долю выручки занимают первые 100 товаров
perc_rev_10_percentile = round(df_sorted.loc[:goods_10_perc, 'Выручка'].sum() / total_revenue, 2) # какую долю выручки занимают первые 10% товаров
perc_rev_50_percentile = round(df_sorted.loc[:goods_50_perc, 'Выручка'].sum() / total_revenue, 2) # какую долю выручки занимают первые 50% товаров


''' ПРОДАВЦЫ '''
total_num_seller = len(sellers_df_sorted['Выручка'])
seller_10_perc = round(total_num_seller*0.1)
seller_50_perc = round(total_num_seller*0.5)



'% выручки продавцов'
seller_perc_rev_top10 = round(sellers_df_sorted.loc[:9, 'Выручка'].sum()/total_revenue, 2)
seller_perc_rev_top30 = round(sellers_df_sorted.loc[:29, 'Выручка'].sum()/total_revenue, 2)
seller_perc_rev_10_percentile = round(sellers_df_sorted.loc[:seller_10_perc, 'Выручка'].sum() / total_revenue, 2)
seller_perc_rev_50_percentile = round(sellers_df_sorted.loc[:seller_50_perc, 'Выручка'].sum() / total_revenue, 2)
# print(seller_perc_rev_top10, seller_perc_rev_top30, seller_perc_rev_10_percentile, seller_perc_rev_50_percentile)

'кол-во товаров на продавца'
av_goods_per_seller_all = round(np.mean(sellers_df_sorted.loc[:, 'Товар']),1) # среднее кол-во товаров на продавца по всем продавцам
median_goods_pre_seller_all = round(np.median(sellers_df_sorted.loc[:, 'Товар']),1) # медианное кол-во товаров на продавца по все продавцам
av_goods_per_seller_top10perc = round(np.mean(sellers_df_sorted.loc[:seller_10_perc, 'Товар']),1) # среднее кол-во товаров на продавца среди 10% самых успешных продавцов

# print(av_goods_per_seller_all, av_goods_per_seller_top10perc, median_goods_pre_seller_all)


''' РЕЙТИНГИ И ОТЗЫВЫ'''

'отзывы'
av_reviews_all = round(np.mean(df_sorted.loc[:, 'Отзывы']))
av_review_top10 = round(np.mean(df_sorted.loc[:9, 'Отзывы']))
av_review_top30 = round(np.mean(df_sorted.loc[:29, 'Отзывы']))
av_review_top100 = round(np.mean(df_sorted.loc[:99, 'Отзывы']))

low_median_goods = round(total_num_goods/2)-20
upper_median_goods = round(total_num_goods/2)+20
med_review_all = round(np.median(df_sorted.loc[low_median_goods:upper_median_goods, 'Отзывы'])) # среднее кол-во отзывов для медианного среднеуспешного магазина

# print(av_reviews_all, av_review_top10, av_review_top30, av_review_top100, med_review_all)

'рейтинг'

av_rating_goods_all = round(np.mean(df_sorted.loc[:, 'Рейтинг']), 2)
av_rating_goods_top100 = round(np.mean(df_sorted.loc[:99, 'Рейтинг']), 2)

av_rating_seller_top30 = round(np.mean(sellers_df_sorted.loc[:29, 'Рейтинг']), 2)

# print(av_rating_goods_all, av_rating_goods_top100, av_rating_seller_top30)

''' ЦЕНОВЫЕ СЕГМЕНТЫ '''
av_price_top100 = round(np.mean(df_sorted.loc[:99, 'Цена со скидкой']))  # средняя цена на карточку в топ100 карточек
price_perc_25 = round(np.percentile(df_sorted.loc[:, 'Цена со скидкой'], 25)) # 25 персентиль цены всех карточек
price_median = round(np.percentile(df_sorted.loc[:, 'Цена со скидкой'], 50)) # 50 персентиль цены всех карточек
price_perc_75 = round(np.percentile(df_sorted.loc[:, 'Цена со скидкой'], 75)) # 75 персентиль цены всех карточек
# price_stdev = round(np.std(df_sorted.loc[:99, 'Цена со скидкой']))

# print(av_price_top100, price_perc_25, price_median, price_perc_75)


''' ВЕРОЯТНОСТЬ ДОСТИЖЕНИЯ ВЫРУЧКИ'''
goods_100k_rev = round(len(df_sorted[df_sorted['Выручка'] >= 100000]) / total_num_goods, 2) # % карточек с выручкой более 100к
seller_500k_rev = round(len(sellers_df_sorted[sellers_df_sorted['Выручка'] >= 500000]) / total_num_seller, 2) # % продавцов с выручкой более 500к


'топ 15 самых дорогих товаров'

'топ 15 самых дешевых товаров товаров и почему'

# print(brands_df_sorted.head())