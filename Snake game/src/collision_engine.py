"""
Collision detection algorithms for Snake: Algorithm Arena.
Demonstrates boundary condition checks and set/list membership testing.
"""

def check_wall_collision(coord, rows, cols):
    """
    Verifies if coord (row, col) is outside valid grid boundaries [0, rows) x [0, cols).
    Time Complexity: O(1)
    """
    r, c = coord
    return r < 0 or r >= rows or c < 0 or c >= cols

def check_self_collision(next_head, snake_body, will_grow=False):
    """
    Checks if next_head collides with any part of the snake body.
    If will_grow is False, the tail will pop forward on this tick,
    so moving into the current tail position is technically valid.
    Otherwise, collision is checked against all segments.
    Time Complexity: O(n) where n = len(snake_body)
    """
    if will_grow:
        return next_head in snake_body
    else:
        # Check against body segments excluding the trailing tail that will vacate
        return next_head in snake_body[:-1]

def evaluate_collision(next_head, snake_body, rows, cols, is_eating=False):
    """
    Unified collision evaluation.
    Returns: (has_collided: bool, reason: str)
    """
    if check_wall_collision(next_head, rows, cols):
        return True, "Wall collision: Boundary exceeded"
    
    if check_self_collision(next_head, snake_body, will_grow=is_eating):
        return True, "Self collision: Ran into own body"
        
    return False, ""
