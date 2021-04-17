from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50
    caffeine = float

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
