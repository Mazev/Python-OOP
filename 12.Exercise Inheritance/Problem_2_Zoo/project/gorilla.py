from project.animal import Animal
from project.mammal import Mammal


class Gorilla(Animal, Mammal):
    def __init__(self):
        Animal.__init__(self)
        Mammal.__init__(self)


print(Gorilla.mro())
