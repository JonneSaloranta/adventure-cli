
from src.util.vector2D import Vector2D

class WorldObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return Vector2D(self.x, self.y)

    def set_position(self, Vector2D):
        self.x = Vector2D.x
        self.y = Vector2D.y

    def move(self, Vector2D):
        self.x += Vector2D.x
        self.y += Vector2D.y