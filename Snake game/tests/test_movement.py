import unittest
from src.config import DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT
from src.snake_engine import compute_next_head, advance_snake
from src.input_controller import validate_direction_change, is_opposite_direction

class TestMovement(unittest.TestCase):
    def test_compute_next_head(self):
        head = (10, 10)
        self.assertEqual(compute_next_head(head, DIR_UP), (9, 10))
        self.assertEqual(compute_next_head(head, DIR_DOWN), (11, 10))
        self.assertEqual(compute_next_head(head, DIR_LEFT), (10, 9))
        self.assertEqual(compute_next_head(head, DIR_RIGHT), (10, 11))

    def test_advance_without_growth(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        next_head = (5, 6)
        advance_snake(snake, next_head, is_eating_food=False)
        self.assertEqual(len(snake), 3)
        self.assertEqual(snake[0], (5, 6))
        self.assertEqual(snake[1], (5, 5))
        self.assertEqual(snake[2], (5, 4))

    def test_advance_with_growth(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        next_head = (5, 6)
        advance_snake(snake, next_head, is_eating_food=True)
        self.assertEqual(len(snake), 4)
        self.assertEqual(snake[0], (5, 6))
        self.assertEqual(snake[-1], (5, 3))

    def test_reversal_rejection(self):
        self.assertTrue(is_opposite_direction(DIR_UP, DIR_DOWN))
        self.assertTrue(is_opposite_direction(DIR_LEFT, DIR_RIGHT))
        self.assertFalse(is_opposite_direction(DIR_UP, DIR_LEFT))
        
        # When moving RIGHT, direct reverse to LEFT must be ignored
        res = validate_direction_change(DIR_RIGHT, DIR_LEFT, snake_len=3)
        self.assertEqual(res, DIR_RIGHT)
        
        # Turn to UP should be accepted
        res = validate_direction_change(DIR_RIGHT, DIR_UP, snake_len=3)
        self.assertEqual(res, DIR_UP)

if __name__ == '__main__':
    unittest.main()
