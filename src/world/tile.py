


class Tile():
    def __init__(self, name: str, symbol: str, walkable: bool, color: str):
        
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        self.name = name
        self.symbol = symbol
        self.walkable = walkable
        self.color = color

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
    def __repr__(self):
        return f"Name: {self.name}, Symbol: {self.symbol}, Walkable: {self.walkable}, Color: {self.color}"
    
    def get_name(self) -> str:
        return self.name
    
    def get_symbol(self) -> str:
        return self.symbol
    
    def is_walkable(self) -> bool:
        return self.walkable
    
    def get_color(self) -> str:
        return self.color
    
    def set_name(self, name: str):
        self.name = name
    
    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def set_walkable(self, walkable: bool):
        self.walkable = walkable

    def set_color(self, color: str):
        self.color = color
    
    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "walkable": self.walkable,
            "color": self.color
        }
    
    def from_dict(self, data: dict):
        self.name = data.get("name")
        self.symbol = data.get("symbol")
        self.walkable = data.get("walkable")
        self.color = data.get("color")


dirt = Tile(name="Dirt",symbol=".", walkable=True, color="green")
grass = Tile(name="Grass",symbol=".", walkable=True, color="green")
water = Tile(name="Water",symbol="#", walkable=False, color="blue")
sand = Tile(name="Sand",symbol=".", walkable=True, color="yellow")
stone = Tile(name="Stone",symbol="O", walkable=True, color="green")
tree = Tile(name="Tree",symbol="#", walkable=False, color="green")
wall = Tile(name="Wall",symbol="#", walkable=False, color="green")