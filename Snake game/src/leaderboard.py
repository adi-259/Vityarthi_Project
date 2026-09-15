"""
Leaderboard management and explicit sorting algorithm.
Demonstrates CSE1021 dictionary data structures, list processing, and Insertion Sort.
"""
from src.config import MAX_LEADERBOARD_ENTRIES

def insertion_sort_scores(records):
    """
    Explicit implementation of Insertion Sort to rank records by score descending.
    Fulfills CSE1021 sorting algorithm syllabus requirements.
    
    Algorithm:
    - Maintains a sorted prefix of elements.
    - For each item from index 1 to n-1, shifts smaller scores rightward
      to insert current record in its correct ranked position.
      
    Complexity Analysis:
    - Best Case: O(n) when input list is already sorted descending.
    - Worst Case: O(n^2) when input is reverse-sorted ascending.
    - Space Complexity: O(1) auxiliary space (in-place rearrangement).
    Ideal for leaderboard where n <= 20 entries.
    """
    n = len(records)
    for i in range(1, n):
        key = records[i]
        j = i - 1
        # Descending sort: shift items where previous score is less than current score
        while j >= 0 and records[j]['score'] < key['score']:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records

class Leaderboard:
    def __init__(self, persistence_manager, max_entries=MAX_LEADERBOARD_ENTRIES):
        self.persistence = persistence_manager
        self.max_entries = max_entries
        self.records = self.load()

    def load(self):
        """Loads and sorts existing leaderboard records."""
        data = self.persistence.load_data()
        if isinstance(data, list):
            return insertion_sort_scores(data)[:self.max_entries]
        return []

    def add_entry(self, player_name, score, difficulty, foods_eaten):
        """
        Inserts a new game run record and sorts the leaderboard.
        Trims to max_entries and persists to storage.
        """
        entry = {
            "player": str(player_name).strip() or "Player",
            "score": int(score),
            "difficulty": str(difficulty),
            "foods_eaten": int(foods_eaten)
        }
        self.records.append(entry)
        self.records = insertion_sort_scores(self.records)[:self.max_entries]
        self.persistence.save_data(self.records)
        return self.records

    def get_top_records(self):
        """Returns the sorted list of top score records."""
        return self.records
