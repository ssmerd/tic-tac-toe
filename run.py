# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#
# Author: Sebastian Smerd
# Project: PP3
#

#
# Constant values
#
BOARD_SIZE = 3

#
# Global values
#
scores = {
    "X": 0,
    "O": 0,
}

class Board:
    """
    Main class Board
    """
    def __init__(self):
        self.board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    def add_moves(self, player, row, col):
        
        if player not in "XO":
            raise ValueError(f"Invalid player specified {player}")

        self.board[row][col] = player


    def is_move_duplicate(self, row, col):

        if self.board[row][col] != '.':
            return True
        
        return False

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def is_finished(self):
        return True
    
    def get_winner(self):
        return "X"


def enter_moves(board, player):

    print("Top left corner is row: 0, col: 0\n")
    
    row, col = -1, -1

    while True:

        try:
            row = int(input(f"Enter row for player {player} (0-2): "))

            if row < 0 or row > BOARD_SIZE - 1:
                raise ValueError
            else:
                break

        except ValueError:
            print("Invalid row\n")
            continue
    
    while True:

        try:
            col = int(input(f"Enter column for player {player} (0-2): "))

            if col < 0 or col > BOARD_SIZE - 1:
                raise ValueError
            else:
                break
            
        except ValueError:
            print("Invalid column\n")
            continue

    if not board.is_move_duplicate(row, col):
        board.add_moves(player, row, col)
        return True
    else:
        print("Error: You have entered duplicate moves.")
    
    return False

def print_results():
    pass

def run_game(board):

    while True:

        while True:
            if enter_moves(board, "X"):
                break

        while True:        
            if enter_moves(board, "O"):
                break

        board.print()

        if board.is_finished():
            break

        winner = board.get_winner()

        if winner in "XO":
            scores[winner] += 1
        else:
            print("No winner this time.")
        
        # decision = input("Do you want to play another game (y,n)? ")

        # if decision == "n":
        #     print_results()
        #     break

    


def main():
    board = Board()
    # board.print()
    run_game(board)


main()