import matplotlib.pyplot as plt
import pandas as pd
import string
from wordcloud import WordCloud
pd.set_option('display.max_columns', None)
# Импортируем библиотеку для лемматизации русских и украинских слов
import pymorphy2
# Импортируем метод word_tokenize из библиотеки nltk
from nltk.tokenize import word_tokenize
# подгружаем библиотеку nltk со стоп-словами
from nltk.corpus import stopwords
# сохраняем список с русскими стоп-cловами в переменную stop_words
stop_words = stopwords.words('russian')

df = pd.read_excel('C:/Users/nick-/Desktop/TG_test/2023-01-22—2023-02-20_Дом_Парфюмерия_для_дома.xlsx')

text = ' '.join(df['Товар'])
text = text.lower()
spec_chars = string.punctuation + '\n\xa0«»\t—…'
# print(len(text))
text = "".join([ch for ch in text if ch not in spec_chars])

# разбиваем текст на токены
# в результате получаем переменную типа list со списком токенов
text_tokens = word_tokenize(text)
print(text_tokens[:50])
print(type(text_tokens))
# убираем стоп слова
tokens_without_sw = [word for word in text_tokens if not word in stop_words]
print(tokens_without_sw[:50])
import nltk
text_new = nltk.Text(tokens_without_sw)
print(type(text_new))
from nltk.probability import FreqDist
fdist = FreqDist(text_new)
print(fdist.most_common(10))

# # инициализируем лемматайзер MorphAnalyzer()
# lemmatizer = pymorphy2.MorphAnalyzer()
#
# # функция для лемматизации текста, на вхд принимает список токенов
# def lemmatize_text(tokens):
#     # создаем переменную для хранения преобразованного текста
#     text_new = ''
#     # для каждого токена в тексте
#     for word in tokens:
#         # с помощью лемматайзера получаем основную форму
#         word = lemmatizer.parse(word)
#         # добавляем полученную лемму в переменную с преобразованным текстом
#         text_new = text_new + ' ' + word[0].normal_form
#     # возвращаем преобразованный текст
#     return text_new
#
# # вызываем функцию лемматизации для списка токенов исходного текста
# text = lemmatize_text(text)

'''облако включая стоп слова - не подгрузил нужный список'''
# Генерируем облако слов и сохраняем в переменной cloud
cloud = WordCloud(stopwords=stop_words).generate(text)
# Выводим облако слов на экран
plt.imshow(cloud)
# Отключаем отображение осей
plt.axis('off')
plt.show()

