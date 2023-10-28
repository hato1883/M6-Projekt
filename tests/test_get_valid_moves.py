import pytest  # noqa: F401
import sys
import os

current = os.path.dirname(__file__)
sys.path.append(current + "/../src")

from chessboard import Chessboard  # noqa: E402
from position_class import Position  # noqa: E402
from move_class import Move  # noqa: E402
from chess_piece_class import EMPTY_PIECE, ChessPiece  # noqa: E402
from piece_color_enum import Color  # noqa: E402
from piece_type_enum import PieceType  # noqa: E402
from move_type_enum import MoveType  # noqa: E402
from move_option_enum import MoveOption  # noqa: E402

# Black pieces
BLACK_ROOK = ChessPiece(Color.BLACK, PieceType.ROOK)
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
WHITE_KING = ChessPiece(Color.WHITE, PieceType.KING)
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
        [EMPTY_PIECE, EMPTY_PIECE, BLACK_ROOK],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, WHITE_KING]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves

    expected_moves = [(Position(2, 2), Move(Position(-1, -1),
                                            MoveType.COLLISION_DIAG,
                                            [MoveOption.CAN_TAKE,
                                             MoveOption.PROTECTED])),
                      (Position(2, 2), Move(Position(0, -1),
                                            MoveType.COLLISION_AXIS,
                                            [MoveOption.CAN_TAKE,
                                             MoveOption.PROTECTED]))]
    assert expected_moves == valid_moves

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, BLACK_ROOK],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [BLACK_ROOK, EMPTY_PIECE, WHITE_KING]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves
    expected_moves = [(Position(2, 2), Move(Position(-1, -1),
                                            MoveType.COLLISION_DIAG,
                                            [MoveOption.CAN_TAKE,
                                             MoveOption.PROTECTED]))]
    assert expected_moves == valid_moves

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, BLACK_ROOK],
        [EMPTY_PIECE, BLACK_ROOK, EMPTY_PIECE],
        [BLACK_ROOK, EMPTY_PIECE, WHITE_KING]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves
    expected_moves = [(Position(2, 2), Move(Position(-1, -1),
                                            MoveType.COLLISION_DIAG,
                                            [MoveOption.CAN_TAKE,
                                             MoveOption.PROTECTED]))]
    assert expected_moves == valid_moves

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, BLACK_ROOK, BLACK_ROOK],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [BLACK_ROOK, EMPTY_PIECE, WHITE_KING]
    ]
    chessboard_instance = Chessboard(board_state)
    valid_moves = chessboard_instance.get_valid_moves(Color.WHITE)
    # expected moves
    expected_moves = []
    assert expected_moves == valid_moves
