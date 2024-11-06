import unittest
import os

from rich import print
from src.util.serialize import Serializer

class TestSerialize(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        # print("tearDown")
        pass

    def test_save(self):
        serializer = Serializer("test.pkl")
        serializer.save({"key": "value"})  # Save a simple dictionary to test.pkl

        # Check if the file was created
        self.assertTrue(os.path.exists("test.pkl"))

        # Clean up after test
        os.remove("test.pkl")

    

if __name__ == "__main__":
    unittest.main(verbosity=2)