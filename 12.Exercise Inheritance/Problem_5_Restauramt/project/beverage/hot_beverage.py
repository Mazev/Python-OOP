from project.beverage.beverage import Beverage


class HotBeverage(Beverage):
    MILLILITERS = 50
    PRICE = 3.50
    caffeine = float

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def price(self):
        return self.PRICE

    @price.setter
    def price(self, value):
        self.name = value

    @property
    def milliliters(self):
        return self.MILLILITERS

    @milliliters.setter
    def milliliters(self, value):
        self.milliliters = value
