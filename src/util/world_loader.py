from src.util.serialize import Serializer
from src.world.world import World

class WorldLoader:
    def __init__(self, serializer=None, path='world'):
        self.serializer = serializer or Serializer(path)

    def save_world(self, world: World):
        self.serializer.save(world)

    def load_world(self) -> World:
        return self.serializer.load()
