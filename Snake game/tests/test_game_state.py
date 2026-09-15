import unittest
from src.game_state import GameState, STATE_MENU, STATE_PLAYING, STATE_PAUSED, STATE_GAME_OVER
from src.config import DEFAULT_DIFFICULTY, DIR_RIGHT

class TestGameState(unittest.TestCase):
    def setUp(self):
        self.state = GameState(difficulty=DEFAULT_DIFFICULTY)

    def test_initial_state(self):
        self.assertEqual(self.state.state, STATE_MENU)
        self.assertEqual(self.state.score, 0)
        self.assertEqual(self.state.foods_eaten, 0)
        self.assertEqual(len(self.state.snake), 3)
        self.assertEqual(self.state.direction, DIR_RIGHT)

    def test_reset_game(self):
        self.state.score = 150
        self.state.foods_eaten = 5
        self.state.reset_game()
        self.assertEqual(self.state.state, STATE_PLAYING)
        self.assertEqual(self.state.score, 0)
        self.assertEqual(self.state.foods_eaten, 0)
        self.assertEqual(len(self.state.snake), 3)

    def test_summary_dictionary(self):
        summary = self.state.get_summary_dict()
        self.assertIn('score', summary)
        self.assertIn('foods_eaten', summary)
        self.assertIn('length', summary)
        self.assertIn('difficulty', summary)

if __name__ == '__main__':
    unittest.main()
