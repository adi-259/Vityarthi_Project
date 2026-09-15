"""
Rendering subsystem for Snake: Algorithm Arena.
Provides dual graphical capabilities:
1. PygameRenderer: Hardware-accelerated 2D graphics with HUD, overlays, and clean styling.
2. TerminalRenderer: Pure text/ASCII renderer for headless or pure CLI execution.
Demonstrates CSE1021 modular design and output formatting.
"""
import sys
from src.config import (
    GRID_ROWS, GRID_COLS, CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT,
    COLOR_BG, COLOR_GRID_LINE, COLOR_HEADER_BG, COLOR_TEXT_PRIMARY,
    COLOR_TEXT_MUTED, COLOR_ACCENT, COLOR_SNAKE_HEAD, COLOR_SNAKE_BODY,
    COLOR_SNAKE_OUTLINE, COLOR_FOOD, COLOR_FOOD_GLOW, COLOR_OVERLAY_BG, COLOR_BORDER
)
from src.game_state import (
    STATE_MENU, STATE_PLAYING, STATE_PAUSED, STATE_GAME_OVER, STATE_LEADERBOARD
)

class PygameRenderer:
    def __init__(self):
        try:
            import pygame
            self.pygame = pygame
            self.pygame.init()
            self.screen = self.pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            self.pygame.display.set_caption("Snake: Algorithm Arena [CSE1021]")
            
            # Fonts
            self.font_title = self.pygame.font.SysFont("Segoe UI, Arial", 32, bold=True)
            self.font_large = self.pygame.font.SysFont("Segoe UI, Arial", 22, bold=True)
            self.font_main = self.pygame.font.SysFont("Segoe UI, Arial", 16)
            self.font_mono = self.pygame.font.SysFont("Consolas, Courier New", 14)
            self.clock = self.pygame.time.Clock()
        except Exception as e:
            raise RuntimeError(f"Pygame initialization failed: {e}")

    def render(self, state, leaderboard_records=None):
        self.screen.fill(COLOR_BG)
        self._draw_header(state)
        self._draw_grid()
        
        if state.food:
            self._draw_food(state.food)
            
        self._draw_snake(state.snake, state.direction)
        
        # State-based overlay rendering
        if state.state == STATE_MENU:
            self._draw_menu_overlay(state)
        elif state.state == STATE_PAUSED:
            self._draw_pause_overlay()
        elif state.state == STATE_GAME_OVER:
            self._draw_game_over_overlay(state)
        elif state.state == STATE_LEADERBOARD:
            self._draw_leaderboard_overlay(leaderboard_records or [])
            
        self.pygame.display.flip()

    def _draw_header(self, state):
        header_rect = self.pygame.Rect(0, 0, WINDOW_WIDTH, 70)
        self.pygame.draw.rect(self.screen, COLOR_HEADER_BG, header_rect)
        self.pygame.draw.line(self.screen, COLOR_BORDER, (0, 70), (WINDOW_WIDTH, 70), 2)
        
        title_surf = self.font_large.render("SNAKE: ALGORITHM ARENA", True, COLOR_ACCENT)
        self.screen.blit(title_surf, (15, 12))
        
        sub_surf = self.font_mono.render(f"CSE1021 Project | Diff: {state.difficulty.upper()}", True, COLOR_TEXT_MUTED)
        self.screen.blit(sub_surf, (15, 42))
        
        # Stats on right
        score_surf = self.font_large.render(f"SCORE: {state.score:04d}", True, COLOR_TEXT_PRIMARY)
        score_x = WINDOW_WIDTH - score_surf.get_width() - 15
        self.screen.blit(score_surf, (score_x, 12))
        
        length_surf = self.font_mono.render(f"Length: {len(state.snake)} | Food: {state.foods_eaten}", True, COLOR_TEXT_MUTED)
        len_x = WINDOW_WIDTH - length_surf.get_width() - 15
        self.screen.blit(length_surf, (len_x, 42))

    def _draw_grid(self):
        for r in range(GRID_ROWS + 1):
            y = 70 + r * CELL_SIZE
            self.pygame.draw.line(self.screen, COLOR_GRID_LINE, (0, y), (WINDOW_WIDTH, y), 1)
        for c in range(GRID_COLS + 1):
            x = c * CELL_SIZE
            self.pygame.draw.line(self.screen, COLOR_GRID_LINE, (x, 70), (x, 70 + GRID_ROWS * CELL_SIZE), 1)

    def _draw_snake(self, snake, direction):
        if not snake:
            return
        
        # Draw body segments
        for r, c in snake[1:]:
            rect = self.pygame.Rect(c * CELL_SIZE + 2, 70 + r * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4)
            self.pygame.draw.rect(self.screen, COLOR_SNAKE_BODY, rect, border_radius=4)
            self.pygame.draw.rect(self.screen, COLOR_SNAKE_OUTLINE, rect, 1, border_radius=4)
            
        # Draw head
        hr, hc = snake[0]
        head_rect = self.pygame.Rect(hc * CELL_SIZE + 1, 70 + hr * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2)
        self.pygame.draw.rect(self.screen, COLOR_SNAKE_HEAD, head_rect, border_radius=6)
        self.pygame.draw.rect(self.screen, COLOR_SNAKE_OUTLINE, head_rect, 2, border_radius=6)
        
        # Eyes
        dr, dc = direction
        cx = hc * CELL_SIZE + CELL_SIZE // 2
        cy = 70 + hr * CELL_SIZE + CELL_SIZE // 2
        eye_color = (20, 20, 20)
        
        # Offset eye positions based on direction vector
        if dc != 0: # Moving horizontally
            eye1 = (cx + dc * 4, cy - 4)
            eye2 = (cx + dc * 4, cy + 4)
        else: # Moving vertically
            eye1 = (cx - 4, cy + dr * 4)
            eye2 = (cx + 4, cy + dr * 4)
        self.pygame.draw.circle(self.screen, eye_color, eye1, 2)
        self.pygame.draw.circle(self.screen, eye_color, eye2, 2)

    def _draw_food(self, food_coord):
        r, c = food_coord
        cx = c * CELL_SIZE + CELL_SIZE // 2
        cy = 70 + r * CELL_SIZE + CELL_SIZE // 2
        radius = (CELL_SIZE // 2) - 3
        # Glow outer circle
        self.pygame.draw.circle(self.screen, COLOR_FOOD_GLOW, (cx, cy), radius + 1)
        # Inner food circle
        self.pygame.draw.circle(self.screen, COLOR_FOOD, (cx, cy), radius)

    def _draw_overlay_box(self, width, height):
        box_x = (WINDOW_WIDTH - width) // 2
        box_y = (WINDOW_HEIGHT - height) // 2
        overlay = self.pygame.Surface((width, height), self.pygame.SRCALPHA)
        overlay.fill((12, 16, 24, 235))
        self.screen.blit(overlay, (box_x, box_y))
        border_rect = self.pygame.Rect(box_x, box_y, width, height)
        self.pygame.draw.rect(self.screen, COLOR_BORDER, border_rect, 2, border_radius=8)
        return box_x, box_y

    def _draw_menu_overlay(self, state):
        bx, by = self._draw_overlay_box(420, 320)
        t = self.font_title.render("SNAKE: ARENA", True, COLOR_ACCENT)
        self.screen.blit(t, (bx + (420 - t.get_width()) // 2, by + 25))
        
        sub = self.font_mono.render("CSE1021 Course Project", True, COLOR_TEXT_MUTED)
        self.screen.blit(sub, (bx + (420 - sub.get_width()) // 2, by + 70))
        
        items = [
            "Press ENTER / SPACE to Start",
            f"Difficulty [1/2/3]: {state.difficulty.upper()}",
            "Press L for Leaderboard",
            "Controls: Arrow Keys or W-A-S-D",
            "P: Pause  |  Q: Quit"
        ]
        y = by + 115
        for item in items:
            color = COLOR_TEXT_PRIMARY if "Start" in item else COLOR_TEXT_MUTED
            text_surf = self.font_main.render(item, True, color)
            self.screen.blit(text_surf, (bx + (420 - text_surf.get_width()) // 2, y))
            y += 35

    def _draw_pause_overlay(self):
        bx, by = self._draw_overlay_box(320, 160)
        t = self.font_title.render("PAUSED", True, (255, 193, 7))
        self.screen.blit(t, (bx + (320 - t.get_width()) // 2, by + 30))
        h = self.font_main.render("Press P or SPACE to Resume", True, COLOR_TEXT_PRIMARY)
        self.screen.blit(h, (bx + (320 - h.get_width()) // 2, by + 85))

    def _draw_game_over_overlay(self, state):
        bx, by = self._draw_overlay_box(380, 260)
        t = self.font_title.render("GAME OVER", True, (244, 67, 54))
        self.screen.blit(t, (bx + (380 - t.get_width()) // 2, by + 20))
        
        reason = self.font_mono.render(state.game_over_reason or "Run Concluded", True, COLOR_TEXT_MUTED)
        self.screen.blit(reason, (bx + (380 - reason.get_width()) // 2, by + 65))
        
        score_txt = self.font_large.render(f"Final Score: {state.score}", True, COLOR_TEXT_PRIMARY)
        self.screen.blit(score_txt, (bx + (380 - score_txt.get_width()) // 2, by + 105))
        
        food_txt = self.font_main.render(f"Foods Eaten: {state.foods_eaten} | Length: {len(state.snake)}", True, COLOR_TEXT_MUTED)
        self.screen.blit(food_txt, (bx + (380 - food_txt.get_width()) // 2, by + 140))
        
        hint = self.font_main.render("Press R to Restart  |  M for Menu", True, COLOR_ACCENT)
        self.screen.blit(hint, (bx + (380 - hint.get_width()) // 2, by + 195))

    def _draw_leaderboard_overlay(self, records):
        bx, by = self._draw_overlay_box(460, 360)
        t = self.font_title.render("HALL OF FAME", True, COLOR_ACCENT)
        self.screen.blit(t, (bx + (460 - t.get_width()) // 2, by + 20))
        
        # Header
        hdr = self.font_mono.render("RK  PLAYER         SCORE   DIFF    FOOD", True, (255, 193, 7))
        self.screen.blit(hdr, (bx + 30, by + 70))
        
        y = by + 100
        if not records:
            empty = self.font_main.render("No scores recorded yet.", True, COLOR_TEXT_MUTED)
            self.screen.blit(empty, (bx + (460 - empty.get_width()) // 2, y + 40))
        else:
            for idx, rec in enumerate(records[:7], start=1):
                p = (rec.get('player', 'Player')[:12]).ljust(14)
                sc = str(rec.get('score', 0)).rjust(5)
                df = str(rec.get('difficulty', 'med')[:4]).ljust(7)
                fd = str(rec.get('foods_eaten', 0)).rjust(4)
                line = f"{idx:02d}  {p} {sc}   {df} {fd}"
                row_surf = self.font_mono.render(line, True, COLOR_TEXT_PRIMARY)
                self.screen.blit(row_surf, (bx + 30, y))
                y += 28
                
        hint = self.font_main.render("Press ESC or M to Return to Menu", True, COLOR_TEXT_MUTED)
        self.screen.blit(hint, (bx + (460 - hint.get_width()) // 2, by + 315))


class TerminalRenderer:
    """ASCII Terminal renderer for headless or pure command line verification."""
    def __init__(self, rows=GRID_ROWS, cols=GRID_COLS):
        self.rows = rows
        self.cols = cols

    def render_frame(self, state):
        occupied_body = set(state.snake[1:])
        head = state.snake[0]
        
        border_top = "+" + "---" * self.cols + "+"
        lines = [
            f"[SNAKE: ALGORITHM ARENA - CLI MODE] Score: {state.score:03d} | Food: {state.foods_eaten} | Diff: {state.difficulty}",
            border_top
        ]
        
        for r in range(self.rows):
            row_chars = []
            for c in range(self.cols):
                coord = (r, c)
                if coord == head:
                    row_chars.append(" O ")
                elif coord in occupied_body:
                    row_chars.append(" o ")
                elif coord == state.food:
                    row_chars.append(" * ")
                else:
                    row_chars.append(" . ")
            lines.append("|" + "".join(row_chars) + "|")
            
        lines.append(border_top)
        return "\n".join(lines)
