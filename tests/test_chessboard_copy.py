import pytest  # noqa: F401
import sys
import os

current = os.path.dirname(__file__)
sys.path.append(current + "/../src")

import copy  # noqa: E402
from chessboard import Chessboard  # noqa: E402
from position_class import Position  # noqa: E402
from chess_piece_class import ChessPiece  # noqa: E402
from piece_color_enum import Color  # noqa: E402
from piece_type_enum import PieceType  # noqa: E402


def test_chessboard_copy():
    """Tests copying chessboard"""
    original = Chessboard()
    original.create_default_board()

    shallow_copy = copy.copy(original)

    custom_deep_copy = original.deep_copy()

    # copy is not the same object as original
    assert (shallow_copy is original) is False
    # copy is equal in terms of comparison
    assert (shallow_copy == original) is True

    # copy contains the same refrence to chessboard list
    assert (shallow_copy.get_chessboard() is original.get_chessboard()) is True  # noqa E501
    assert (shallow_copy.get_chessboard() == original.get_chessboard()) is True  # noqa E501

    # copy contains the same refrence to move history list
    assert (shallow_copy.get_move_history() == original.get_move_history()) is True  # noqa E501
    assert (shallow_copy.get_move_history() is original.get_move_history()) is True  # noqa E501

    # deepcopy is not the same object as original
    assert (custom_deep_copy is original) is False
    # deepcopy is equal in terms of comparison
    assert (custom_deep_copy == original) is True

    # deepcopy's refrence to chessboard list is not the same as original
    assert (custom_deep_copy.get_chessboard() is original.get_chessboard()) is False  # noqa E501
    # deepcopy's chessboard list is equal in terms of comparison
    assert (custom_deep_copy.get_chessboard() == original.get_chessboard()) is True  # noqa E501

    # deepcopy's chess piece at given position is not the same obj
    assert (custom_deep_copy.get_piece(Position(0, 0)) is original.get_piece(Position(0, 0))) is False  # noqa E501
    # deepcopy's chess piece at given position is equal in compparison
    assert (custom_deep_copy.get_piece(Position(0, 0)) == original.get_piece(Position(0, 0))) is True  # noqa E501

    # deepcopy's chess piece Color at given position is the same obj (Enum)
    assert (custom_deep_copy.get_piece(Position(0, 0)).get_color() is original.get_piece(Position(0, 0)).get_color()) is True  # noqa E501
    # deepcopy's chess piece Color at given position is equal in compparison
    assert (custom_deep_copy.get_piece(Position(0, 0)).get_color() == original.get_piece(Position(0, 0)).get_color()) is True  # noqa E501

    # deepcopy's chess piece Type at given position is the same obj (Enum)
    assert (custom_deep_copy.get_piece(Position(0, 0)).get_type() is original.get_piece(Position(0, 0)).get_type()) is True  # noqa E501
    # deepcopy's chess piece Type at given position is equal in compparison
    assert (custom_deep_copy.get_piece(Position(0, 0)).get_type() == original.get_piece(Position(0, 0)).get_type()) is True  # noqa E501

    # deepcopy's refrence to move history is not the same as original
    assert (custom_deep_copy.get_move_history() is original.get_move_history()) is False  # noqa E501
    # deepcopy's move history is equal in terms of comparison
    assert (custom_deep_copy.get_move_history() == original.get_move_history()) is True  # noqa E501

    # now change piece at (0, 0) at se how shallow copy differs from deepcopy
    original.remove_piece(Position(0, 0))
    original.add_piece(ChessPiece(Color.WHITE, PieceType.KING), Position(0, 0))

    # copy is equal in terms of comparison
    assert (shallow_copy == original) is True

    # copy contains the same refrence to chessboard list
    assert (shallow_copy.get_chessboard() is original.get_chessboard()) is True  # noqa E501
    assert (shallow_copy.get_chessboard() == original.get_chessboard()) is True  # noqa E501

    # deepcopy is not equal in terms of comparison
    assert (custom_deep_copy == original) is False

    # deepcopy's move history is still equal in terms of comparison
    # as no move has been made
    assert (custom_deep_copy.get_move_history() == original.get_move_history()) is True  # noqa E501
