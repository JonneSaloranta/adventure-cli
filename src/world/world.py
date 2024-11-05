
from src.world.world_gen import WorldGenerator


class World:
    def __init__(self, width=256, height=256, chunk_size=16, seed=""):
        self.width = width
        self.height = height
        self.chunk_size = chunk_size
        self.chunks = {}
        self.seed = seed
        self.generator = WorldGenerator(seed)

    def generate_world(self):
        for x in range(self.width):
            for y in range(self.height):
                self.chunks[(x, y)] = self.generator.generate_chunk(x, y, self.chunk_size)

    def get_chunk(self, x, y):
        return self.chunks.get((x, y))
    
    def get_tile(self, x, y):
        chunk_x = x // self.chunk_size
        chunk_y = y // self.chunk_size
        chunk = self.get_chunk(chunk_x, chunk_y)
        if chunk:
            return chunk[x % self.chunk_size][y % self.chunk_size]
        return None
    
    def set_tile(self, x, y, tile):
        chunk_x = x // self.chunk_size
        chunk_y = y // self.chunk_size
        chunk = self.get_chunk(chunk_x, chunk_y)
        if chunk:
            chunk[x % self.chunk_size][y % self.chunk_size] = tile
        return None
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_chunk_size(self):
        return self.chunk_size
    
    def get_seed(self):
        return self.seed
    
    def get_chunks(self):
        return self.chunks