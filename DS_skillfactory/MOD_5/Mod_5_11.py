# Напишите рекурсивную функцию power(val, n), которая возводит число
# в заданную целую натуральную степень (или в степень 0).
# def power(val, n):
#     if n == 0: return 1
#     if n == 1: return val
#     return power(val,n-1)*val
#
# print(power(4,0))
# print(power(4,3))

# 2
# Напишите функцию is_leap(year), которая принимает на вход год и возвращает True, если год високосный, иначе — False.
# def is_leap(year):
#     if year%4 == 0 and not year % 100 == 0:
#         return True
#     if year%400==0:
#         return True
#     return False

# 3
# проверка даты рождения
def check_date(day, month, year):
    def is_leap(year):
        if year % 400 == 0: return True
        if year % 100 == 0: return False
        if year % 4 == 0: return True
        return False

    if type(day) is not int:
        return False
    elif type(month) is not int:
        return False
    elif type(year) is not int:
        return False

    if month > 12 or month < 1:
        return False

    if day < 1: return False
    if day > 31: return False
    if month in [2, 4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if is_leap(year):
            if day > 29: return False
        else:
            if day > 28: return False
    return True

# 4
# Эта функция принимает на вход фамилию, имя, дату рождения (в виде кортежа из трёх чисел — день, месяц, год), отчество и список, в который необходимо сохранить полученные аргументы в виде кортежа в следующем порядке:
# фамилия, имя, отчество, день, месяц, год рождения
# Функция возвращает список, в который добавила запись.

# def register(surname, name, date, middle_name=None, registry=None):
#    if registry is None:
#        registry = list()
#    if not check_date(*date):
#        raise ValueError("Invalid Date!")
#    registry.append((surname, name, middle_name, date[0], date[1], date[2]))
#    return registry
#
# # def sort_registry(registry):
# #    registry.sort(key=lambda x:
# #                  (x[-1], x[-2], x[-3], x[0], x[1], x[2]))
# #    return registry
#
#
# def get_strings(registry):
#    def get_line(record):
#        m, d, y = record[-3:]
#        m = str(m).zfill(2)
#        d = str(d).zfill(2)
#        y = str(y).zfill(4)
#        if record[2] is None:
#            result = record[0]+" "+record[1][0]+"., "
#            result += m+'.'+d+'.'+y
#        else:
#            result = record[0]+" "+record[1][0]+"."+record[2][0]+"., "
#            result += m+'.'+d+'.'+y
#        return result
#    reg = filter(lambda x: x[-1] >= 2000, registry)
#    reg = map(get_line, reg)
#    return list(reg)
#
# reg = [('Ivanov', 'Sergej', None, 24, 9, 1995),
#       ('Smith', 'John', None, 13, 2, 2003),
#       ('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003)]
# print(get_strings(reg))
# print(reg[0][0][0])


def print_students(students, groups):
   def group_gen(n):
       while True:
           for i in range(1, n+1):
               yield i
   for student, group in zip(students, group_gen(groups)):
       print(student, 'studies in group', group)

reg = ['Smith J., 13.02.2003', 'Petrova M.I., 13.03.2003']
print_students(reg, 3)