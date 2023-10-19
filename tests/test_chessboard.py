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
    
    assert len(expected_board) == len(chessboard_ref.get_chessboard())
    for row in range(len(expected_board)):
        # Check amount of columns in the row are equal
        assert len(expected_board[row]) == len(chessboard_ref.get_chessboard()[row])
        for col in range(len(expected_board)):
            assert chessboard_ref.get_chessboard()[row][col] == None
    
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
    __is_board_equal(expected_board, chessboard_ref.get_chessboard())



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
    __is_board_equal(expected_board, ref.chessboard)


def test_add_piece():
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    ref = Chessboard()
    ref.create_board(3)
    assert ref.add_piece(b_qu, (1,0))
    assert ref.add_piece(b_ki, (1,2))
    expected_chessboard: list[list[ChessPiece]] = [
        [None, None, None],
        [b_qu, None, b_ki],
        [None, None, None],
    ]
    # check
    __is_board_equal(expected_chessboard, ref.chessboard)


def test_remove_piece():
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    # empty 3x3
    expected = Chessboard()
    expected.create_board(3)

    ref = Chessboard()
    ref.create_board(3)
    ref.add_piece(b_qu, (1,0))
    ref.add_piece(b_ki, (1,2))
    assert ref.remove_piece((1, 0))
    assert ref.remove_piece((1, 2))
    # check
    __is_board_equal(expected.chessboard, ref.chessboard)


def test_in_danger():
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

    chessboard: list[list[ChessPiece]] = [
        # 0     1     2     3     4     5     6     7
        [b_ro, b_kn, b_bi, b_qu, b_ki, b_bi, b_kn, b_ro], # 0
        [b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa], # 1
        [None, None, None, None, None, None, None, None], # 2
        [None, None, None, None, None, None, None, None], # 3
        [None, None, None, None, None, None, None, None], # 4
        [None, None, None, None, None, None, None, None], # 5
        [w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa], # 6
        [w_ro, w_kn, w_bi, w_qu, w_ki, w_bi, w_kn, w_ro], # 7
    ]

    board_refrence = Chessboard(chessboard)
    # check
    assert board_refrence.in_danger((0,0), Color.BLACK) == False
    assert board_refrence.in_danger((0,0), Color.WHITE) == False
    assert board_refrence.in_danger((0,1), Color.BLACK) == False
    assert board_refrence.in_danger((0,1), Color.WHITE) == True

    assert board_refrence.in_danger((1,1), Color.BLACK) == False
    assert board_refrence.in_danger((3,1), Color.BLACK) == False
    assert board_refrence.in_danger((5,1), Color.BLACK) == False

    board_refrence.add_piece(w_qu, (3,3))
    assert board_refrence.in_danger((1,0), Color.BLACK) == False
    assert board_refrence.in_danger((1,1), Color.BLACK) == True
    assert board_refrence.in_danger((1,2), Color.BLACK) == False
    assert board_refrence.in_danger((1,3), Color.BLACK) == True
    assert board_refrence.in_danger((1,4), Color.BLACK) == False
    assert board_refrence.in_danger((1,5), Color.BLACK) == True
    assert board_refrence.in_danger((1,6), Color.BLACK) == False
    assert board_refrence.in_danger((1,7), Color.BLACK) == False


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

test_in_danger()