# import numpy as np
# np.random.seed(2021)
# # В simple сохраните случайное число в диапазоне от 0 до 1
# simple = np.random.rand()
# # Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# # в переменную randoms
# randoms = np.random.uniform(-150, 2021, size=120)
# # Получите массив из случайных целых чисел от 1 до 100 (включительно)
# # из 3 строк и 2 столбцов. Сохраните результат в table
# table = np.random.randint(1, 101, size=(3,2))
# # В переменную even сохраните чётные числа от 2 до 16 (включительно)
# even = np.arange(2,17,2)
# # Перемешайте числа в even так, чтобы массив even изменился
# np.random.shuffle(even)
# # Получите из even 3 числа без повторений. Сохраните их в переменную select
# select = np.random.choice(even, replace=False, size=3)
# # Получите переменную triplet, которая должна содержать перемешанные
# # значения из массива select (сам select измениться не должен)
# triplet = np.random.permutation(select)

# import numpy as np
# array = np.int64(np.array([1, 2, 3, 4, 5]))
# seed = np.random.randint(2**32-1)
# print(seed)
# np.random.seed(seed)
# print(np.random.seed(seed))
# result = np.random.permutation(array)
# print(result)



import numpy as np

# def min_max_dist(*vectors):
#     dists = list()
#     for i in range(len(vectors)):
#         for j in range(i + 1, len(vectors)):
#             dists.append(np.linalg.norm(vectors[i] - vectors[j]))
#     return (min(dists), max(dists))
#
#
# vec1 = np.array([1, 2, 3])
# vec2 = np.array([4, 5, 6])
# vec3 = np.array([7, 8, 9])
# print(min_max_dist(vec1, vec2, vec3))


import numpy as np

def get_unique_loto(num):
    sample = np.arange(1, 101)
    res = list()
    for i in range(num):
        res.append(np.random.choice(sample, replace=False, size=(5, 5)))
    res = np.array(res)
    return res
print(get_unique_loto(3))


