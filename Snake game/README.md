# 🐍 Snake Algorithm Arena

A Python-based Snake Game project developed as part of the **VIT Bhopal University Vityarthi Project**.

The project combines the classic Snake game with algorithmic programming concepts such as game loops, conditional statements, iteration, functions, data structures, collision detection, and score management.

## 🎮 Project Overview

**Snake Algorithm Arena** is an interactive Snake game where the player controls a growing snake, collects food, earns points, and tries to achieve the highest possible score without colliding with the walls or itself.

The project focuses on implementing programming concepts using **Python** while maintaining an interactive and user-friendly game experience.

## ✨ Features

- Classic Snake gameplay
- Keyboard-based controls
- Real-time movement
- Food generation
- Snake growth
- Score tracking
- Collision detection
- Game-over system
- Restart functionality
- Increasing difficulty
- Clean and interactive interface
- Python-based implementation

## 🧠 Concepts Used

This project demonstrates several fundamental programming concepts:

- Variables and data types
- Input and output
- Conditional statements
- Boolean expressions
- `if`, `elif`, and `else`
- `for` and `while` loops
- `break` and `continue`
- Functions
- Lists and data structures
- Random number generation
- Coordinate systems
- Collision detection
- Event handling
- Game loops
- Modular programming

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pygame | Game development and graphics |
| Random | Random food generation |
| Git | Version control |
| GitHub | Project hosting |

## 🚀 Installation

### 1. Install Python

Download and install Python from the official Python website.

Make sure to enable:

```text
Add Python to PATH
```

during installation.

### 2. Clone the Repository

```bash
git clone https://github.com/adi-259/Vityarthi_Project.git
```

### 3. Enter the Project Folder

```bash
cd Vityarthi_Project
cd "Snake game"
```

### 4. Install Dependencies

If the project contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

If Pygame is required but isn't listed:

```bash
pip install pygame
```

### 5. Run the Game

```bash
python main.py
```

## 🎮 Controls

| Key | Action |
|---|---|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| Space | Pause/Resume |
| R | Restart |
| Esc | Exit |

> Controls may vary depending on the final implementation.

## 🏆 Gameplay

The objective is to collect as much food as possible while avoiding:

1. Collision with the walls
2. Collision with the snake's own body

Every successful food collection increases the snake's length and score.

The game ends when the snake collides with an obstacle.

## 🔄 Basic Game Algorithm

```text
START
  ↓
Initialize game
  ↓
Create snake
  ↓
Generate food
  ↓
Start game loop
  ↓
Read keyboard input
  ↓
Move snake
  ↓
Check food collision
  ↓
Food collected?
 ┌───────┴───────┐
YES              NO
 ↓                ↓
Increase score    Continue
Grow snake
Generate food
 └───────┬───────┘
         ↓
Check wall/body collision
         ↓
Collision?
 ┌───────┴───────┐
YES              NO
 ↓                ↓
Game Over       Continue loop
 ↓
Restart / Exit
 ↓
END
```

## 📊 Educational Objectives

The project was developed to demonstrate how theoretical programming concepts can be converted into a functional software application.

The project particularly demonstrates:

- Problem solving
- Algorithm design
- Logical thinking
- Python programming
- Data structure usage
- Event-driven programming
- Software development workflow

## 🔮 Future Improvements

Possible future enhancements include:

- Multiple difficulty levels
- High-score leaderboard
- Sound effects
- Background music
- Multiple maps
- Power-ups
- Different snake skins
- Multiplayer mode
- AI-controlled snake
- Algorithm visualization
- Save/load high scores

## 👨‍💻 Author

**Aditya Kumar**
Reg No. 26BAI10114
B.Tech CSE (AI & ML)  
VIT Bhopal University

## 📚 Academic Project

Developed as part of the **Vityarthi Project – VIT Bhopal University**.

## 📄 License

This project is intended primarily for educational and academic purposes.
