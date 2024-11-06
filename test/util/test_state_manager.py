import unittest

from src.util.state_manager import StateManager, State

class TestStateManager(unittest.TestCase):
    
    def setUp(self):
        self.state_manager = StateManager()
    def tearDown(self):
        # print("tearDown")
        pass

    def test_get_state(self):
        self.assertEqual(self.state_manager.get_state(), State.MAIN_MENU)
        self.assertEqual(self.state_manager.state, State.MAIN_MENU)

    def test_set_state(self):
        self.state_manager.set_state(State.GAME)
        self.assertEqual(self.state_manager.state, State.GAME)
        self.state_manager.set_state(State.PAUSE)
        self.assertEqual(self.state_manager.state, State.PAUSE)
        self.state_manager.set_state(State.GAME_OVER)
        self.assertEqual(self.state_manager.state, State.GAME_OVER)
        self.state_manager.set_state(State.MAIN_MENU)
        self.assertEqual(self.state_manager.state, State.MAIN_MENU)

    def test_change_state(self):
        self.state_manager.change_state(State.GAME)
        self.assertEqual(self.state_manager.state, State.GAME)
        self.state_manager.change_state(State.PAUSE)
        self.assertEqual(self.state_manager.state, State.PAUSE)
        self.state_manager.change_state(State.GAME_OVER)
        self.assertEqual(self.state_manager.state, State.GAME_OVER)
        self.state_manager.change_state(State.MAIN_MENU)
        self.assertEqual(self.state_manager.state, State.MAIN_MENU)

    def test_is_main_menu(self):
        self.assertTrue(self.state_manager.is_main_menu())
        self.state_manager.change_state(State.GAME)
        self.assertFalse(self.state_manager.is_main_menu())
        self.state_manager.change_state(State.PAUSE)
        self.assertFalse(self.state_manager.is_main_menu())
        self.state_manager.change_state(State.GAME_OVER)
        self.assertFalse(self.state_manager.is_main_menu())

    def test_is_game(self):
        self.assertFalse(self.state_manager.is_game())
        self.state_manager.change_state(State.GAME)
        self.assertTrue(self.state_manager.is_game())
        self.state_manager.change_state(State.PAUSE)
        self.assertFalse(self.state_manager.is_game())
        self.state_manager.change_state(State.GAME_OVER)
        self.assertFalse(self.state_manager.is_game())

    def test_is_pause(self):
        self.assertFalse(self.state_manager.is_pause())
        self.state_manager.change_state(State.GAME)
        self.assertFalse(self.state_manager.is_pause())
        self.state_manager.change_state(State.PAUSE)
        self.assertTrue(self.state_manager.is_pause())
        self.state_manager.change_state(State.GAME_OVER)
        self.assertFalse(self.state_manager.is_pause())

    def test_is_game_over(self):
        self.assertFalse(self.state_manager.is_game_over())
        self.state_manager.change_state(State.GAME)
        self.assertFalse(self.state_manager.is_game_over())
        self.state_manager.change_state(State.PAUSE)
        self.assertFalse(self.state_manager.is_game_over())
        self.state_manager.change_state(State.GAME_OVER)
        self.assertTrue(self.state_manager.is_game_over())

if __name__ == "__main__":
    unittest.main(verbosity=2)