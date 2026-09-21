WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def check_winner(board, player):
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


def board_full(board):
    return " " not in board


def available_moves(board):
    return [index + 1 for index, value in enumerate(board) if value == " "]
