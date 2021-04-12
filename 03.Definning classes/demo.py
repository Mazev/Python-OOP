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


# class Music:
#     def __init__(self, title, artist, lyrics):
#         self.title = title
#         self.artist = artist
#         self.lyrics = lyrics
#
#     def print_info(self):
#         return f'This is "{self.title}" from "{self.artist}"'
#
#
#     def play(self):
#         return self.lyrics
#
#
# song = Music("Title", "Artist", "Lyrics")
# print(song.print_info())
# print(song.play())


# class Cup:
#     def __init__(self, size, quantity):
#         self.size = size
#         self.quantity = quantity
#
#     def get_free_size(self):
#         return self.size - self.quantity
#
#     def fill(self, milliliters):
#         if self.get_free_size() < milliliters:
#             return
#         self.quantity += milliliters
#
#     def status(self):
#         return self.get_free_size()
#
#
# cup = Cup(100, 50)
# cup.fill(50)
# cup.fill(10)
# print(cup.status())


# class Flower:
#     def __init__(self, name, water_requirements):
#         self.name = name
#         self.water_requirements = water_requirements
#         self.is_happy = False
#
#     def water(self, quantity):
#         if quantity >= self.water_requirements:
#             self.is_happy = True
#
#     def status(self):
#         if self.is_happy:
#             return f"{self.name} is happy"
#
#         return f"{self.name} is not happy"
#
#
# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(100)
# print(flower.status())



# class Car:
#     def __init__(self, name, model, engine):
#         self.name= name
#         self.model = model
#         self.engine = engine
#
#     def get_info(self):
#         return f"This is {self.name} {self.model} with engine {self.engine}"
#
#
#
#
# car = Car("Kia", "Rio", "1.3L B3 I4")
# print(car.get_info())



