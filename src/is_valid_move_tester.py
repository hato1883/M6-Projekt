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
    TextUserInterface.show_chess_board(cb.get_chessboard(), debug=False)
    move = TextUserInterface.input_user_move()
    print(f"{move}")
    (origin, dest) = move


    cb.move(origin, dest)
    TextUserInterface.show_chess_board(cb.get_chessboard(), debug=True)
    input("Enter to continue")