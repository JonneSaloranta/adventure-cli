import unittest
from rich import print

from src.world.world import World

class TestWorld(unittest.TestCase):
    
    def setUp(self):
        self.world = World(width=10, height=10, chunk_size=16, seed="test")

    def tearDown(self):
        # print("tearDown")
        pass

    def test_get_width(self):
        self.assertEqual(self.world.get_width(), 10)

    def test_get_height(self):
        self.assertEqual(self.world.get_height(), 10)

    def test_get_chunk_size(self):
        self.assertEqual(self.world.get_chunk_size(), 16)

    def test_get_seed(self):
        self.assertEqual(self.world.get_seed(), "test")

    def test_get_chunk(self):
        self.assertEqual(self.world.get_chunk(0, 0), None)

    def test_get_tile(self):
        self.assertEqual(self.world.get_tile(0, 0), None)

    def test_set_tile(self):
        self.assertEqual(self.world.set_tile(0, 0, "#"), None)

    def test_generate_world(self):
        self.world.generate_world()
        self.assertNotEqual(self.world.get_chunk(0, 0), None)
        print(self.world.get_chunk(0, 0))

    def test_get_chunks(self):
        self.assertEqual(self.world.get_chunks(), {})
        self.assertRaises(ValueError, self.world.get_chunk, -1, -1)
        self.assertRaises(ValueError, self.world.get_chunk, 10, 10)

    def test_get_name(self):
        self.assertEqual(self.world.get_name(), "World")

    def test_set_name(self):
        self.world.set_name("Test")
        self.assertEqual(self.world.get_name(), "Test")

    def test_to_dict(self):
        self.assertEqual(self.world.to_dict(), {
            "name": "World",
            "width": 10,
            "height": 10,
            "chunk_size": 16,
            "seed": "test",
            "chunks": {}
        })

    def test_from_dict(self):
        data = {
            "name": "Test",
            "width": 20,
            "height": 20,
            "chunk_size": 32,
            "seed": "test",
            "chunks": {}
        }
        self.world.from_dict(data)
        self.assertEqual(self.world.get_name(), "Test")
        self.assertEqual(self.world.get_width(), 20)
        self.assertEqual(self.world.get_height(), 20)
        self.assertEqual(self.world.get_chunk_size(), 32)
        self.assertEqual(self.world.get_seed(), "test")
        self.assertEqual(self.world.get_chunks(), {})
    

if __name__ == "__main__":
    unittest.main(verbosity=2)