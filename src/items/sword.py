from src.items.item import Item

class Sword(Item):
    def __init__(self):
        super().__init__(name="Sword", description="A sharp sword", rarity="Common", base_value=10, weight=2.0)
        self.damage = 5

    def __str__(self):
        return f"{self.name}: {self.description}, Damage: {self.damage}"
    
    def __repr__(self):
        return f"{self.name}: {self.description}, {self.rarity}, {self.base_value}, {self.weight}, {self.damage}"