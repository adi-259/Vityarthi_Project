"""
State model for Snake: Algorithm Arena.
Demonstrates CSE1021 compound data types:
- Lists: mutable snake body coordinates
- Tuples: immutable (row, col) grid coordinates
- Dictionaries: state metadata, configurations, and summaries
"""
from src.config import (
    GRID_ROWS, GRID_COLS, DIR_RIGHT,
    DIFFICULTY_CONFIG, DEFAULT_DIFFICULTY
)

# Game lifecycle states
STATE_MENU = "MENU"
STATE_PLAYING = "PLAYING"
STATE_PAUSED = "PAUSED"
STATE_GAME_OVER = "GAME_OVER"
STATE_LEADERBOARD = "LEADERBOARD"

class GameState:
    def __init__(self, difficulty=DEFAULT_DIFFICULTY, seed=None):
        self.difficulty = difficulty if difficulty in DIFFICULTY_CONFIG else DEFAULT_DIFFICULTY
        self.seed = seed
        self.state = STATE_MENU
        self.score = 0
        self.foods_eaten = 0
        self.game_over_reason = ""
        
        # Difficulty configuration values
        diff_cfg = DIFFICULTY_CONFIG[self.difficulty]
        self.tick_interval_ms = diff_cfg['tick_interval_ms']
        self.points_per_food = diff_cfg['points_per_food']
        self.speed_increment = diff_cfg['speed_increment']
        self.min_interval_ms = diff_cfg['min_interval_ms']
        
        # Movement & grid state
        self.direction = DIR_RIGHT
        self.next_direction = DIR_RIGHT
        
        # Snake body represented as list of (row, col) coordinate tuples
        # Initial position: centered horizontally with length 3
        mid_row = GRID_ROWS // 2
        mid_col = GRID_COLS // 2
        self.snake = [
            (mid_row, mid_col),
            (mid_row, mid_col - 1),
            (mid_row, mid_col - 2)
        ]
        
        self.food = None

    def reset_game(self):
        """Resets dynamic game variables for a fresh run while preserving settings."""
        diff_cfg = DIFFICULTY_CONFIG[self.difficulty]
        self.tick_interval_ms = diff_cfg['tick_interval_ms']
        self.score = 0
        self.foods_eaten = 0
        self.game_over_reason = ""
        self.direction = DIR_RIGHT
        self.next_direction = DIR_RIGHT
        
        mid_row = GRID_ROWS // 2
        mid_col = GRID_COLS // 2
        self.snake = [
            (mid_row, mid_col),
            (mid_row, mid_col - 1),
            (mid_row, mid_col - 2)
        ]
        self.food = None
        self.state = STATE_PLAYING

    def get_summary_dict(self):
        """Returns run statistics as a dictionary for reporting and persistence."""
        return {
            "score": self.score,
            "foods_eaten": self.foods_eaten,
            "length": len(self.snake),
            "difficulty": self.difficulty,
            "reason": self.game_over_reason
        }
