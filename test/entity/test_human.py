import unittest

from src.entity.human import Human
from src.util.vector2D import Vector2D

class TestHuman(unittest.TestCase):

    def setUp(self):
        self.human1 = Human(name="John", description="A Human player", position=Vector2D(0, 0))
        
    def tearDown(self):
        # print("tearDown")
        pass

    def test_human(self):
        self.assertEqual(str(self.human1), "John: A Human player")


if __name__ == "__main__":
    unittest.main(verbosity=2)