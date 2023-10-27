import pytest  # noqa: F401
import sys
import os

current = os.path.dirname(__file__)
sys.path.append(current + "/../src")

from chessboard import Chessboard  # noqa: E402
from position_class import Position  # noqa: E402
from chess_piece_class import EMPTY_PIECE, ChessPiece  # noqa: E402
from piece_color_enum import Color  # noqa: E402
from piece_type_enum import PieceType  # noqa: E402


# Test if remove piece works as intended
def test_remove_piece():
    """test for remove_piece"""
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    # empty 3x3
    expected = Chessboard()
    expected.create_board(3)

    starting_board: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [b_qu, EMPTY_PIECE, b_ki],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
    ]

    expected_board: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
    ]

    ref = Chessboard(starting_board)
    loaded_expected = Chessboard(expected_board)
    assert ref.remove_piece(Position(1, 0))
    assert ref.remove_piece(Position(1, 2))
    # check
    assert expected.get_chessboard() == ref.get_chessboard()
    assert loaded_expected.get_chessboard() == ref.get_chessboard()
