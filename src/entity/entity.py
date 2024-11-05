from src.util.vector2D import Vector2D

class Entity:
    def __init__(self, name: str, description: str, position: Vector2D):
        self.name = name
        self.description = description
        self.position = position


    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def __repr__(self):
        return f"{self.name}: {self.description}, {self.position}"
    
    def get_position(self):
        return self.position
    
    def move_position(self, vector: Vector2D):
        self.position += vector

    def set_position(self, vector: Vector2D):
        self.position = vector