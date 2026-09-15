"""
Input validation and direction management.
Demonstrates CSE1021 control structures (selection, conditionals) and vector validation.
"""
from src.config import DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT

# Canonical direction map for text and key bindings
KEY_TO_DIR = {
    'UP': DIR_UP,
    'w': DIR_UP,
    'W': DIR_UP,
    'DOWN': DIR_DOWN,
    's': DIR_DOWN,
    'S': DIR_DOWN,
    'LEFT': DIR_LEFT,
    'a': DIR_LEFT,
    'A': DIR_LEFT,
    'RIGHT': DIR_RIGHT,
    'd': DIR_RIGHT,
    'D': DIR_RIGHT
}

def is_opposite_direction(current_dir, requested_dir):
    """
    Checks if requested_dir is 180 degrees opposite to current_dir.
    Mathematically: two 2D direction vectors are opposite if their component-wise sum is (0, 0).
    Example: DIR_UP (-1, 0) + DIR_DOWN (1, 0) = (0, 0).
    """
    r1, c1 = current_dir
    r2, c2 = requested_dir
    return (r1 + r2 == 0) and (c1 + c2 == 0)

def validate_direction_change(current_dir, requested_dir, snake_len=3):
    """
    Validates a direction change request.
    Rejects direct reversal if snake length > 1 to prevent immediate suicide.
    """
    if requested_dir not in (DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT):
        return current_dir
    
    if snake_len > 1 and is_opposite_direction(current_dir, requested_dir):
        return current_dir
        
    return requested_dir
