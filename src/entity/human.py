

from src.entity.entity import Entity

class Human(Entity):
    def __init__(self, name, description, position):
        super().__init__(name, description, position)