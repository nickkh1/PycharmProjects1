# import random
# my_list = []
# for i in range(0, 10):
#     my_list.append(random.randint(0, 10))
# print(my_list)
#
# sum_ = 0
# print(len(my_list))
# val = 0
# while val < len(my_list):
#   sum_ += my_list[val]
#   val += 1
# print(sum_)


# str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
# str_str = {}
# sum_ = 0
#
# for s in str_list:
#   for chr in s:
#     if chr == 't':
#       sum_ += 1
#     str_str[s] = sum_
#   sum_ = 0
#
# print(str_str)

#5.4
# current_health = 500
# attack = 80
# num_sec = 0
#
# while current_health > 0:
#     current_health -= attack
#     num_sec += 1
# print(num_sec)

# 5.5
# import random
# my_list = []
# for i in range(3):
#     my_list.append(random.randint(0, 100000))
# print(my_list)
#
# dict1 = {}
# listt = []
# summm = 0
# i = 0
# for val in my_list:
#     for k in (10000,1000,100,10):
#         if val//k > 1:
#             summm+=val//k
#     listt.append(summm)
#     i += 1
# print(listt)

# import random
# my_list = []
# for i in range(3):
#     my_list.append(random.randint(0, 100000))
# print(my_list)
#
# digit_sum = 0
# for element in my_list:
#   tmp_sum = 0
#   while element > 0:
#     last_digit = element % 10
#     tmp_sum += last_digit
#     element = element // 10
#   if tmp_sum > digit_sum:
#     digit_sum = tmp_sum
#
# print(digit_sum)



# str_list = ['Hello', 'my', 'name', 'is', 'Ezeikel', 'I', 'like', 'kniting']
# req_num = 3
# i = 0
# str_tmp = ""
#
# for ind, word in enumerate(str_list):
#   str_tmp = word[0:req_num]
#   print(ind, str_tmp)



sentence = 'A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm'
sentence = sentence.lower()
word_list = sentence.split()
word_list.sort()
word_dict = {}
print(word_list)

for word in word_list:
  if word not in word_dict.keys():
    word_dict[word] = word_list.count(word)
    print(word_dict.keys())

print(word_dict)





