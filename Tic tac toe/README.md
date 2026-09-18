# Tic Tac Toe Game

A simple two-player Tic Tac Toe game written in Python as my project.

## How to run

```bash
python main.py
```

## How to play

The board positions are:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

- Player **X** starts.
- Player **O** plays second.
- Enter a position from **1 to 9**.
- A player wins when they occupy three positions in a row, column, or diagonal.
- If all nine positions are filled without a winner, the game is a draw.
- After each round, choose `Y` to play again or `N` to exit.

## Pseudocode - Game Loop

START
CREATE an empty 3 x 3 board
SET current player to X

WHILE game is running
    DISPLAY board
    INPUT position
    IF position is valid and empty
        PLACE current player's symbol

        IF current player has a winning combination
            DISPLAY winner
            END round

        IF board is full
            DISPLAY draw
            END round

        SWITCH player
    ELSE
        DISPLAY invalid move
END WHILE
STOP

## Flowchart

START
  |
  v
Create empty board
  |
  v
Set player = X
  |
  v
Display board
  |
  v
Input position
  |
  v
Is position valid and empty?
  | Yes                 | No
  v                     v
Place symbol       Show error
  |
  v
Winner?
 | Yes       | No
 v           v
Show winner  Board full?
             | Yes       | No
             v           v
          Show draw   Switch player
                         |
                         +----> Display board

## Main Concepts Used

- Variables and data types
- Lists
- Functions
- Parameters and arguments
- `if`, `elif`, and `else`
- `while` loop
- `for` loop
- Boolean expressions
- Operators
- Input and output
- Modules
- Basic algorithm design
