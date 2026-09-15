"""
Configuration constants and settings for Snake: Algorithm Arena.
Maps directly to CSE1021 primitive types, variables, and dictionary structures.
"""
import os

# Board Dimensions (grid cells)
GRID_ROWS = 20
GRID_COLS = 20
CELL_SIZE = 28

# Screen / Window Settings
WINDOW_WIDTH = GRID_COLS * CELL_SIZE
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE + 70  # extra 70px for status HUD header

# Movement Direction Vectors: (row_delta, col_delta)
DIR_UP = (-1, 0)
DIR_DOWN = (1, 0)
DIR_LEFT = (0, -1)
DIR_RIGHT = (0, 1)

# Difficulty settings: update tick intervals (in milliseconds)
DIFFICULTY_CONFIG = {
    'easy': {
        'tick_interval_ms': 150,
        'points_per_food': 10,
        'speed_increment': 2,
        'min_interval_ms': 80
    },
    'medium': {
        'tick_interval_ms': 110,
        'points_per_food': 20,
        'speed_increment': 3,
        'min_interval_ms': 60
    },
    'hard': {
        'tick_interval_ms': 75,
        'points_per_food': 30,
        'speed_increment': 4,
        'min_interval_ms': 45
    }
}

DEFAULT_DIFFICULTY = 'medium'

# Color Palette (RGB tuples)
COLOR_BG = (18, 22, 28)
COLOR_GRID_LINE = (28, 34, 44)
COLOR_HEADER_BG = (12, 15, 20)
COLOR_TEXT_PRIMARY = (235, 240, 245)
COLOR_TEXT_MUTED = (140, 150, 165)
COLOR_ACCENT = (76, 175, 80)
COLOR_SNAKE_HEAD = (102, 187, 106)
COLOR_SNAKE_BODY = (67, 160, 71)
COLOR_SNAKE_OUTLINE = (27, 94, 32)
COLOR_FOOD = (239, 83, 80)
COLOR_FOOD_GLOW = (255, 138, 128)
COLOR_OVERLAY_BG = (10, 14, 20)
COLOR_BORDER = (45, 55, 72)

# File Paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
LEADERBOARD_FILE = os.path.join(DATA_DIR, "leaderboard.json")
MAX_LEADERBOARD_ENTRIES = 10
