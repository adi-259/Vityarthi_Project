from algorithms import check_winner, board_full, available_moves


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def display_board(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()

    def make_move(self, position):
        if position < 1 or position > 9:
            return False

        index = position - 1
        if self.board[index] != " ":
            return False

        self.board[index] = self.current_player
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_round(self):
        self.board = [" "] * 9
        self.current_player = "X"

        print("\nTIC TAC TOE")
        print("Player X goes first.")
        print("Choose positions 1-9:")

        position_board = [str(i) for i in range(1, 10)]
        print(f" {position_board[0]} | {position_board[1]} | {position_board[2]} ")
        print("---+---+---")
        print(f" {position_board[3]} | {position_board[4]} | {position_board[5]} ")
        print("---+---+---")
        print(f" {position_board[6]} | {position_board[7]} | {position_board[8]} ")

        while True:
            self.display_board()

            try:
                position = int(input(f"Player {self.current_player}, enter position: "))
            except ValueError:
                print("Please enter a number from 1 to 9.")
                continue

            if not self.make_move(position):
                print("Invalid move. Choose an empty position from 1 to 9.")
                continue

            if check_winner(self.board, self.current_player):
                self.display_board()
                print(f"Player {self.current_player} wins!")
                return self.current_player

            if board_full(self.board):
                self.display_board()
                print("It's a draw!")
                return "Draw"

            self.switch_player()

    def run(self):
        print("CSE1021 Tic Tac Toe Game")

        while True:
            self.play_round()

            choice = input("\nPlay again? (Y/N): ").strip().upper()
            if choice != "Y":
                print("Thanks for playing!")
                break
