import unittest

from src.entity.player import Player
from src.util.vector2D import Vector2D

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.Player1 = Player(name="John", description="A Human player", position=Vector2D(0, 0))
        
    def tearDown(self):
        # print("tearDown")
        pass

    def test_player(self):
        self.assertEqual(str(self.Player1), "John")


if __name__ == "__main__":
    unittest.main(verbosity=2)