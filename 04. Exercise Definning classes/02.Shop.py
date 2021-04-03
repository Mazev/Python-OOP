class Shop:

    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return f"{len(self.items)}"


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         shop = Shop("Product Shop", [1, 2, 3])
#         self.assertEqual(shop.name, "Product Shop")
#         self.assertEqual(shop.items, [1, 2, 3])
#
#     def test_get_items_when_0(self):
#         shop = Shop("Product Shop", [])
#         self.assertEqual(shop.get_items_count(), 0)
#
#     def test_get_items_bigger_than_0(self):
#         shop = Shop("Product Shop", [1, 2, 3])
#         self.assertEqual(shop.get_items_count(), 3)
#
#
# if __name__ == "__main__":
#     unittest.main()