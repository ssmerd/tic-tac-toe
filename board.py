#
# Author: Sebastian Smerd
# Project: PP3
# Class: Board - The class implements board for Tic Tac Toc game.
#


class Board:
    """
    Main class Board. The class provides methods to run Tic Tac Toe game
    """
    BOARD_SIZE = 3
    PLAYER_X = 'X'
    PLAYER_O = 'O'

    def __init__(self):
        """
        The class constructor.
        """
        self.reset_game()

    def reset_game(self):
        """
        The method resets the board so that players can
        play once or multipletimes.
        """
        self.board = \
            [["." for _ in range(Board.BOARD_SIZE)]
                for _ in range(Board.BOARD_SIZE)]

    def add_move(self, player, row, col):
        """
        The method add moves to the board.
        """
        if player not in (Board.PLAYER_X, Board.PLAYER_O):
            raise ValueError(f"Invalid player specified {player}")

        if not self.is_valid_move(row, col):
            raise ValueError("Invalid move")

        self.board[row][col] = player

    def is_valid_move(self, row, col):
        """
        Check if a move is valid.
        """
        if 0 <= row < Board.BOARD_SIZE and \
            0 <= col < Board.BOARD_SIZE \
                and self.board[row][col] == ".":
            return True
        return False

    def is_move_duplicate(self, row, col):
        """
        The mothod check for duplicate moves
        """
        if self.board[row][col] != '.':
            return True
        return False

    def print_board(self):
        """
        The mothod prints the board.
        """
        print()
        for row in self.board:
            print(" ".join(row))
        print()

    def is_full(self):
        """
        Check if the board is full.
        """
        for row in self.board:
            if "." in row:
                return False
        return True

    def is_winner(self):
        """
        The method check for win.
        """

        # Check horizontal lines
        if ((self.board[0][0] == self.board[0][1] == self.board[0][2]
                == Board.PLAYER_X)
            or (self.board[1][0] == self.board[1][1] == self.board[1][2]
                == Board.PLAYER_X)
            or (self.board[2][0] == self.board[2][1] == self.board[2][2]
                == Board.PLAYER_X)):
            return Board.PLAYER_X

        if ((self.board[0][0] == self.board[0][1] == self.board[0][2]
                == Board.PLAYER_O)
            or (self.board[1][0] == self.board[1][1] == self.board[1][2]
                == Board.PLAYER_O)
            or (self.board[2][0] == self.board[2][1] == self.board[2][2]
                == Board.PLAYER_O)):
            return Board.PLAYER_O

        # Check vertical lines
        if ((self.board[0][0] == self.board[1][0] == self.board[2][0]
                == Board.PLAYER_X)
            or (self.board[0][1] == self.board[1][1] == self.board[2][1]
                == Board.PLAYER_X)
            or (self.board[0][2] == self.board[1][2] == self.board[2][2]
                == Board.PLAYER_X)):
            return Board.PLAYER_X

        if ((self.board[0][0] == self.board[1][0] == self.board[2][0]
                == Board.PLAYER_O)
            or (self.board[0][1] == self.board[1][1] == self.board[2][1]
                == Board.PLAYER_O)
            or (self.board[0][2] == self.board[1][2] == self.board[2][2]
                == Board.PLAYER_O)):
            return Board.PLAYER_O

        # Check for cross lines
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2]
                == Board.PLAYER_X)
            or (self.board[0][2] == self.board[1][1] == self.board[2][0]
                == Board.PLAYER_X)):
            return Board.PLAYER_X

        if ((self.board[0][0] == self.board[1][1] == self.board[2][2]
                == Board.PLAYER_O)
            or (self.board[0][2] == self.board[1][1] == self.board[2][0]
                == Board.PLAYER_O)):
            return Board.PLAYER_O

        return None
