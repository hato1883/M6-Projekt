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

# Test if remove piece works as intended
def test_remove_piece():
    """test for remove_piece"""
    # TODO: add 1 more test case that is not dependable on add_piece(...) method
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    # empty 3x3
    expected = Chessboard()
    expected.create_board(3)

    starting_board: list[list[ChessPiece]] = [
        [None, None, None],
        [b_qu, None, b_ki],
        [None, None, None],
    ]

    expected_board: list[list[ChessPiece]] = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    ref = Chessboard(starting_board)
    loaded_expected = Chessboard(expected_board)
    assert ref.remove_piece(Position(1, 0))
    assert ref.remove_piece(Position(1, 2))
    # check
    assert expected.get_chessboard() == ref.get_chessboard()
    assert loaded_expected.get_chessboard() == ref.get_chessboard()