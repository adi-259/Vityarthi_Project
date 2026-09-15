import unittest
from src.collision_engine import check_wall_collision, check_self_collision, evaluate_collision

class TestCollision(unittest.TestCase):
    def test_wall_collision(self):
        rows, cols = 20, 20
        # Valid in-bounds
        self.assertFalse(check_wall_collision((0, 0), rows, cols))
        self.assertFalse(check_wall_collision((19, 19), rows, cols))
        self.assertFalse(check_wall_collision((10, 10), rows, cols))
        
        # Out-of-bounds boundary checks
        self.assertTrue(check_wall_collision((-1, 10), rows, cols))  # Above top
        self.assertTrue(check_wall_collision((20, 10), rows, cols))  # Below bottom
        self.assertTrue(check_wall_collision((10, -1), rows, cols))  # Left
        self.assertTrue(check_wall_collision((10, 20), rows, cols))  # Right

    def test_self_collision(self):
        snake = [(5, 5), (5, 4), (6, 4), (6, 5)]
        # Stepping into neck/body segment
        self.assertTrue(check_self_collision((5, 4), snake, will_grow=False))
        # Empty space
        self.assertFalse(check_self_collision((4, 5), snake, will_grow=False))

    def test_tail_chase_behavior(self):
        # When NOT growing, the tail moves forward, so moving to previous tail coordinate is legal
        snake = [(5, 5), (5, 4), (6, 4), (6, 5)]
        self.assertFalse(check_self_collision((6, 5), snake, will_grow=False))
        # When growing, tail stays, so it IS a collision
        self.assertTrue(check_self_collision((6, 5), snake, will_grow=True))

if __name__ == '__main__':
    unittest.main()
