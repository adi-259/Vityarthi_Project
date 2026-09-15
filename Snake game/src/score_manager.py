"""
Score tracking and dynamic speed scaling logic.
Demonstrates CSE1021 numerical expressions, threshold checks, and conditional logic.
"""

def calculate_points(base_points, difficulty):
    """
    Returns points awarded per food item based on difficulty setting.
    """
    multiplier_map = {'easy': 1, 'medium': 2, 'hard': 3}
    multiplier = multiplier_map.get(difficulty.lower(), 1)
    return base_points * multiplier

def update_game_speed(current_interval_ms, foods_eaten, speed_increment, min_interval_ms):
    """
    Dynamically increases game speed by shortening the tick interval every 5 foods.
    Clamps to min_interval_ms to maintain playable refresh rates.
    """
    if foods_eaten > 0 and foods_eaten % 5 == 0:
        new_interval = current_interval_ms - speed_increment
        return max(new_interval, min_interval_ms)
    return current_interval_ms
