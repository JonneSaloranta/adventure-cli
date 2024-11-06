
from src.world.world_gen import WorldGenerator
from src.world.tile import Tile


class World:
    def __init__(self, name: str = "World", width: int = 256, height: int = 256, chunk_size: int = 16, seed=None):
        self.name = name
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

    def get_chunk(self, x, y) -> list:
        # raise error if chunk location is not valid
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError("Chunk is out of bounds.")

        return self.chunks.get((x, y))
    
    def get_tile(self, x, y) -> Tile:
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
    
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    
    def get_chunk_size(self) -> int:
        return self.chunk_size
    
    def get_seed(self) -> str:
        return self.seed
    
    def get_chunks(self) -> dict:
        return self.chunks
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str):
        self.name = name

    def to_dict(self):
        return {
            "name": self.name,
            "width": self.width,
            "height": self.height,
            "chunk_size": self.chunk_size,
            "seed": self.seed,
            "chunks": self.chunks
        }
    
    def from_dict(self, data: dict):
        self.name = data.get("name")
        self.width = data.get("width")
        self.height = data.get("height")
        self.chunk_size = data.get("chunk_size")
        self.seed = data.get("seed")
        self.chunks = data.get("chunks")


if __name__ == "__main__":

    from rich import print
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    
    console = Console()

    world = World(width=10, height=10, seed="test")
    world.generate_world()

    table = Table(box=None, show_header=False, show_edge=False)


    chunk = world.get_chunk(0, 0)
    # print(chunk)

    for row in chunk:
        table.add_row("".join([tile.get_symbol() for tile in row]))
        
    console.print(Panel(table, title="2D CLI World", border_style="blue"))
