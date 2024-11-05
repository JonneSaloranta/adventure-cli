
import random

ELEMENTS = {
    "#": 0.1,
    " ": 0.9,
}


class WorldGenerator():
    def __init__(self, seed: str):
        self.seed = seed
        self.rng = random.Random(seed)

    def generate_chunk(self, chunk_x, chunk_y, chunk_size):
        return [
        [random.choices(list(ELEMENTS.keys()), weights=ELEMENTS.values(), k=1)[0] for _ in range(chunk_size)]
        for _ in range(chunk_size)
    ]