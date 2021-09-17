# text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
#
# def get_unique_words(text):
#   punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
#   for symbol in punctuation_list:
#     text = text.replace(symbol, "")
#   words_list = text.split()
#   words_list = list(set(words_list))
#   words_list.sort()
#   return words_list
#
# def get_most_frequent_word(text):
#   unique_words = get_unique_words(text)
#   word_count = 0
#   most_frequent_word = ''
#   for word in unique_words:
#     if text.count(word) > word_count:
#       word_count = text.count(word)
#       most_frequent_word = word
#   return most_frequent_word
#
# get_most_frequent_word(text_example)
#
# print(get_most_frequent_word(text_example))


def holes_count(number):
  holes_dict = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
  str_number = str(number)
  holes_count = 0
  for digit in str_number:
    holes_count += holes_dict.get(digit,0)
  return holes_count

print(holes_count(123))
print(holes_count(8888))