
from .human import Human

class NPC(Human):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def __str__(self):
        return f'{self.name} ({self.age}) - {self.role}'