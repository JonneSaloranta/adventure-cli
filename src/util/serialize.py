import pickle
import os

class Serializer:
    def __init__(self, default_path: str):
        self.default_path = default_path

    def save(self, obj, path=None):
        save_path = path or self.default_path
        with open(save_path, 'wb') as f:
            pickle.dump(obj, f)

    def load(self, path=None):
        load_path = path or self.default_path
        with open(load_path, 'rb') as f:
            return pickle.load(f)
