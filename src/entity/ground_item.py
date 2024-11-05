
from entity.entity import Entity

class GroundItem(Entity):
    def __init__(self, item, x, y):
        super().__init__(x, y, item.char, item.color, item.name)
        self.item = item
        self.item.x = self.x
        self.item.y = self.y

    def pick_up(self, inventory):
        if len(inventory.items) >= 26:
            return False

        inventory.items.append(self.item)
        return True

    def drop(self):
        return self.item

    def render(self, console):
        console.print(self.x, self.y, self.char, self.color)