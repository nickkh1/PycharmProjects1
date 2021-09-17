# marks = [4,5,5,5,5,3,4,4,5,4,5]
#
# def mean_mark(name, *marks):
#    result = sum(marks) / len(marks)
#    # Не возвращаем результат, а печатаем его
#    print(name+':', result)
#
# mean_mark('Кузнецов', *marks)

def root_generator(values):
   for val in values:
       if val >= 0:
           result = val ** 0.5
           yield result

new_root_generator = root_generator([-5, 25, 36, -25, 0])

for elem in new_root_generator:
   print(elem)