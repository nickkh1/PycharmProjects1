# class User():
#     def __init__(self, email, password, balance):
#         self.email = email
#         self.password = password
#         self.balance = balance
#
#     def login(self, email_l, password_l):
#         if email_l == self.email and password_l == self.password:
#             print(True)
#         else:
#             print(False)
#
#     def update_balance(self, amount):
#         self.balance = self.balance + amount
#         print(f' Your balance is {self.balance}')
#
#
# user = User("gosha@roskino.org", "qwerty", 20000)
# user.login("gosha@roskino.org", "qwerty123")
# user.login("gosha@roskino.org", "qwerty")
# user.update_balance(200)
# user.update_balance(-500)

import os

def walk_desc(path=None):
    start_path = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print("Текущая директория", root)
        print("---")

        if dirs:
            print("Список папок", dirs)
        else:
            print("Папок нет")
        print("---")

        if files:
            print("Список файлов", files)
        else:
            print("Файлов нет")
        print("---")

        if files and dirs:
            print("Все пути:")
        for f in files:
            print("Файл ", os.path.join(root, f))
        for d in dirs:
            print("Папка ", os.path.join(root, d))
        print("===")

walk_desc()
