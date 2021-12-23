# class DepartmentReport():
#     # Позволим добавлять много разных сделок
#     def add_revenue(self, revenue):
#         # На первой сделке создадим список для хранения всех сделок
#         if not hasattr(self, 'revenues'):
#             self.revenues = []
#             # Добавим текущую сделку
#         self.revenues.append(revenue)
#
#         # Посчитаем сумму всех сделок
#
#     def average_revenue(self):
#         return sum(self.revenues)/len(self.revenues)
#
# report = DepartmentReport()
# report.add_revenue(1000000)
# report.add_revenue(400000)
# print(report.revenues)
# # => [1000000, 400000]
# print(report.average_revenue())
# # => 700000.0


# class SalesReport():
#     def __init__(self):
#         self.deals = []
#
#     def add_deal(self, amount):
#         self.deals.append(amount)
#
#     def total_amount(self):
#         return sum(self.deals)
#
#     def print_report(self):
#         print("Total sales:", self.total_amount())
#
#
# report = SalesReport()
# print(report.deals)
# # => []
# report.print_report()
# # => 0


# class SalesReport():
#     # Будем принимать в __init__ ещё и имя менеджера
#     def __init__(self, manager_name):
#         self.deals = []
#         self.manager_name = manager_name
#
#     def add_deal(self, amount):
#         self.deals.append(amount)
#
#     def total_amount(self):
#         return sum(self.deals)
#
#     def print_report(self):
#         # И добавлять это имя в отчёт
#         print("Manager:", self.manager_name)
#         print("Total sales:", self.total_amount())
#
#
# report = SalesReport("Ivan Taranov")
# report.add_deal(10_000)
# report.add_deal(30_000)
# report.print_report()


class DepartmentReport():
    def __init__(self, company_name):
        self.revenues = []
        self.company_name = company_name

    def add_revenue(self, revenue):
        self.revenues.append(revenue)

    def average_revenue(self):
        return f'Average department revenue for {self.company_name}: {round(sum(self.revenues)/len(self.revenues))}'

report = DepartmentReport("Danon")
report.add_revenue(1_000_000)
report.add_revenue(400_000)

print(report.average_revenue())
# => Average department revenue for Danon: 700000