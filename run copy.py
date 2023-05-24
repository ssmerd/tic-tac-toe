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
    "player1": 0,
    "player2": 0,
}

class Board:
    """
    Main class Board
    """
    def __init__(self):
        self.board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def is_finished():
        pass
    
    def get_winner():
        pass


def enter_moves(board):
    pass


def run_game(board):

    while True:

        while True:
            enter_moves(board)
            if board.is_finished(board):
                break

        winner = board.get_winner()
        if  winner in "XO":
              

        decision = input("Do you want to play another game (y,n)? ")

        if decision == "n":
            break
    


def main():
    board = Board()
    board.print()
    run_gane(board)


main()