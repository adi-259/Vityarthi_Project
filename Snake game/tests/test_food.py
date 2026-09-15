import unittest
from src.food_manager import FoodManager

class TestFood(unittest.TestCase):
    def test_available_cells_filter(self):
        fm = FoodManager()
        rows, cols = 3, 3
        occupied = [(0, 0), (0, 1), (0, 2)]
        avail = fm.get_available_cells(rows, cols, occupied)
        self.assertEqual(len(avail), 6)
        for cell in occupied:
            self.assertNotIn(cell, avail)

    def test_spawn_avoids_occupied(self):
        fm = FoodManager(seed=123)
        rows, cols = 5, 5
        occupied = [(0, 0), (0, 1), (0, 2)]
        for _ in range(20):
            food = fm.spawn_food(rows, cols, occupied)
            self.assertNotIn(food, occupied)
            self.assertTrue(0 <= food[0] < rows)
            self.assertTrue(0 <= food[1] < cols)

    def test_board_full_handling(self):
        fm = FoodManager()
        rows, cols = 2, 2
        all_cells = [(0, 0), (0, 1), (1, 0), (1, 1)]
        food = fm.spawn_food(rows, cols, all_cells)
        self.assertIsNone(food)

    def test_seed_reproducibility(self):
        fm1 = FoodManager(seed=999)
        fm2 = FoodManager(seed=999)
        coords1 = [fm1.spawn_food(20, 20, []) for _ in range(10)]
        coords2 = [fm2.spawn_food(20, 20, []) for _ in range(10)]
        self.assertEqual(coords1, coords2)

if __name__ == '__main__':
    unittest.main()
