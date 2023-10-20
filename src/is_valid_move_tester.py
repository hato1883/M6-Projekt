from chessboard import *
from text_user_interface import *

cb = Chessboard()
cb.create_default_board()

def move_piece(chess_board, move):
    (origin, dest) = move
    (row_origin, column_origin) = origin
    (row_dest, column_dest) = dest

    chess_board[row_dest][column_dest] = chess_board[row_origin][column_origin]
    chess_board[row_origin][column_origin] = None
    chess_board[row_dest][column_dest].set_has_moved_true()


while True:
  TextUserInterface.show_chess_board(cb.chessboard_list, debug=False)
  move = TextUserInterface.input_user_move()
  print()
  (origin, dest) = move
  valid_move = cb.is_axis_move_valid(origin, dest, [MoveOption.PROTECTED])
  print(valid_move)
  if valid_move:
    move_piece(cb.chessboard_list, move)
    TextUserInterface.show_chess_board(cb.chessboard_list, debug=True)
    input("Enter to continue")