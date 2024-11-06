import pickle
import os
class Serializer:
    def __init__(self, default_path: str):
        self.default_path = default_path
        fileformat = ".pkl"
        if not self.default_path.endswith(fileformat):
            self.default_path.join(fileformat)

    def save(self, obj, path=None):
        save_path = path or self.default_path
        with open(save_path, 'wb') as f:
            pickle.dump(obj, f)

    def load(self, path=None):
        load_path = path or self.default_path
        with open(load_path, 'rb') as f:
            return pickle.load(f)
