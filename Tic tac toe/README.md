# Tic Tac Toe Game

A simple two-player Tic Tac Toe game written in Python and designed for my Vityarthi Project.

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

1. Player X takes the first turn.
2. Player O follows as the second player.
3. Pick your lucky digits from 1 to 9 like you’re defusing a bomb with numbers.
4. Line up three of your chosen digits in a row, column, or diagonal—boom, you win!
5. If the board fills up and nobody won, congratulations, it’s a tie.
6. After each round, hit Y to keep the chaos going or N to escape before it gets weird.
   
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

## Main Concepts Used

1. Variables and data types
2. Lists
3. Functions
4. Parameters and arguments
5. if, elif, and else
6. while loop
7. for loop
8. Boolean expressions
9. Operators
10. Input and output
11. Modules
12. Basic algorithm design
