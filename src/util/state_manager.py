from enum import Enum

class State(Enum):
    MAIN_MENU = 0
    GAME = 1
    PAUSE = 2
    GAME_OVER = 3        



class StateManager:
    def __init__(self):
        self.state = State.MAIN_MENU

    def get_state(self):
        return self.state

    def set_state(self, state: State):
        self.state = state

    def change_state(self, state: State):
        self.state = state

    def is_main_menu(self):
        return self.state == State.MAIN_MENU

    def is_game(self):
        return self.state == State.GAME

    def is_pause(self):
        return self.state == State.PAUSE

    def is_game_over(self):
        return self.state == State.GAME_OVER
