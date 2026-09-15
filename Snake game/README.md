# Snake: Algorithm Arena
### CSE1021 Problem Solving and Programming – Evaluated Course Project
**Institution**: Vellore Institute of Technology (VIT Bhopal University)  
**Academic Target**: VITyarthi Flipped Course Evaluation  

---

## 1. Overview
**Snake: Algorithm Arena** is an academically grounded, modular implementation of the classic Snake game designed specifically to demonstrate the core computational concepts taught in **CSE1021 (Problem Solving and Programming)**.

Unlike typical monolithic script implementations, this project separates state management, vector input filtering, collision mathematics, set-based food placement, dynamic interval modulation, and file persistence into 10 cohesive, single-responsibility modules. The project features an explicit **Insertion Sort** algorithm for leaderboard management, deterministic pseudo-random seed testing, and dual interfaces: a hardware-accelerated 2D Pygame graphical interface and an interactive, zero-dependency ASCII Terminal CLI mode.

---

## 2. CSE1021 Syllabus Alignment
Every core component maps directly to verified CSE1021 curriculum concepts:

| Course Concept | Concrete Implementation in Project | File Reference |
|---|---|---|
| **Lists & Mutability** | Ordered snake body coordinates with O(1) head insertion and tail popping | `src/snake_engine.py` |
| **Tuples** | Immutable 2D grid coordinates `(row, col)` and velocity vectors `(dr, dc)` | `src/config.py`, `src/game_state.py` |
| **Dictionaries** | Game state bundles, difficulty settings, and serialized leaderboard entries | `src/config.py`, `src/game_state.py` |
| **Control Flow & Selection** | Direction change filtering, 180-degree reversal prevention, state machine | `src/input_controller.py` |
| **Set Operations & Comprehensions** | Free-cell candidate generation via set subtraction `all_cells - set(snake)` | `src/food_manager.py` |
| **Pseudo-Random Generation (Unit IV)** | Deterministic food coordinate generation with reproducible seed support | `src/food_manager.py` |
| **Sorting Algorithms** | Explicit in-place descending Insertion Sort for top-10 leaderboard ranking | `src/leaderboard.py` |
| **File Handling & Defensive I/O** | Safe JSON persistence with automatic missing/corrupted file recovery | `src/persistence.py` |

---

## 3. Key Features
- **Dual Execution Interfaces**:
  - **Graphical Mode**: 60 FPS hardware-accelerated 2D interface using `pygame-ce` with smooth snake segments, direction-aware eyes, pulsating food, HUD banner, and modal overlays.
  - **Terminal CLI Mode (`--cli-mode`)**: Dependency-free ASCII board rendering directly in standard Windows PowerShell, CMD, or Linux terminal.
- **Headless Automated Self-Test (`--self-test`)**:
  - Terminal-based diagnostic command validating 13 discrete functional requirements without opening a GUI window.
- **Deterministic Reproducibility (`--seed <INT>`)**:
  - Enables repeatable gameplay and food sequences for deterministic testing and grading.
- **Smart Reversal Prevention**:
  - Automatically rejects instant 180-degree turns (e.g. pressing LEFT while moving RIGHT) to prevent unintended self-collisions.
- **Dynamic Speed Progression**:
  - Shortens tick intervals every 5 foods consumed to scale difficulty gradually up to safe hardware minimums.
- **Persistent Hall of Fame**:
  - Maintains top-10 historic runs ranked via explicit Insertion Sort in `data/leaderboard.json`.

---

## 4. Technologies & Prerequisites
- **Language**: Python 3.10+ (Tested on Python 3.14.7)
- **Standard Libraries Used**: `sys`, `os`, `random`, `json`, `argparse`, `time`, `unittest`
- **External Dependencies**: `pygame-ce>=2.5.0` (Optional for terminal CLI mode and self-test)

---

## 5. Installation & Setup

### Clone or Download the Repository:
```bash
git clone https://github.com/{username}/snake-algorithm-arena.git
cd snake-algorithm-arena
```

### (Recommended) Create and Activate a Virtual Environment:
**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```
*(Note: If running in pure terminal CLI mode `--cli-mode` or `--self-test`, no external pip packages are strictly required.)*

---

## 6. Execution Commands

### 1. Launch the Full Graphical Game (Default)
```bash
python main.py
```
*Keyboard Controls*:
- **Start / Select**: `ENTER` or `SPACE`
- **Steer**: Arrow Keys (`UP`, `DOWN`, `LEFT`, `RIGHT`) or `W`, `A`, `S`, `D`
- **Pause / Resume**: `P` or `SPACE`
- **Difficulty Selection** (in Menu): `1` (Easy), `2` (Medium), `3` (Hard)
- **Leaderboard**: `L`
- **Restart Run** (on Game Over): `R`
- **Return to Menu / Quit**: `M` / `ESC` / `Q`

### 2. Run Interactive Terminal CLI Mode (Zero GUI dependencies)
```bash
python main.py --cli-mode
```
*Allows playing directly in your command line terminal.*

### 3. Run Headless Self-Test Suite
```bash
python main.py --self-test
```
*Executes all 13 requirement tests in memory and outputs a formatted pass/fail matrix.*

### 4. Run Deterministic Seeded Simulation
```bash
python main.py --seed 42
```

### 5. Launch with Preset Difficulty
```bash
python main.py --difficulty hard
```

---

## 7. Testing Suite

The repository includes a comprehensive `unittest` test suite covering all units:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Test Coverage Summary:
- `tests/test_game_state.py`: Verifies initial variables, reset functionality, and summary dictionary exports.
- `tests/test_movement.py`: Validates vector arithmetic, head advancement, tail maintenance, and growth.
- `tests/test_collision.py`: Asserts wall collisions across all 4 grid boundaries and self-collision with tail-chase checks.
- `tests/test_food.py`: Validates free-cell filtering, occupied cell avoidance, board-full win condition, and seed reproducibility.
- `tests/test_score.py`: Verifies points multipliers, interval reduction thresholds, and clamping.
- `tests/test_leaderboard.py`: Asserts descending order from Insertion Sort, duplicate score stability, and JSON persistence.

---

## 8. Project Structure
```
snake-algorithm-arena/
├── README.md                      # Project documentation and execution instructions
├── statement.md                   # Problem statement, scope, target users, and features
├── requirements.txt               # Dependency specification (pygame-ce)
├── .gitignore                     # Git exclusion rules
├── main.py                        # Application entry point and CLI controller
├── src/
│   ├── __init__.py                # Package indicator
│   ├── config.py                  # Constants, dimensions, difficulty presets, and colors
│   ├── game_state.py              # Central game state model and lifecycle transitions
│   ├── input_controller.py        # Direction parsing and reversal prevention logic
│   ├── snake_engine.py            # Movement calculations and body elongation
│   ├── collision_engine.py        # Boundary limits and self-collision checks
│   ├── food_manager.py            # Free-cell scanning and seeded PRNG food placement
│   ├── score_manager.py           # Scoring multipliers and dynamic speed acceleration
│   ├── leaderboard.py             # Explicit Insertion Sort and ranking management
│   ├── persistence.py             # Defensive JSON read/write handlers
│   └── renderer.py                # Dual rendering engines (Pygame GUI and ASCII CLI)
├── tests/
│   ├── __init__.py                # Test package indicator
│   ├── test_game_state.py         # State lifecycle unit tests
│   ├── test_movement.py           # Vector movement unit tests
│   ├── test_collision.py          # Spatial collision tests
│   ├── test_food.py               # Food generator and PRNG tests
│   ├── test_score.py              # Score and interval scaling tests
│   └── test_leaderboard.py        # Insertion sort and ranking tests
├── data/
│   └── leaderboard.json           # Persistent Hall of Fame data storage
└── docs/
    ├── architecture.svg           # High-level tiered architectural diagram
    ├── workflow.svg               # Complete execution flowchart and state transitions
    ├── use_case.svg               # Actor use case model
    ├── class_diagram.svg          # Class, module, and component dependencies
    ├── sequence_diagram.svg       # Single-tick runtime sequence diagram
    ├── er_diagram.svg             # Storage schema and state model
    ├── algorithms.md              # Pseudocode and asymptotic complexity analysis
    └── CSE1021_Project_Report.md  # Formal 15-section academic report
```

---

## 9. Troubleshooting & Known Behaviors
- **Pygame Not Installed?**: Run in terminal mode using `python main.py --cli-mode` or run `--self-test`. Both execute completely using Python standard library alone.
- **Corrupted Leaderboard File?**: `src/persistence.py` automatically detects damaged or unreadable JSON files and re-initializes a clean list without crashing the game.
- **Headless Environments**: When running in automated CI or headless virtual machines without an X11/Windows display server, invoke `--self-test` to inspect full functionality.
