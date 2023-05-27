#
# Author: Sebastian Smerd
# Project: PP3
# Class: Board - The class implements board for Tic Tac Toc game.
#

BOARD_SIZE = 3
PLAYER_X = 'X'
PLAYER_O = 'O'



class Board:
    """
    Main class Board. The class provides methods to run Tic Tac Toe game
    """

    def __init__(self):
        """
        The class constructor.
        """
        self.reset_game()
    

    def reset_game(self):
        """
        The method resets the board so that players can play once or multiple 
        times.
        """
        self.board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def add_moves(self, player, row, col):
        """
        The method add moves to the board.
        """
        
        if player not in (PLAYER_X,PLAYER_O):
            raise ValueError(f"Invalid player specified {player}")

        self.board[row][col] = player


    def is_move_duplicate(self, row, col):
        """
        The mothod check for duplicate moves
        """
        if self.board[row][col] != '.':
            return True    
        return False

    def print(self):
        """
        The mothod prints the board.
        """
        print()
        for row in self.board:
            print(" ".join(row))
        print()
        
    def check_win(self):
        """
        The method check for win.
        """

        # Check horizontal lines
        if ((self.board[0][0] == self.board[0][1] == self.board[0][2] 
                == PLAYER_X)
            or (self.board[1][0] == self.board[1][1] == self.board[1][2] 
                == PLAYER_X)
            or (self.board[2][0] == self.board[2][1] == self.board[2][2] 
                == PLAYER_X)):
            return PLAYER_X

        if ((self.board[0][0] == self.board[0][1] == self.board[0][2] 
                == PLAYER_O)
            or (self.board[1][0] == self.board[1][1] == self.board[1][2] 
                == PLAYER_O)
            or (self.board[2][0] == self.board[2][1] == self.board[2][2] 
                == PLAYER_O)):
            return PLAYER_O

        # Check vertical lines
        if ((self.board[0][0] == self.board[1][0] == self.board[2][0]
                == PLAYER_X)
            or (self.board[0][1] == self.board[1][1] == self.board[2][1]
                == PLAYER_X)
            or (self.board[0][2] == self.board[1][2] == self.board[2][2]
                == PLAYER_X)):
            return PLAYER_X

        if ((self.board[0][0] == self.board[1][0] == self.board[2][0]
                == PLAYER_O)
            or (self.board[0][1] == self.board[1][1] == self.board[2][1]
                == PLAYER_O)
            or (self.board[0][2] == self.board[1][2] == self.board[2][2]
                == PLAYER_O)):
            return PLAYER_O

        # Check for cross lines
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2] 
                == PLAYER_X) 
            or (self.board[0][2] == self.board[1][1] == self.board[2][0]
                == PLAYER_X)): 
            return PLAYER_X

        if ((self.board[0][0] == self.board[1][1] == self.board[2][2] 
                == PLAYER_O) 
            or (self.board[0][2] == self.board[1][1] == self.board[2][0]
                == PLAYER_O)): 
            return PLAYER_O

        return None 