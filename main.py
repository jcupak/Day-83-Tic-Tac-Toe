# Day 83 Tic-Tac-Toe
# Portfolio Python Solution
# Author: John Cupak

X = 'X'      # Constant for player X marker
O = 'O'      # Constant for player O marker
EMPTY = ' '  # Constant for empty cell


def print_instructions():
    """Display game instructions"""

    print("Welcome to the game of Tic-Tac-Toe.")
    print("To play you must pick either 'X' or 'O'.")
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


def is_terminal_state(b):
    """Returns True if game is over, false otherwise"""

    # Checks if board is in a terminal state
    if EMPTY not in b:
        return True  # All positions filled
    else:
        for XO in [X, O]:
            if b[6] == XO and b[7] == XO and b[8] == XO:
                return True  # Row 1
            elif b[3] == XO and b[4] == XO and b[5] == XO:
                return True   # Row 2
            elif b[0] == XO and b[1] == XO and b[2] == XO:
                return True   # Row 3
            elif b[6] == XO and b[3] == XO and b[0] == XO:
                return True   # Column 1
            elif b[7] == XO and b[4] == XO and b[1] == XO:
                return True   # Column 2
            elif b[8] == XO and b[5] == XO and b[2] == XO:
                return True   # Column 3
            elif b[6] == XO and b[4] == XO and b[2] == XO:
                return True   # Diagonal 1
            elif b[8] == XO and b[4] == XO and b[0] == XO:
                return True   # Diagonal 2
    return False  # At least one space is empty


def terminal_value(b):
    """Returns 1 if X has won, -1 if O has won, or 0 if game is a draw"""

    # Finds numerical value for terminal state b
    # Check for X win, then O
    for XO in [X, O]:
        if b[6] == XO and b[7] == XO and b[8] == XO:
            return 1 if XO == X else -1  # Row 1
        elif b[3] == XO and b[4] == XO and b[5] == XO:
            return 1 if XO == X else -1  # Row 2
        elif b[0] == XO and b[1] == XO and b[2] == XO:
            return 1 if XO == X else -1  # Row 3
        elif b[6] == XO and b[3] == XO and b[0] == XO:
            return 1 if XO == X else -1  # Column 1
        elif b[7] == XO and b[4] == XO and b[1] == XO:
            return 1 if XO == X else -1  # Column 2
        elif b[8] == XO and b[5] == XO and b[2] == XO:
            return 1 if XO == X else -1  # Column 3
        elif b[6] == XO and b[4] == XO and b[2] == XO:
            return 1 if XO == X else -1  # Diagonal 1
        elif b[8] == XO and b[4] == XO and b[0] == XO:
            return 1 if XO == X else -1  # Diagonal 2
    return 0  # Game is a draw


def legal_moves(board):
    """Returns zero-based indices of legal (EMPTY) board moves"""

    # Possible actions (moves) for board in current state
    return [move for move in range(len(board)) if board[move] == EMPTY]  # Actions(board)


def is_legal_move(board, move):
    """Determines if move is 0-8 and board[move] is empty """

    return move in range(9) and board[move] == EMPTY


def result(board, move, marker):
    """Returns the new board after a move is made"""

    new_board = board.copy()
    new_board[move] = marker
    return new_board


def minvalue(board):
    """Picks move that produces smallest value of maxvalue(result(board, move))"""

    if is_terminal_state(board):
        return terminal_value(board)  # -1, 0, or 1
    else:
        value = 100  # Always possible to get below 100, as values are at most 1
        moves = legal_moves(board)  # What legal moves are available?
        for move in moves:
            value = min(value, maxvalue(result(board, move, O)))  # Find best move for O
    return value  # Best board position 0 - 9


def maxvalue(board):
    """Picks move that produces highest value of minvalue(results(board, move))"""

    if is_terminal_state(board):
        return terminal_value(board)  # -1, 0, or 1
    else:
        value = -100  # Always possible to get above -100, as values are at most 1
        moves = legal_moves(board)  # What legal moves are available?
        for move in moves:
            value = max(value, minvalue(result(board, move, X)))  # Find best move for Xe
    return value  # Best board position 0 - 8


def minmax(board, player):
    """Determine best move for player X or player O"""

    if is_terminal_state(board):
        return terminal_value(board)
    else:
        optimal_move = 0
        moves = legal_moves(board)  # What legal moves are available?

        # Whose turn is it?
        if player == X:  # Maximizing player
            best_value = -100
            for move in moves:
                if best_value < minvalue(result(board, move, O)):
                    best_value = minvalue(result(board, move, O))
                    optimal_move = move
            return optimal_move
        else:  # Minimizing player
            best_value = 100
            for move in moves:
                if best_value > maxvalue(result(board, move, X)):
                    best_value = maxvalue(result(board, move, X))
                    optimal_move = move
            return optimal_move


def winner(board):
    """Returns winner of terminal state"""

    reward = terminal_value(board)
    if reward == 1:
        return X
    elif reward == -1:
        return O
    else:
        return EMPTY


def game():
    """Play game of tic-tac-toe with computer"""

    # Version 1: User plays both sides. NO AI Computer
    # Version 2: Computer uses AI to pick best move

    print_instructions()

    # Initialization
    user = ''
    while user not in [X, O]:
        user = input("Would you like to be X or O? (X starts): ").upper()
        if user not in [X, O]:
            print("Please enter an 'X' or an 'O' (can be 'x' or 'o'.")

    game_over = False  # Not yet, it isn't
    player_turn = True if user == X else False  # Who moves first?
    board = [' '] * 9  # Initial game state: Nine empty positions

    print()
    print("The Game begins!")
    display_board(board)

    while not game_over:

        if player_turn:  # Player's Turn

            print()

            # Get legal user's move
            legal_move = False
            user_move = 0
            while not legal_move:
                user_move = int(input(f"Where would you like to place your X? "))
                legal_move = is_legal_move(board, user_move - 1)  # Convert to zero-indexed
                if not legal_move:
                    print("I'm sorry, but that square is occupied by {board[move - 1]}.")
                    print("Please enter an unoccupied board position (1-9).")

            board = result(board, user_move - 1, X)  # Update board with X's move
            display_board(board)
            player_turn = False  # Computer's turn next
            game_over = is_terminal_state(board)  # Check for end game

        else:  # Computer's turn

            print()
            print("AI is thinking...")

            ai_move = minmax(board, O)  # Figure best move for computer
            print(f"The computer moves to {ai_move + 1}.")  # Show computer's move as 1-indexed value
            board = result(board, ai_move, O)  # Update board with O's move
            display_board(board)
            player_turn = True  # player's turn next
            game_over = is_terminal_state(board)

    print()
    print("Game over.")
    if winner(board) == EMPTY:
        print("The game is a draw!")
    else:
        print(f"Player {winner(board)} is the winner!")


if __name__ == '__main__':
    game()
