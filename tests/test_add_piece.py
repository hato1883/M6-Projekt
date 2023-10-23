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

# Tests if add_piece() works as intended
def test_add_piece():
    """Tests add_piece(ChessPiece, Position) method"""
    # TODO: add more tests
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    ref = Chessboard()
    ref.create_board(3)
    assert ref.add_piece(b_qu, Position(1,0))
    assert ref.add_piece(b_ki, Position(1,2))
    expected_chessboard: list[list[ChessPiece]] = [
        [None, None, None],
        [b_qu, None, b_ki],
        [None, None, None],
    ]
    # check
    assert Chessboard(expected_chessboard).get_chessboard() == ref.get_chessboard()