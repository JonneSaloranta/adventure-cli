import unittest

from src.entity.entity import Entity
from src.world.vector2D import Vector2D

class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity1 = Entity(name="John", description="A Human player", position=Vector2D(0, 0))

    def tearDown(self):
        # print("tearDown")
        pass
        
    def test_entity(self):
        self.assertEqual(str(self.entity1), "John: A Human player")

    def test_entity_position(self):
        self.assertEqual(self.entity1.get_position(), Vector2D(0, 0))

    def test_entity_repr(self):
        self.assertEqual(repr(self.entity1), "John: A Human player, (0, 0)")

    def test_entity_move_position(self):
        self.entity1.move_position(Vector2D(1, 1))
        self.assertEqual(self.entity1.get_position(), Vector2D(1, 1))

    def test_entity_set_position(self):
        self.entity1.set_position(Vector2D(2, 2))
        self.assertEqual(self.entity1.get_position(), Vector2D(2, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)