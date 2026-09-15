"""
Food placement and grid cell management.
Demonstrates CSE1021 lists, sets, list comprehensions, and pseudo-random generation (Unit IV).
"""
import random

class FoodManager:
    def __init__(self, seed=None):
        # We maintain a dedicated PRNG instance so seeded tests are completely isolated
        self.rng = random.Random(seed) if seed is not None else random.Random()

    def set_seed(self, seed):
        """Allows resetting the PRNG seed dynamically for deterministic validation."""
        self.rng = random.Random(seed)

    def get_available_cells(self, rows, cols, occupied_cells):
        """
        Computes the set difference between all board coordinates and occupied cells.
        Uses a set for O(1) membership lookups during candidate filtering.
        Time Complexity: O(R * C)
        """
        occupied_set = set(occupied_cells)
        available = []
        for r in range(rows):
            for c in range(cols):
                coord = (r, c)
                if coord not in occupied_set:
                    available.append(coord)
        return available

    def spawn_food(self, rows, cols, occupied_cells):
        """
        Selects a random unoccupied cell for the next food item.
        Returns: (row, col) tuple, or None if the board is completely full (win condition).
        """
        available = self.get_available_cells(rows, cols, occupied_cells)
        if not available:
            return None
        return self.rng.choice(available)
