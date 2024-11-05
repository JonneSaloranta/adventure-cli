
from .human import Human
from src.util.vector2D import Vector2D

class Player(Human):
    def __init__(self, name: str, description: str, position: Vector2D):
        super().__init__(name, description, position)

    def __str__(self):
        return f'{self.name}'