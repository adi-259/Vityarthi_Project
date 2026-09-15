import unittest
from src.score_manager import calculate_points, update_game_speed

class TestScore(unittest.TestCase):
    def test_point_multipliers(self):
        self.assertEqual(calculate_points(10, 'easy'), 10)
        self.assertEqual(calculate_points(10, 'medium'), 20)
        self.assertEqual(calculate_points(10, 'hard'), 30)

    def test_dynamic_speed_scaling(self):
        initial_speed = 100
        # At foods_eaten = 4, no acceleration yet
        s1 = update_game_speed(initial_speed, foods_eaten=4, speed_increment=5, min_interval_ms=50)
        self.assertEqual(s1, 100)
        
        # At foods_eaten = 5 (multiple of 5), speed accelerates (tick interval decreases)
        s2 = update_game_speed(initial_speed, foods_eaten=5, speed_increment=5, min_interval_ms=50)
        self.assertEqual(s2, 95)

    def test_speed_clamping_at_minimum(self):
        # Clamps to min_interval_ms (50ms)
        s = update_game_speed(52, foods_eaten=10, speed_increment=5, min_interval_ms=50)
        self.assertEqual(s, 50)

if __name__ == '__main__':
    unittest.main()
