"""
Core snake mechanics: movement, coordinate calculation, and body growth.
Demonstrates CSE1021 list manipulations (insert, pop) and tuple calculations.
"""

def compute_next_head(current_head, direction):
    """
    Calculates candidate next head coordinate using vector addition:
    next_head = (row + dir_row, col + dir_col)
    """
    r, c = current_head
    dr, dc = direction
    return (r + dr, c + dc)

def advance_snake(snake_body, next_head, is_eating_food):
    """
    Advances the snake grid coordinates by one discrete time-step.
    - Inserts new head at index 0: O(n) in python list.
    - If food is consumed, tail is retained (growth occurs).
    - If food is not consumed, tail element is popped to maintain length.
    Returns: None (mutates snake_body in place)
    """
    snake_body.insert(0, next_head)
    if not is_eating_food:
        snake_body.pop()
