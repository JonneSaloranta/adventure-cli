import random

from src.world.tile import dirt, grass, water, sand, stone, tree, wall

ELEMENTS = {
    dirt: 0.1,
    grass: 0.9,
    water: 0.1,
    sand: 0.1,
    stone: 0.1,
    tree: 0.1,
    wall: 0.1
}


class WorldGenerator:
    def __init__(self, seed: str = None):
        if not seed:
            self.seed = random.randint(0, 1000000000)
        else:
            self.seed = seed

    def generate_chunk(self, chunk_x, chunk_y, chunk_size):

        self.generate_combined_seed(self.seed, chunk_x, chunk_y)

        return [
            [random.choices(list(ELEMENTS.keys()), weights=ELEMENTS.values(), k=1)[0] for _ in range(chunk_size)]
            for _ in range(chunk_size)
        ]

    def get_seed(self):
        return self.seed

    def generate_combined_seed(self, seed: str, chunk_x: int, chunk_y: int) -> str:
        new_X = str(chunk_x)
        new_Y = str(chunk_y)

        combined_seed = f"{seed}_{new_X}_{new_Y}"
        random.seed(combined_seed)
        return combined_seed
    
if __name__ == "__main__":
    world_gen = WorldGenerator(seed="test")
    print(world_gen.generate_combined_seed("test", 0, 0))