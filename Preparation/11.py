# class Mammal:
#     __kingdom = "animals"
#
#     def __init__(self, name, type, sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def get_kingdom(self):
#         return Mammal.__kingdom
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"
#
#
#
#
# mammal = Mammal("Dog", "Domestic", "Bark")
# print(mammal.make_sound())
# print(mammal.get_kingdom())
# print(mammal.info())

#
# class Account:
#     def __init__(self, id, balance, pin):
#         self.__id = id
#         self.__pin = pin
#         self.balance = balance
#
#     def get_id(self, pin):
#         if self.__pin != pin:
#             return "Wrong pin"
#
#         return self.__id
#
#     def change_pin(self, old_pin, new_pin):
#         if old_pin == self.__pin:
#             self.__pin = new_pin
#             return "Pin changed"
#         return 'Wrong pin'
#
#
# account = Account(8827312, 100, 3421)
# print(account.get_id(1111))
# print(account.get_id(3421))
# print(account.balance)
# print(account.change_pin(2212, 4321))
# print(account.change_pin(3421, 1234))
