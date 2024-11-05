import pickle

class Deserializer:
    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, 'rb') as f:
            return pickle.load(f)