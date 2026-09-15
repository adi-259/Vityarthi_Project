"""
Snake: Algorithm Arena
CSE1021 Evaluated Course Project - Main Entry Point

Demonstrates:
- Command-line argument parsing (argparse)
- Modular system integration across 10 distinct source files
- Headless automated self-testing without GUI dependencies
- Hardware-accelerated 2D Pygame rendering and interactive Terminal CLI mode
"""
import sys
import os
import argparse
import time

# Ensure project root is in python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import (
    GRID_ROWS, GRID_COLS, DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT,
    DEFAULT_DIFFICULTY, DIFFICULTY_CONFIG, LEADERBOARD_FILE
)
from src.game_state import (
    GameState, STATE_MENU, STATE_PLAYING, STATE_PAUSED,
    STATE_GAME_OVER, STATE_LEADERBOARD
)
from src.input_controller import validate_direction_change
from src.snake_engine import compute_next_head, advance_snake
from src.collision_engine import evaluate_collision
from src.food_manager import FoodManager
from src.score_manager import calculate_points, update_game_speed
from src.leaderboard import Leaderboard
from src.persistence import PersistenceManager
# WSGI entrypoint for Vercel serverless functions if deployed directly
def app(environ, start_response):
    from api.index import app as wsgi_app
    return wsgi_app(environ, start_response)

def run_headless_simulation(ticks=50, seed=42):
    """
    Simulates a multi-step game in memory without any graphical display.
    Demonstrates deterministic simulation, collision handling, and scoring.
    """
    state = GameState(difficulty='medium', seed=seed)
    food_mgr = FoodManager(seed=seed)
    state.reset_game()
    state.food = food_mgr.spawn_food(GRID_ROWS, GRID_COLS, state.snake)
    
    # Run simulation forward
    for step in range(ticks):
        if state.state != STATE_PLAYING:
            break
        next_head = compute_next_head(state.snake[0], state.direction)
        is_eating = (next_head == state.food)
        collided, reason = evaluate_collision(next_head, state.snake, GRID_ROWS, GRID_COLS, is_eating)
        
        if collided:
            state.state = STATE_GAME_OVER
            state.game_over_reason = reason
            break
            
        advance_snake(state.snake, next_head, is_eating)
        if is_eating:
            state.score += calculate_points(state.points_per_food, state.difficulty)
            state.foods_eaten += 1
            state.food = food_mgr.spawn_food(GRID_ROWS, GRID_COLS, state.snake)
            
    return state

def run_self_test(seed=42):
    """
    Executes automated unit and integration tests headlessly.
    Produces structured validation report matching VITyarthi verification rubric.
    """
    print("=" * 65)
    print("  CSE1021 VITyarthi Project: Snake - Algorithm Arena")
    print("  Automated Headless Test Suite & Traceability Verification")
    print("=" * 65)
    
    passed_count = 0
    total_tests = 0
    
    def test_case(test_id, req_id, desc, assertion):
        nonlocal passed_count, total_tests
        total_tests += 1
        status = "PASS" if assertion else "FAIL"
        if assertion:
            passed_count += 1
        print(f"[{status}] {test_id:8s} | {req_id:6s} | {desc}")
        return assertion

    # Test 1: Grid boundary collision
    from src.collision_engine import check_wall_collision
    test_case("TC-01", "FR-07", "Detect top boundary wall collision (-1, 5)", check_wall_collision((-1, 5), 20, 20) is True)
    test_case("TC-02", "FR-07", "Detect right boundary wall collision (5, 20)", check_wall_collision((5, 20), 20, 20) is True)
    test_case("TC-03", "FR-07", "Accept valid in-bound coordinate (10, 10)", check_wall_collision((10, 10), 20, 20) is False)

    # Test 2: Direction reversal rejection
    from src.input_controller import validate_direction_change
    d1 = validate_direction_change(DIR_RIGHT, DIR_LEFT, snake_len=3)
    test_case("TC-04", "FR-03", "Reject immediate reverse when moving RIGHT (DIR_LEFT ignored)", d1 == DIR_RIGHT)
    d2 = validate_direction_change(DIR_RIGHT, DIR_UP, snake_len=3)
    test_case("TC-05", "FR-02", "Permit 90-degree turn when moving RIGHT (DIR_UP accepted)", d2 == DIR_UP)

    # Test 3: Self-collision detection
    from src.collision_engine import check_self_collision
    snake = [(5, 5), (5, 4), (6, 4), (6, 5)]
    test_case("TC-06", "FR-08", "Detect head entering occupied body segment", check_self_collision((5, 4), snake, False) is True)
    test_case("TC-07", "FR-08", "Allow movement into empty cell adjacent to body", check_self_collision((5, 6), snake, False) is False)

    # Test 4: Seeded PRNG food placement reproducibility
    fm1 = FoodManager(seed=seed)
    fm2 = FoodManager(seed=seed)
    food_seq1 = [fm1.spawn_food(20, 20, [(10, 10)]) for _ in range(5)]
    food_seq2 = [fm2.spawn_food(20, 20, [(10, 10)]) for _ in range(5)]
    test_case("TC-08", "FR-15", f"Seeded PRNG (seed={seed}) produces identical food coordinates", food_seq1 == food_seq2)

    # Test 5: Food not placed on occupied cells
    test_occupied = [(r, c) for r in range(19) for c in range(20)] # All but row 19 occupied
    f_coord = fm1.spawn_food(20, 20, test_occupied)
    test_case("TC-09", "FR-05", "Spawned food strictly avoids all occupied coordinates", f_coord not in test_occupied and f_coord[0] == 19)

    # Test 6: Movement advancement and growth
    body = [(10, 10), (10, 9), (10, 8)]
    advance_snake(body, (10, 11), is_eating_food=False)
    test_case("TC-10", "FR-04", "Advance snake without food maintains constant length (3)", len(body) == 3 and body[0] == (10, 11))
    advance_snake(body, (10, 12), is_eating_food=True)
    test_case("TC-11", "FR-06", "Advance snake with food increases length (4)", len(body) == 4 and body[0] == (10, 12))

    # Test 7: Explicit Insertion Sort for leaderboard ranking
    from src.leaderboard import insertion_sort_scores
    unsorted_data = [
        {"player": "Alice", "score": 120},
        {"player": "Bob", "score": 350},
        {"player": "Charlie", "score": 210},
        {"player": "Dave", "score": 500}
    ]
    sorted_data = insertion_sort_scores(unsorted_data)
    expected_order = [500, 350, 210, 120]
    actual_order = [r["score"] for r in sorted_data]
    test_case("TC-12", "FR-12", "Insertion sort orders score records in descending sequence", actual_order == expected_order)

    # Test 8: End-to-end headless simulation
    sim_state = run_headless_simulation(ticks=40, seed=seed)
    test_case("TC-13", "FR-14", "Headless multi-tick simulation runs to completion safely", sim_state is not None)

    print("-" * 65)
    print(f"Results: {passed_count}/{total_tests} tests passed ({passed_count/total_tests*100:.1f}%)")
    print("=" * 65)
    return passed_count == total_tests

def run_cli_game(seed=None, difficulty=DEFAULT_DIFFICULTY):
    """
    Playable turn-based terminal mode for interactive execution without GUI libraries.
    """
    renderer = TerminalRenderer(GRID_ROWS, GRID_COLS)
    state = GameState(difficulty=difficulty, seed=seed)
    food_mgr = FoodManager(seed=seed)
    state.reset_game()
    state.food = food_mgr.spawn_food(GRID_ROWS, GRID_COLS, state.snake)
    
    print("\n--- Starting Terminal CLI Mode ---")
    print("Controls: W (Up), S (Down), A (Left), D (Right), Q (Quit), Press Enter after each command.\n")
    
    while state.state == STATE_PLAYING:
        print(renderer.render_frame(state))
        try:
            cmd = input("Move [WASD/Q]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break
            
        if cmd == 'q':
            print("Game exited by user.")
            break
            
        key_dir = {'w': DIR_UP, 's': DIR_DOWN, 'a': DIR_LEFT, 'd': DIR_RIGHT}.get(cmd)
        if key_dir:
            state.direction = validate_direction_change(state.direction, key_dir, len(state.snake))
            
        next_head = compute_next_head(state.snake[0], state.direction)
        is_eating = (next_head == state.food)
        collided, reason = evaluate_collision(next_head, state.snake, GRID_ROWS, GRID_COLS, is_eating)
        
        if collided:
            state.state = STATE_GAME_OVER
            state.game_over_reason = reason
            print(f"\n*** GAME OVER: {reason} ***")
            print(f"Final Score: {state.score} | Length: {len(state.snake)}\n")
            break
            
        advance_snake(state.snake, next_head, is_eating)
        if is_eating:
            state.score += calculate_points(state.points_per_food, state.difficulty)
            state.foods_eaten += 1
            state.food = food_mgr.spawn_food(GRID_ROWS, GRID_COLS, state.snake)

def run_graphical_game(seed=None, difficulty=DEFAULT_DIFFICULTY):
    """
    Hardware-accelerated Pygame interactive mode.
    """
    try:
        from src.renderer import PygameRenderer
        import pygame
    except ImportError:
        print("[ERROR] Pygame is not installed. Run 'pip install -r requirements.txt' or use '--cli-mode'.")
        sys.exit(1)
        
    renderer = PygameRenderer()
    persistence = PersistenceManager(LEADERBOARD_FILE)
    leaderboard = Leaderboard(persistence)
    food_mgr = FoodManager(seed=seed)
    
    state = GameState(difficulty=difficulty, seed=seed)
    clock = pygame.time.Clock()
    last_tick_time = pygame.time.get_ticks()
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        
        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if state.state == STATE_MENU:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        state.reset_game()
                        state.food = food_mgr.spawn_food(GRID_ROWS, GRID_COLS, state.snake)
                    elif event.key == pygame.K_1:
                        state.difficulty = 'easy'
                    elif event.key == pygame.K_2:
                        state.difficulty = 'medium'
                    elif event.key == pygame.K_3:
                        state.difficulty = 'hard'
                    elif event.key == pygame.K_l:
                        state.state = STATE_LEADERBOARD
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        running = False
                        
                elif state.state == STATE_PLAYING:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        state.next_direction = validate_direction_change(state.direction, DIR_UP, len(state.snake))
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        state.next_direction = validate_direction_change(state.direction, DIR_DOWN, len(state.snake))
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        state.next_direction = validate_direction_change(state.direction, DIR_LEFT, len(state.snake))
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        state.next_direction = validate_direction_change(state.direction, DIR_RIGHT, len(state.snake))
                    elif event.key in (pygame.K_p, pygame.K_SPACE):
                        state.state = STATE_PAUSED
                    elif event.key == pygame.K_ESCAPE:
                        state.state = STATE_MENU
                        
                elif state.state == STATE_PAUSED:
                    if event.key in (pygame.K_p, pygame.K_SPACE):
                        state.state = STATE_PLAYING
                        last_tick_time = current_time # Prevent instant multi-tick catch-up
                    elif event.key == pygame.K_ESCAPE:
                        state.state = STATE_MENU
                        
                elif state.state == STATE_GAME_OVER:
                    if event.key == pygame.K_r:
                        state.reset_game()
                        state.food = food_mgr.spawn_food(GRID_ROWS, GRID_COLS, state.snake)
                    elif event.key in (pygame.K_m, pygame.K_ESCAPE):
                        state.state = STATE_MENU
                        
                elif state.state == STATE_LEADERBOARD:
                    if event.key in (pygame.K_ESCAPE, pygame.K_m, pygame.K_RETURN):
                        state.state = STATE_MENU

        # Gameplay Tick Update
        if state.state == STATE_PLAYING:
            if current_time - last_tick_time >= state.tick_interval_ms:
                last_tick_time = current_time
                state.direction = state.next_direction
                
                next_head = compute_next_head(state.snake[0], state.direction)
                is_eating = (next_head == state.food)
                collided, reason = evaluate_collision(next_head, state.snake, GRID_ROWS, GRID_COLS, is_eating)
                
                if collided:
                    state.state = STATE_GAME_OVER
                    state.game_over_reason = reason
                    if state.score > 0:
                        leaderboard.add_entry("Player", state.score, state.difficulty, state.foods_eaten)
                else:
                    advance_snake(state.snake, next_head, is_eating)
                    if is_eating:
                        state.score += calculate_points(state.points_per_food, state.difficulty)
                        state.foods_eaten += 1
                        state.tick_interval_ms = update_game_speed(
                            state.tick_interval_ms, state.foods_eaten,
                            state.speed_increment, state.min_interval_ms
                        )
                        state.food = food_mgr.spawn_food(GRID_ROWS, GRID_COLS, state.snake)
                        if state.food is None: # Board full
                            state.state = STATE_GAME_OVER
                            state.game_over_reason = "Victory: Board Completely Cleared!"
                            leaderboard.add_entry("Winner", state.score, state.difficulty, state.foods_eaten)

        # Render current frame
        renderer.render(state, leaderboard.get_top_records())
        clock.tick(60)

    pygame.quit()

def main():
    parser = argparse.ArgumentParser(
        description="Snake: Algorithm Arena - CSE1021 Evaluated Course Project"
    )
    parser.add_argument("--self-test", action="store_true", help="Run automated headless unit/integration test suite")
    parser.add_argument("--seed", type=int, default=None, help="Set random seed for deterministic food generation")
    parser.add_argument("--cli-mode", action="store_true", help="Launch turn-based text CLI mode without GUI")
    parser.add_argument("--difficulty", choices=['easy', 'medium', 'hard'], default=DEFAULT_DIFFICULTY, help="Game difficulty preset")
    args = parser.parse_args()

    if args.self_test:
        success = run_self_test(seed=args.seed if args.seed is not None else 42)
        sys.exit(0 if success else 1)
    elif args.cli_mode:
        run_cli_game(seed=args.seed, difficulty=args.difficulty)
    else:
        run_graphical_game(seed=args.seed, difficulty=args.difficulty)

if __name__ == "__main__":
    main()
