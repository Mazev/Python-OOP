class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        hero = Hero("Alexander", 75)
        self.assertEqual(hero.name, "Alexander")
        self.assertEqual(hero.health, 75)

    def test_attack_success(self):
        hero = Hero("Alexander", 75)
        hero.defend(20)
        self.assertEqual(hero.health, 55)

    def test_attack_killed(self):
        hero = Hero("Alexander", 75)
        res = hero.defend(100)
        self.assertEqual(hero.health, 0)
        self.assertEqual(res, "Alexander was defeated")

    def test_heal(self):
        hero = Hero("Alexander", 5)
        hero.heal(20)
        self.assertEqual(hero.health, 25)


if __name__ == "__main__":
    unittest.main()