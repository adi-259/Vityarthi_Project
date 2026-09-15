import unittest
import os
import tempfile
from src.leaderboard import insertion_sort_scores, Leaderboard
from src.persistence import PersistenceManager

class TestLeaderboard(unittest.TestCase):
    def test_insertion_sort_order(self):
        data = [
            {'player': 'P1', 'score': 100},
            {'player': 'P2', 'score': 500},
            {'player': 'P3', 'score': 250},
            {'player': 'P4', 'score': 50}
        ]
        sorted_records = insertion_sort_scores(data)
        scores = [r['score'] for r in sorted_records]
        self.assertEqual(scores, [500, 250, 100, 50])

    def test_insertion_sort_with_duplicates(self):
        data = [
            {'player': 'A', 'score': 200},
            {'player': 'B', 'score': 200},
            {'player': 'C', 'score': 400}
        ]
        sorted_records = insertion_sort_scores(data)
        scores = [r['score'] for r in sorted_records]
        self.assertEqual(scores, [400, 200, 200])

    def test_leaderboard_persistence(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_file = os.path.join(tmpdir, "test_scores.json")
            pm = PersistenceManager(temp_file)
            lb = Leaderboard(pm, max_entries=3)
            
            lb.add_entry("Alice", 100, "medium", 5)
            lb.add_entry("Bob", 300, "medium", 15)
            lb.add_entry("Charlie", 200, "medium", 10)
            lb.add_entry("Dave", 50, "medium", 2)
            
            top = lb.get_top_records()
            self.assertEqual(len(top), 3) # limited to max_entries 3
            self.assertEqual(top[0]['player'], "Bob")
            self.assertEqual(top[0]['score'], 300)
            self.assertEqual(top[1]['player'], "Charlie")
            self.assertEqual(top[2]['player'], "Alice")

if __name__ == '__main__':
    unittest.main()
