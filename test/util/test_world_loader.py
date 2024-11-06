import unittest
from src.util.world_loader import WorldLoader
from src.world.world import World


class TestWorldLoader(unittest.TestCase):
    
    def setUp(self):
        self.world_loader = WorldLoader()
        self.world = World("test")

    def tearDown(self):
        # print("tearDown")
        pass

    def test_save_world(self):
        self.world_loader.save_world(self.world)
        self.assertTrue(self.world_loader.serializer.default_path)

    def test_load_world(self):
        self.world_loader.save_world(self.world)
        self.assertTrue(self.world_loader.load_world())

if __name__ == "__main__":
    unittest.main(verbosity=2)