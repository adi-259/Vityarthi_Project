"""
File input/output and data persistence module.
Demonstrates CSE1021 file handling, JSON serialization, and defensive error handling.
"""
import json
import os

class PersistenceManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def save_data(self, data):
        """
        Serializes data to a JSON file. Creates parent directories if missing.
        Catches IO errors gracefully to prevent game crash on disk write errors.
        """
        try:
            parent_dir = os.path.dirname(self.filepath)
            if parent_dir and not os.path.exists(parent_dir):
                os.makedirs(parent_dir, exist_ok=True)
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            return True
        except (IOError, OSError) as e:
            print(f"[Persistence Warning] Failed to save data: {e}")
            return False

    def load_data(self):
        """
        Reads data from JSON file. Returns empty list if file does not exist,
        or if content is corrupted/invalid.
        """
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError, OSError) as e:
            print(f"[Persistence Warning] Corrupted or unreadable file ({e}). Initializing empty.")
            return []
