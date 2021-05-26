# Day 83 Tic-Tac-Toe
# Portfolio Python Solution
# Author: John Cupak

X = 'X'
O = 'O'
EMPTY = ' '

def print_instructions():
    """Display game instructions"""

    print("Welcome to the game of Tic-Tac-Toe.")
    print("You must pick to play either 'X' or 'O'.")
    print("'X' always goes first.")
    print("The first to get three in a row, column, or diagonal wins!")
    print("The 3 x 3 board is numbered as follows:")
    print(" 7 | 8 | 9 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 1 | 2 | 3 ")
    print("Use the numeric keypad to enter your move.")


def display_board(b):
    """Display contents of board positions"""

    # Board numbered as zero-indexed numeric keypad
    print(' ' + b[6] + ' | ' + b[7] + ' | ' + b[8] + ' ')
    print('---+---+---')
    print(' ' + b[3] + ' | ' + b[4] + ' | ' + b[5] + ' ')
    print('---+---+---')
    print(' ' + b[0] + ' | ' + b[1] + ' | ' + b[2] + ' ')


def is_legal_move(b, a):
    """Determines if position a is legal for board b"""

    if not isinstance(a, int):
        return False  # a is not an integer
    if a not in range(1,10):
        return False  # position a is not 1-9
    if b[a-1] is not EMPTY:
        return False  # Move must be to empty cell
    return True


def is_Terminal_State(b):
    """Returns True if game is over"""

    if EMPTY not in b:
        return True  # All positions filled
    else:
        for XO in [X, O]:
            if b[6] == XO and b[7] == XO and b[8] == XO:
                return True  # Row 1
            elif b[3] == XO and b[4] == XO and b[5] == XO:
                return True  # Row 2
            elif b[0] == XO and b[1] == XO and b[2] == XO:
                return True  # Row 3
            elif b[6] == XO and b[3] == XO and b[0] == XO:
                return True  # Column 1
            elif b[7] == XO and b[4] == XO and b[1] == XO:
                return True  # Column 2
            elif b[8] == XO and b[5] == XO and b[2] == XO:
                return True  # Column 3
            elif b[6] == XO and b[4] == XO and b[2] == XO:
                return True  # Diagonal 1
            elif b[8] == XO and b[4] == XO and b[0] == XO:
                return True  # Diagonal 2
    return False


def result(board, position, marker):
    """Returns the new board after a move is made"""

    new_board = board.copy()
    if new_board[position-1] == EMPTY:
        new_board[position-1] = marker

    return new_board

def game():
    """Play game of tic-tac-toe with computer"""

    # Version 1: User plays both sides. NO AI Computer

    print_instructions()

    # Initialization
    user = ''
    while user not in ['X', 'O']:
        user = input("Would you like to be X or O? (X starts): ").upper()
        if user not in ['X', 'O']:
            print("Please enter an 'X' or an 'O'.")
    # Got X or O

    game_over = False  # Not yet, it isn't
    player_turn = True if user == 'X' else False  # Who moves first?
    board = [' '] * 9 # Nine empty positions

    display_board(board)

    while not game_over:

        if player_turn:  # Player's Turn

            legal_move = False
            print()
            while not legal_move:
                position = int(input(f"Where would you like to place your X? "))
                legal_move = is_legal_move(board, position)
                if not legal_move:
                    print("Please enter an unoccupied board position from 1-9")
            # Got legal player move

            board = result(board, position, 'X')  # Update board
            display_board(board)
            player_turn = False  # Computer's turn next
            game_over = is_Terminal_State(board)

        else:  # Computer's turn

            legal_move = False
            print()
            while not legal_move:
                position = int(input(f"Where would you like to place your O? "))
                legal_move = is_legal_move(board, position)
                if not legal_move:
                    print("Please enter an unoccupied board position from 1-9")
            # Got legal computer move

            board = result(board, position, 'O') # Update board
            display_board(board)
            player_turn = True  # User's turn next
            game_over = is_Terminal_State(board)

    print(game_over)


if __name__ == '__main__':
    game()
