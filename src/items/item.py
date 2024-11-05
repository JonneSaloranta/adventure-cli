

class Item:
    def __init__(self, name: str, description: str, rarity: str, base_value: int, weight: float):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.base_value = base_value
        self.weight = weight

    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def __repr__(self):
        return f"{self.name}: {self.description}, {self.rarity}, {self.base_value}, {self.weight}"