import pickle

class Serializer:
    def __init__(self, path):
        self.path = path

    def save(self, obj):
        try:
            with open(self.path, 'wb') as f:
                pickle.dump(obj, f)
        except FileNotFoundError:
            print("File not found")

    def load(self):
        with open(self.path, 'rb') as f:
            return pickle.load(f)