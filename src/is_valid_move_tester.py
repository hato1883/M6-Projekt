from chessboard import *
from text_user_interface import *

cb = Chessboard()
cb.create_default_board()

#cb.remove_piece(Position(7,1))
#cb.remove_piece(Position(7,2))
#cb.remove_piece(Position(7,3))

cb.move(Position(6,0),Position(4,0))
cb.move(Position(4,0),Position(3,0))
cb.move(Position(1,1),Position(3,1))


while True:
    TextUserInterface.show_chess_board(cb.get_chessboard(), debug=False)
    move = TextUserInterface.input_user_move()
    print(f"{move}")
    (origin, dest) = move

    cb.move(origin, dest)
    TextUserInterface.show_chess_board(cb.get_chessboard(), debug=True)
    input("Enter to continue")