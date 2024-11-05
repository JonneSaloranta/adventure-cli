import unittest

from src.items.sword import Sword

class TestSword(unittest.TestCase):
    def test_sword(self):
        sword = Sword()
        self.assertEqual(str(sword), "Sword: A sharp sword, Damage: 5")

if __name__ == "__main__":
    unittest.main()