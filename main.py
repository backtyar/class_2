# 1.  Создайте систему классов для электронной библиотеки.У вас
# должен быть базовый класс Item для представления элементов библиотеки
# (например, книг и видео), с атрибутами, такими как title, author, и year.
# Создайте подклассы для разных типов элементов (например, Book и Video),
# которые будут наследовать от базового класса Item. Реализуйте инкапсуляцию,
# чтобы контролировать доступ к атрибутам, и добавьте методы для вывода
# информации о каждом элементе.
#
# class Item:
#
#     def __init__(self, title, author, year):
#         self.__title = title
#         self.__author = author
#         self.__year = year
#
#     def __str__(self):
#         return (f"Class: {self.__class__.__name__} \nTitle: {self.__title}"
#                 f" \nAuthor: {self.__author}  \nYear: {self.__year}")
#
#
# class Book(Item):
#     pass
#
# class Video(Item):
#     pass
#
# book = Book('Марсианин Джон Картер', 'Эдгар Райс Берроуз',1943)
# print(book)
# print('*' * 50)
# video = Video('Shorts', 'Tom',2023)
# print(video)






#2. Создайте систему классов для представления заказов в интернет-магазине.
# Создайте класс Product с атрибутами, такими как name, price, и quantity.
# Затем создайте класс Order, который может содержать несколько
# экземпляров Product. Реализуйте методы для добавления и удаления товаров
# из заказа, а также для вычисления общей суммы заказа.

# class Product:
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __str__(self):
#         return f'{self.name}, {self.price}, {self.quantity}'
#
# banana = Product('banana', 150, 5)
# orange = Product('orange', 200, 10)
# onion = Product('onion', 200, 15)
#
#
# class Order:
#
#     def __init__(self):
#         self.__list_product = []
#         self.sum = 0
#
#     def add_copy_product(self, copy_product):
#         self.__list_product.append(copy_product)
#
#
#     def convertor(self):
#         for i in self.__list_product:
#             self.sum += int(str(i).split(',')[1])
#         return self.sum




# mark = Order()
# mark.add_copy_product(banana)
# mark.add_copy_product(orange)
# mark.add_copy_product(onion)
# mark.convertor()
# print(mark.sum)