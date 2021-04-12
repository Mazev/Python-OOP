# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#
# book = Book("My Book", "Me", 200)
# print(book.name)
# print(book.author)
# print(book.pages)


# x = "global"
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal  x
#         x = "nonlocal"
#         print("inner:", x)
#
#     def change_global():
#         global x
#         x = "global: changed!"
#
#     print("outer:", x)
#     inner()
#     print("outer:", x)
#     change_global()
#
#
# print(x)
# outer()
# print(x)
