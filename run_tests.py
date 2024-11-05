import unittest

if __name__ == "__main__":
    # Run all tests in the test directory
    loader = unittest.TestLoader()
    suite = loader.discover("test")
    runner = unittest.TextTestRunner()

    runner.run(suite)