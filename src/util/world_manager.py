
from src.world.world import World
from src.util.world_loader import WorldLoader

class WorldManager:
    def __init__(self):
        self.worlds = {}
        self.current_world = None

    def add_world(self, world: World):
        self.worlds[world.name] = world

    def get_world(self, name):
        return self.worlds[name]

    def set_current_world(self, name):
        self.current_world = self.worlds[name]

    def get_current_world(self):
        return self.current_world
    
    def save_world(self, file_name: str):
        world_loader = WorldLoader()
        world_loader.save_world(self.current_world, file_name)

    def load_world(self, file_name: str):
        world_loader = WorldLoader()
        world = world_loader.load_world(file_name)
        self.add_world(world)
        self.set_current_world(world.name)