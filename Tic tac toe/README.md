# Tic Tac Toe Game

A simple two-player Tic Tac Toe game written in Python and designed as a CSE1021 project.

## How to run

```bash
python main.py
```

## How to play

The board positions are:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

1. Player **X** starts.
2. Player **O** plays second.
3. Enter a position from **1 to 9**.
4. A player wins when they occupy three positions in a row, column, or diagonal.
5. If all nine positions are filled without a winner, the game is a draw.
6. After each round, choose `Y` to play again or `N` to exit.

## Pseudocode - Game Loop

```text
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
```

## Flowchart

```text
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
```

## Main Concepts Used

1. Variables and data types
2. Lists
3. Functions
4. Parameters and arguments
5. `if`, `elif`, and `else`
6. `while` loop
7. `for` loop
8. Boolean expressions
9. Operators
10. Input and output
11. Modules
12. Basic algorithm design
