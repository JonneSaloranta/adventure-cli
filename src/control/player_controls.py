import keyboard

from src.util.vector2D import Vector2D

class PlayerControls:
    def __init__(self):
        self.move = None

    def move_player(self, direction: Vector2D):
        self.move = direction

    def get_move(self):
        return self.move

    def is_moving(self):
        return self.move is not None

    def reset_move(self):
        self.move = None

    def check_input(self):
        if keyboard.is_pressed("w"):
            self.move_player("w")
        elif keyboard.is_pressed("a"):
            self.move_player("a")
        elif keyboard.is_pressed("s"):
            self.move_player("s")
        elif keyboard.is_pressed("d"):
            self.move_player("d")
        elif keyboard.is_pressed("q"):
            print("Exiting...")
            return False
        return True