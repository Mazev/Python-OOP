import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())

# test rectangle
import unittest


class ShapesTests(unittest.TestCase):
    def test(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.calculate_perimeter(), 60)
        self.assertEqual(r.calculate_area(), 200)


if __name__ == "__main__":
    unittest.main()
