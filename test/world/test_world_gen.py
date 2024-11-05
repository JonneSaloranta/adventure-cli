import unittest

from src.world.world_gen import WorldGenerator

class TestWorldGenerator(unittest.TestCase):
    
    def setUp(self):
        self.world_gen = WorldGenerator(seed="test")

    def tearDown(self):
        # print("tearDown")
        pass

    def test_generate_chunk(self):
        self.assertEqual(len(self.world_gen.generate_chunk(0, 0, 10)), 10)
        self.assertEqual(len(self.world_gen.generate_chunk(0, 0, 10)[0]), 10)
        self.assertEqual(len(self.world_gen.generate_chunk(0, 0, 5)), 5)
        self.assertEqual(len(self.world_gen.generate_chunk(0, 0, 5)[0]), 5)
        self.assertEqual(len(self.world_gen.generate_chunk(0, 0, 1)), 1)
        self.assertEqual(len(self.world_gen.generate_chunk(0, 0, 1)[0]), 1)
    
    def test_generate_combined_seed(self):
        self.assertEqual(self.world_gen.generate_combined_seed("test", 0, 0), "test_0_0")

    def test_get_seed(self):
        self.assertEqual(self.world_gen.get_seed(), "test")


if __name__ == "__main__":
    unittest.main(verbosity=2)