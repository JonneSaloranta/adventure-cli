import unittest
import os

from rich import print
from src.util.serialize import Serializer
from src.util.deserialize import Deserializer

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


class TestDeserialize(unittest.TestCase):
    
    def setUp(self):
        serializer = Serializer("test.pkl")
        serializer.save("test")
    def tearDown(self):
        # print("tearDown")
        pass            

    def test_load(self):
        # Check if FileNotFoundError is raised when loading a non-existent file
        deserializer = Deserializer("non_existent_file.pkl")
        with self.assertRaises(FileNotFoundError):
            deserializer.load()

    

if __name__ == "__main__":
    unittest.main(verbosity=2)