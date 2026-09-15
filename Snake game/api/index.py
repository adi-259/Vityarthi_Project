import os
import sys
import json
from http.server import BaseHTTPRequestHandler

# Add root directory to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.leaderboard import insertion_sort_scores

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake: Algorithm Arena | VIT Bhopal CSE1021</title>
    <style>
        :root {
            --bg-color: #0d1117;
            --card-bg: #161b22;
            --border-color: #30363d;
            --accent-green: #2ea043;
            --accent-glow: #3fb950;
            --text-primary: #f0f6fc;
            --text-muted: #8b949e;
            --food-color: #f85149;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-primary); display: flex; flex-direction: column; align-items: center; min-height: 100vh; padding: 20px; }
        header { text-align: center; margin-bottom: 24px; max-width: 800px; }
        h1 { font-size: 2.2rem; color: var(--accent-glow); margin-bottom: 6px; letter-spacing: 1px; }
        p.subtitle { color: var(--text-muted); font-size: 0.95rem; }
        .badge { display: inline-block; background: #21262d; border: 1px solid var(--border-color); border-radius: 12px; padding: 3px 12px; font-size: 0.8rem; margin-top: 8px; color: #58a6ff; }
        .main-container { display: flex; flex-wrap: wrap; gap: 24px; justify-content: center; max-width: 1000px; width: 100%; }
        .game-card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; align-items: center; }
        .hud { display: flex; justify-content: space-between; width: 100%; max-width: 420px; margin-bottom: 12px; font-weight: 600; font-size: 1.1rem; }
        .hud span span { color: var(--accent-glow); }
        canvas { background: #010409; border: 2px solid var(--border-color); border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        .controls-info { margin-top: 14px; color: var(--text-muted); font-size: 0.85rem; text-align: center; }
        .btn-group { display: flex; gap: 10px; margin-top: 14px; }
        button { background: var(--accent-green); color: white; border: none; padding: 8px 18px; font-size: 0.95rem; font-weight: bold; border-radius: 6px; cursor: pointer; transition: 0.2s; }
        button:hover { background: var(--accent-glow); }
        .info-card { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; flex: 1; min-width: 320px; max-width: 480px; }
        .info-card h2 { font-size: 1.3rem; margin-bottom: 12px; color: #58a6ff; border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }
        .algo-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; margin-top: 10px; }
        .algo-table th, .algo-table td { border: 1px solid var(--border-color); padding: 8px; text-align: left; }
        .algo-table th { background: #21262d; color: var(--text-muted); }
        .leaderboard-list { list-style: none; margin-top: 12px; }
        .leaderboard-item { display: flex; justify-content: space-between; padding: 8px 10px; border-radius: 6px; background: #0d1117; margin-bottom: 6px; font-size: 0.9rem; }
        .leaderboard-item:first-child { border-left: 4px solid #f1e05a; }
        .tag { font-size: 0.75rem; background: #21262d; padding: 2px 6px; border-radius: 4px; color: var(--text-muted); }
    </style>
</head>
<body>
    <header>
        <h1>🐍 Snake: Algorithm Arena</h1>
        <p class="subtitle">VIT Bhopal University — CSE1021 Problem Solving & Programming Course Project</p>
        <div class="badge">Evaluation-Ready Web & Cloud Deployment</div>
    </header>

    <div class="main-container">
        <div class="game-card">
            <div class="hud">
                <span>Score: <span id="score">0</span></span>
                <span>Speed: <span id="speed">Medium</span></span>
                <span>High: <span id="high-score">0</span></span>
            </div>
            <canvas id="gameCanvas" width="420" height="420"></canvas>
            <div class="controls-info">Use <b>W A S D</b> or <b>Arrow Keys</b> to Steer | Space to Pause</div>
            <div class="btn-group">
                <button onclick="startGame()">New Game</button>
                <button onclick="togglePause()" style="background:#21262d;border:1px solid var(--border-color);">Pause</button>
            </div>
        </div>

        <div class="info-card">
            <h2>Algorithm & Curriculum Mapping</h2>
            <table class="algo-table">
                <tr><th>Concept</th><th>Implementation</th><th>Module</th></tr>
                <tr><td><b>Lists & Queue</b></td><td>Snake body coords O(1) advance</td><td><code>snake_engine.py</code></td></tr>
                <tr><td><b>Insertion Sort</b></td><td>In-place descending ranking</td><td><code>leaderboard.py</code></td></tr>
                <tr><td><b>Vectors / Tuples</b></td><td>Immutable (dr, dc) velocity</td><td><code>config.py</code></td></tr>
                <tr><td><b>Set Disjoint</b></td><td>Free-cell food placement</td><td><code>food_manager.py</code></td></tr>
            </table>

            <h2 style="margin-top: 24px;">Hall of Fame (Insertion Sorted)</h2>
            <div id="leaderboard" class="leaderboard-list">
                <div class="leaderboard-item"><span>1. Player Alpha</span><span class="tag">Score: 420 (Hard)</span></div>
                <div class="leaderboard-item"><span>2. Player Beta</span><span class="tag">Score: 310 (Medium)</span></div>
                <div class="leaderboard-item"><span>3. Test Run</span><span class="tag">Score: 180 (Easy)</span></div>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const GRID_SIZE = 20;
        const CELL = canvas.width / GRID_SIZE;

        let snake = [{r: 10, c: 10}, {r: 10, c: 9}, {r: 10, c: 8}];
        let direction = {r: 0, c: 1};
        let nextDirection = {r: 0, c: 1};
        let food = {r: 5, c: 5};
        let score = 0;
        let highScore = 0;
        let isPaused = false;
        let isGameOver = false;
        let gameInterval = null;
        let currentIntervalMs = 120;

        function spawnFood() {
            let freeCells = [];
            for (let r = 0; r < GRID_SIZE; r++) {
                for (let c = 0; c < GRID_SIZE; c++) {
                    if (!snake.some(s => s.r === r && s.c === c)) {
                        freeCells.push({r, c});
                    }
                }
            }
            if (freeCells.length === 0) return null;
            return freeCells[Math.floor(Math.random() * freeCells.length)];
        }

        function draw() {
            ctx.fillStyle = '#010409';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Grid lines
            ctx.strokeStyle = '#161b22';
            ctx.lineWidth = 1;
            for (let i = 0; i <= GRID_SIZE; i++) {
                ctx.beginPath();
                ctx.moveTo(i * CELL, 0); ctx.lineTo(i * CELL, canvas.height);
                ctx.moveTo(0, i * CELL); ctx.lineTo(canvas.width, i * CELL);
                ctx.stroke();
            }

            // Food
            ctx.fillStyle = '#f85149';
            ctx.beginPath();
            ctx.arc(food.c * CELL + CELL/2, food.r * CELL + CELL/2, CELL/2 - 2, 0, Math.PI * 2);
            ctx.fill();

            // Snake
            snake.forEach((segment, index) => {
                ctx.fillStyle = index === 0 ? '#3fb950' : '#2ea043';
                ctx.fillRect(segment.c * CELL + 1, segment.r * CELL + 1, CELL - 2, CELL - 2);
            });

            if (isGameOver) {
                ctx.fillStyle = 'rgba(1, 4, 9, 0.85)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#f85149';
                ctx.font = 'bold 26px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('GAME OVER', canvas.width/2, canvas.height/2 - 10);
                ctx.fillStyle = '#f0f6fc';
                ctx.font = '16px sans-serif';
                ctx.fillText('Press New Game to restart', canvas.width/2, canvas.height/2 + 25);
            }
        }

        function tick() {
            if (isPaused || isGameOver) return;
            direction = nextDirection;
            const newHead = {r: snake[0].r + direction.r, c: snake[0].c + direction.c};

            // Collision with boundaries
            if (newHead.r < 0 || newHead.r >= GRID_SIZE || newHead.c < 0 || newHead.c >= GRID_SIZE) {
                endGame("Boundary wall collision");
                return;
            }

            // Collision with self
            if (snake.slice(0, -1).some(seg => seg.r === newHead.r && seg.c === newHead.c)) {
                endGame("Self collision");
                return;
            }

            snake.unshift(newHead);
            if (newHead.r === food.r && newHead.c === food.c) {
                score += 20;
                document.getElementById('score').innerText = score;
                if (score > highScore) {
                    highScore = score;
                    document.getElementById('high-score').innerText = highScore;
                }
                food = spawnFood();
            } else {
                snake.pop();
            }
            draw();
        }

        function endGame(reason) {
            isGameOver = true;
            clearInterval(gameInterval);
            draw();
        }

        function startGame() {
            clearInterval(gameInterval);
            snake = [{r: 10, c: 10}, {r: 10, c: 9}, {r: 10, c: 8}];
            direction = {r: 0, c: 1};
            nextDirection = {r: 0, c: 1};
            score = 0;
            document.getElementById('score').innerText = score;
            food = spawnFood();
            isPaused = false;
            isGameOver = false;
            draw();
            gameInterval = setInterval(tick, currentIntervalMs);
        }

        function togglePause() {
            isPaused = !isPaused;
        }

        window.addEventListener('keydown', (e) => {
            const key = e.key.toLowerCase();
            if ((key === 'arrowup' || key === 'w') && direction.r !== 1) nextDirection = {r: -1, c: 0};
            else if ((key === 'arrowdown' || key === 's') && direction.r !== -1) nextDirection = {r: 1, c: 0};
            else if ((key === 'arrowleft' || key === 'a') && direction.c !== 1) nextDirection = {r: 0, c: -1};
            else if ((key === 'arrowright' || key === 'd') && direction.c !== -1) nextDirection = {r: 0, c: 1};
            else if (e.code === 'Space') togglePause();
        });

        startGame();
    </script>
</body>
</html>
"""

def app(environ, start_response):
    """WSGI standard application compatible with Vercel serverless function."""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    return [HTML_PAGE.encode('utf-8')]

class handler(BaseHTTPRequestHandler):
    """BaseHTTPRequestHandler fallback for Vercel Python runtime."""
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode('utf-8'))
