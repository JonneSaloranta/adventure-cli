import unittest
from rich import print

from src.world.tile import Tile

class TestTile(unittest.TestCase):
    
    def setUp(self):
        self.dirt = Tile(name="Dirt",symbol=".", walkable=True, color="brown")

    def tearDown(self):
        # print("tearDown")
        pass

    def test_get_name(self):
        self.assertEqual(self.dirt.get_name(), "Dirt")

    def test_get_symbol(self):
        self.assertEqual(self.dirt.get_symbol(), ".")

    def test_is_walkable(self):
        self.assertTrue(self.dirt.is_walkable())
    
    def test_get_color(self):
        self.assertEqual(self.dirt.get_color(), "brown")

    def test_set_name(self):
        self.dirt.set_name("New Dirt")
        self.assertEqual(self.dirt.get_name(), "New Dirt")

    def test_set_symbol(self):
        self.dirt.set_symbol("N")
        self.assertEqual(self.dirt.get_symbol(), "N")

    def test_set_walkable(self):
        self.dirt.set_walkable(False)
        self.assertFalse(self.dirt.is_walkable())

    def test_set_color(self):
        self.dirt.set_color("black")
        self.assertEqual(self.dirt.get_color(), "black")

    def test_to_dict(self):
        self.assertEqual(self.dirt.to_dict(), {
            "name": "Dirt",
            "symbol": ".",
            "walkable": True,
            "color": "brown"
        })

    def test_from_dict(self):
        data = {
            "name": "New Dirt",
            "symbol": "N",
            "walkable": False,
            "color": "black"
        }
        self.dirt.from_dict(data)
        self.assertEqual(self.dirt.to_dict(), data)

    def test_str(self):
        self.assertEqual(str(self.dirt), "Dirt (.)")

    def test_repr(self):
        self.assertEqual(repr(self.dirt), "Name: Dirt, Symbol: ., Walkable: True, Color: brown")

    def test_symbol_length(self):
        with self.assertRaises(ValueError):
            Tile(name="Dirt",symbol="..", walkable=True, color="brown")

if __name__ == "__main__":
    unittest.main(verbosity=2)