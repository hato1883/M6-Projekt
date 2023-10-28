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


def test_add_piece():
    """Tests add_piece(ChessPiece, Position) method"""
    # TODO: add more tests
    b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
    b_ki = ChessPiece(Color.BLACK, PieceType.KING)
    ref = Chessboard()
    ref.create_board(3)
    assert ref.add_piece(b_qu, Position(1, 0))
    assert ref.add_piece(b_ki, Position(1, 2))
    expected_chessboard: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [b_qu, EMPTY_PIECE, b_ki],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
    ]
    expected = Chessboard(expected_chessboard)
    assert expected.get_chessboard() == ref.get_chessboard()
