import pytest
import sys
import os
 
# getting the name of the directory
# where the this file is present.
#current = os.path.dirname(os.path.realpath(__file__))
current = os.path.dirname(__file__)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(current + "/../src")

from chessboard import *

# Test if create board returns a 2d list filed with None
def test_create_board():
    chessboard_ref = Chessboard()
    expected_board = [
        [None]
        ]
    chessboard_ref.create_board(1)
    
    assert len(expected_board) == len(chessboard_ref.chessboard_list)
    for row in range(len(expected_board)):
        # Check amount of columns in the row are equal
        assert len(expected_board[row]) == len(chessboard_ref.chessboard_list[row])
        for col in range(len(expected_board)):
            assert chessboard_ref.chessboard_list[row][col] == None
    
    expected_board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
        ]
    chessboard_ref.create_board() # default size is 8
    # check
    __is_board_equal(expected_board, chessboard_ref.chessboard_list)



# Test if we get a default chessboard
def test_create_default_board():
    # Black Pieces
    b_ro = ChessPiece(Color.BLACK, PieceType.ROOK)
    b_kn = ChessPiece(Color.BLACK, PieceType.KNIGHT)
    b_bi = ChessPiece(Color.BLACK, PieceType.BISHOP)
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    b_pa = ChessPiece(Color.BLACK, PieceType.PAWN)
    # White Pieces
    w_ro = ChessPiece(Color.WHITE, PieceType.ROOK)
    w_kn = ChessPiece(Color.WHITE, PieceType.KNIGHT)
    w_bi = ChessPiece(Color.WHITE, PieceType.BISHOP)
    w_qu = ChessPiece(Color.WHITE, PieceType.QUEEN)
    w_ki = ChessPiece(Color.WHITE, PieceType.KING)
    w_pa = ChessPiece(Color.WHITE, PieceType.PAWN)
    expected_board: list[list[ChessPiece]] = [
        [b_ro, b_kn, b_bi, b_qu, b_ki, b_bi, b_kn, b_ro],
        [b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa],
        [w_ro, w_kn, w_bi, w_qu, w_ki, w_bi, w_kn, w_ro],
    ]
    ref = Chessboard()
    ref.create_default_board()
    # Check
    __is_board_equal(expected_board, ref.chessboard_list)


def test_add_piece():
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    ref = Chessboard()
    ref.create_board(3)
    ref.add_piece(b_qu, (1,0))
    ref.add_piece(b_ki, (1,2))
    expected_chessboard: list[list[ChessPiece]] = [
        [None, None, None],
        [b_qu, None, b_ki],
        [None, None, None],
    ]
    # check
    __is_board_equal(expected_chessboard, ref.chessboard_list)


def __is_board_equal(expected: list[list[ChessPiece]], recived: list[list[ChessPiece]]):
    assert len(expected) == len(recived)
    for row in range(len(expected)):
        # Check amount of columns in the row are equal
        assert len(expected[row]) == len(recived[row])
        for col in range(len(expected)):
            # Check if piece matches expexted
            print()
            if expected[row][col] is not None:
                assert expected[row][col].get_color() == recived[row][col].get_color()
                assert expected[row][col].get_type() == recived[row][col].get_type()
            else:
                assert expected[row][col] == recived[row][col]