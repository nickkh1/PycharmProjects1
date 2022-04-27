import pandas as pd
import category_encoders as ce


# инициализируем информацию об одежде
clothing_list = [
    ['xxs', 'dress'],
    ['xxs', 'skirt'],
    ['xs', 'dress'],
    ['s', 'skirt'],
    ['m', 'dress'],
    ['l', 'shirt'],
    ['s', 'coat'],
    ['m', 'coat'],
    ['xxl', 'shirt'],
    ['l', 'dress']
]

clothing = pd.DataFrame(clothing_list, columns = ['size',  'type'])

'''кодируем порядковую переменную'''
# ord_encoder = ce.OrdinalEncoder()
# data_bin = ord_encoder.fit_transform(clothing[['size', 'type']])
# clothing = pd.concat([clothing, data_bin], axis=1)

'''кодируем одинарным способом'''
# encoder = ce.OneHotEncoder(cols=['type']) # указываем столбец для кодирования
# type_bin = encoder.fit_transform(clothing['type'])
# clothing = pd.concat([clothing, type_bin], axis=1)

'''кодируем двоичным способом'''
bin_encoder = ce.BinaryEncoder(cols=['type']) # указываем столбец для кодирования
type_bin = bin_encoder.fit_transform(clothing['type'])
clothing = pd.concat([clothing, type_bin], axis=1)

print(clothing)