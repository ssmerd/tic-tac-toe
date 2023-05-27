# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#
# Author: Sebastian Smerd
# Project: PP3
# Main program plus functions
#

from board import Board, BOARD_SIZE, PLAYER_X, PLAYER_O

scores = {
    PLAYER_X : 0,
    PLAYER_O : 0,
}
    
def enter_moves(board, player):
    """
    The function is to enter a player's moves. It also check for duplicate moves
    """

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


def is_game_finished():
    """
    The function checks if users want to finish the game.
    """
    while True:
        try:
            decision = input(f"Do you want to continue (y,n): \n")
            if decision not in ('y', 'n'):
                raise ValueError
            elif decision == "y":
                return False
            else:
                return True
                
        except ValueError:
            print("Enter a valid decision (y,n)\n")
            continue

def print_results():
    """
    The function print results.
    """
    print()
    print(f"Player {PLAYER_X} won {scores[PLAYER_X]} times\n")
    print(f"Player {PLAYER_O} won {scores[PLAYER_O]} times\n")

def run_game(board):
    """
    The main function which run one or more games
    """

    end_game = False

    print("Top left corner is row: 0, col: 0\n")

    while True:
        while True:
            if enter_moves(board, "X"):
                board.print()
                if board.check_win() == PLAYER_X:
                    print(f"Player {PLAYER_X} won the game\n")
                    scores[PLAYER_X] += 1
                    end_game = True
                    break
                break
        while True and not end_game:        
            if enter_moves(board, "O"):
                board.print()
                if board.check_win() == PLAYER_O:
                    print(f"Player {PLAYER_O} won the game\n")
                    scores[PLAYER_O] += 1
                    end_game = True
                    break
                break

        if end_game:
            end_game = False
            if is_game_finished():
                break
            else:
                board.reset_game()


def print_banner():
    """
    The function prints the banner.
    """
    print()
    print(""" #######             #######                  #######               
    #    #  ####        #      ##    ####        #     ####  ###### 
    #    # #    #       #     #  #  #    #       #    #    # #      
    #    # #            #    #    # #            #    #    # #####  
    #    # #            #    ###### #            #    #    # #      
    #    # #    #       #    #    # #    #       #    #    # #      
    #    #  ####        #    #    #  ####        #     ####  ###### 
                                                                    """)
    print()


def main():
    print_banner()
    board_game = Board()
    run_game(board_game)
    print_results()

if __name__ == "__main__":
    main()