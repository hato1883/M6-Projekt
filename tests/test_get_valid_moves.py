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

# Black pieces
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


def tuple_list_comparison(expected, recived) -> bool:
    if len(expected) != len(recived):
        return False
    for (ex_origin, ex_dest) in expected:
        for (re_origin, re_dest) in recived:
            if ex_origin == re_origin and ex_dest == re_dest:
                break
        else:
            return False
        continue
    return True


def test_get_valid_moves():
    """Tests get valid moves"""

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, b_ro],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves
    expected_moves = [(Position(2, 2), Position(1, 1)),
                      (Position(2, 2), Position(2, 1))]
    assert (Position(2, 2), Position(1, 1)) in valid_moves
    assert expected_moves == valid_moves

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, b_ro],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [b_ro, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves
    expected_moves = [(Position(2, 2), Position(1, 1))]
    assert expected_moves == valid_moves

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, b_ro],
        [EMPTY_PIECE, b_ro, EMPTY_PIECE],
        [b_ro, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves
    expected_moves = [(Position(2, 2), Position(1, 1))]
    assert expected_moves == valid_moves

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, b_ro, b_ro],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [b_ro, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves
    expected_moves = []
    assert expected_moves == valid_moves
