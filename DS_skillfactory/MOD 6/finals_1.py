# def lucky_ticket(number):
#     sum_f = 0
#     sum_l = 0
#     for char in str(number)[0:3]:
#         sum_f += int(char)
#     for char1 in str(number)[3:6]:
#         sum_l += int(char1)
#     return sum_f == sum_l

# print(lucky_ticket(264543))



# Числа Фибоначчи.

# Напишите функцию def fib_number(), которая получается на вход некоторое
# число n и выводит n-e число Фибоначчи.
# Задачу можно решить как с помощью цикла for, так и с помощью цикла while

# Примечание: числа Фибоначчи определяются так


# ```
# a0 = 0, a1 = 1, a2 = a1 + a0 = 1, an = a_n-1 + a_n-2
# ```

# Примечание: в модуле по функциям уже было задание на вычисление чисел Фибоначчи
# с помощью рекурсивных функций. Здесь необходимо реализовать те же вычисления,
# но без использования рекурсии.

# def fib_number(n):
#   a_res = None
#   a0 = 0
#   a1 = 1
#   if n == 1:
#     return a1
#   if n == 0:
#     return a0
#   count = 2
#   while count <= n:
#     a_res = a0 + a1
#     a0 = a1
#     a1 = a_res
#     count += 1
#   return a_res
#
# print(fib_number(0))
# print(fib_number(1))
# print(fib_number(2))
# print(fib_number(3))
# print(fib_number(4))
# print(fib_number(6))







# Напишите функцию def matrix_sum(), которая получает на вход две матрицы
# и возвращает их сумму.

# Примечание: чтобы найти сумму двух матриц, нужно просуммировать
# их соответствующие элементы. Но перед этим необходимо проверить, что размеры
# матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк)
# matrix_example = [
#     [1, 5, 4],
#     [4, 2, -2],
#     [7, 65, 88]
# ]
#
#
# def matrix_sum(matrix1, matrix2):
#     # check matrices dimensions
#     if (len(matrix1) != len(matrix2)) or (len(matrix1[0]) != len(matrix2[0])):
#         print("Error! Matrices dimensions are different!")
#         return
#
#     matrix_lines = len(matrix1)
#     matrix_rows = len(matrix1[0])
#
#     # find matrix sum
#     sum_matrix = []
#
#     for i in range(matrix_lines):
#
#         line_tmp = []
#         for j in range(matrix_rows):
#             line_tmp.append(matrix1[i][j] + matrix2[i][j])
#         sum_matrix.append(line_tmp)
#
#     return sum_matrix
#
#
# print(matrix_sum(matrix_example, matrix_example))



#
# Реализуйте программу, которая сжимает последовательность символов. На вход подаётся последовательность вида:
#
# aaabbccccdaa
# Необходимо вывести строку, состоящую из символов и количества повторений этого символа. Вывод должен выглядеть как:
#
# a3b2c4d1a2

# str_example = 'aaabbccccdaa'
# first_symbol = str_example[0]
# count = 0
# new_str = ''
# for symbol in str_example:
#   if symbol == first_symbol:
#     count += 1
#   else:
#     new_str += first_symbol + str(count)
#     first_symbol = symbol
#     count = 1
#
# new_str += first_symbol + str(count)
# print(new_str)


alphabet_str = 'abcdefghijklmnopqrstuvwqyz'
letters_dict = {letter: 0 for letter in alphabet_str}
print(letters_dict)


