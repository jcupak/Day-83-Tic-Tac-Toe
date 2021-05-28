# Day 83 Tic-Tac-Toe

This is completion Python code for Day 83 of 100 Days of Code

The game board was set up as a list of nine positions, all initialized to EMPTY, numbered as the keyboard number keys:

   7 | 8 | 9    
  ---+---+---    
   4 | 5 | 6  
  ---+---+---  
   1 | 2 | 3   
   
Three constants were defined:
1. X = 'X' 
2. O = 'O'
3. EMPTY = ' '

## Version 1
The initial version contained the following modules:

### print_instructions
Displays game instructions
### display_board(b)
Displays contents of board b positions
### is_legal_move(board, move)
Returns True if move is to empty board position
### is_terminal_state(b)
Returns True if board is in terminal state (X won, O won, or game is a draw)
### terminal_value(b)
Returns 1 if X has won, -1 if O has won, or 0 if game is a draw
### result(board, move, marker)
This module put the X or O marker on the board at the move position.
### winner(board)
This module returned 1 if X player was the winner, -1 if the O player was the winner, and 0 if the game was a draw.
### game()
Displays board, then alternates between X and O player to allow them to place a marker on the board.
Displays winner (or draw) of terminal game.

## Version 2
The revision added three new modules:

### minvalue(board)
Returns move that produces smallest value of maxvalue(result(board, move))
### maxvalue(board
Returns move that produces highest value of minvalue(results(board, move
### minmax(board, player)
Determine best move for player X or player O
