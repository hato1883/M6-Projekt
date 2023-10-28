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
EMPTY_PIECE
black_rook_ = ChessPiece(Color.BLACK, PieceType.ROOK)
black_knigh = ChessPiece(Color.BLACK, PieceType.KNIGHT)
black_bisho = ChessPiece(Color.BLACK, PieceType.BISHOP)
black_queen = ChessPiece(Color.BLACK, PieceType.QUEEN)
black_king_ = ChessPiece(Color.BLACK, PieceType.KING)
black_pawn_ = ChessPiece(Color.BLACK, PieceType.PAWN)
# White Pieces
white_rook_ = ChessPiece(Color.WHITE, PieceType.ROOK)
white_knigh = ChessPiece(Color.WHITE, PieceType.KNIGHT)
white_bisho = ChessPiece(Color.WHITE, PieceType.BISHOP)
white_queen = ChessPiece(Color.WHITE, PieceType.QUEEN)
white_king_ = ChessPiece(Color.WHITE, PieceType.KING)
white_pawn_ = ChessPiece(Color.WHITE, PieceType.PAWN)


def test_in_danger_rook_threats():
    """Tests in_danger() method using only rook pieces"""
    ####
    # Black attacking_
    ####
    board_state: list[list[ChessPiece]] = [
        [black_rook_, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the rook? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, black_rook_, EMPTY_PIECE],
        [black_rook_, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [black_rook_, black_rook_, EMPTY_PIECE],
        [black_rook_, black_rook_, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, black_rook_],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the rooks? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [black_rook_, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the rook? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [black_rook_, black_rook_, black_rook_],
        [black_rook_, black_rook_, black_rook_],
        [black_rook_, black_rook_, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the rooks? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    ####
    # White attacking_
    ####
    board_state: list[list[ChessPiece]] = [
        [white_rook_, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the rook? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, white_rook_, EMPTY_PIECE],
        [white_rook_, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [white_rook_, white_rook_, EMPTY_PIECE],
        [white_rook_, white_rook_, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, white_rook_],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the rooks? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [white_rook_, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the rook? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [white_rook_, white_rook_, white_rook_],
        [white_rook_, white_rook_, white_rook_],
        [white_rook_, white_rook_, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the rooks? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True


def test_in_danger_bisho_threats():
    """Tests in_danger() method with only bisho pieces"""

    ####
    # Black attacking_
    ####
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, black_bisho, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the bisho? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, black_bisho, EMPTY_PIECE],
        [black_bisho, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the bishos? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, black_bisho, black_bisho],
        [black_bisho, EMPTY_PIECE, black_bisho],
        [black_bisho, black_bisho, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the bishos? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [black_bisho, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the bishos? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, black_bisho, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the bisho? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    board_state: list[list[ChessPiece]] = [
        [black_bisho, black_bisho, black_bisho],
        [black_bisho, black_bisho, black_bisho],
        [black_bisho, black_bisho, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the bishos? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    ####
    # White attacking_
    ####
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, white_bisho, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the bisho? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, white_bisho, EMPTY_PIECE],
        [white_bisho, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the bishos? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, white_bisho, white_bisho],
        [white_bisho, EMPTY_PIECE, white_bisho],
        [white_bisho, white_bisho, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the bishos? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [white_bisho, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the bisho? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, white_bisho, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the bisho? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [white_bisho, white_bisho, white_bisho],
        [white_bisho, white_bisho, white_bisho],
        [white_bisho, white_bisho, black_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king_ in danger from the bishos? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True


def test_in_danger_pawn__diag():
    ####
    # Black attacking_
    ####
    board_state: list[list[ChessPiece]] = [
        [black_pawn_, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_pawn_],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [black_pawn_, black_pawn_, black_pawn_],
        [black_pawn_, EMPTY_PIECE, black_pawn_],
        [black_pawn_, black_pawn_, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, black_pawn_, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    board_state: list[list[ChessPiece]] = [
        [black_pawn_, black_pawn_, black_pawn_],
        [black_pawn_, black_pawn_, black_pawn_],
        [black_pawn_, black_pawn_, white_king_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    ####
    # White attacking_
    ####
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, black_king_],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [white_pawn_, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: No
    assert chessboard_instance.in_danger(Position(0, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, black_king_],
        [EMPTY_PIECE, EMPTY_PIECE, white_pawn_],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: No
    assert chessboard_instance.in_danger(Position(0, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [white_pawn_, white_pawn_, black_king_],
        [white_pawn_, EMPTY_PIECE, white_pawn_],
        [white_pawn_, white_pawn_, white_pawn_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: No
    assert chessboard_instance.in_danger(Position(0, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, black_king_],
        [EMPTY_PIECE, white_pawn_, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: Yes
    assert chessboard_instance.in_danger(Position(0, 2)) is True

    board_state: list[list[ChessPiece]] = [
        [white_pawn_, white_pawn_, black_king_],
        [white_pawn_, white_pawn_, white_pawn_],
        [white_pawn_, white_pawn_, white_pawn_]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king_ in danger from the pawn_? Answer: Yes
    assert chessboard_instance.in_danger(Position(0, 2)) is True


def test_in_danger_pawn__en_passant():
    # Enpassant check

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [black_pawn_, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, white_pawn_, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn_ next to the Black pawn_
    chessboard_instance.move(Position(3, 1), Position(1, 1))

    # Is white pawn_ in danger from the black pawn_?
    # Answer: Yes, due to en passant
    assert chessboard_instance.in_danger(Position(1, 1)) is True

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [black_pawn_, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, white_pawn_, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn_ next to the Black pawn_
    chessboard_instance.move(Position(3, 1), Position(2, 1))
    chessboard_instance.move(Position(2, 1), Position(1, 1))

    # Is white pawn_ in danger from the black pawn_?
    # Answer: Yes, due to en passant
    assert chessboard_instance.in_danger(Position(1, 1)) is False

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [black_pawn_, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, white_pawn_, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn_ next to the Black pawn_
    chessboard_instance.move(Position(0, 0), Position(2, 0))

    # Is white pawn_ in danger from the black pawn_?
    # Answer: Yes, due to en passant
    assert chessboard_instance.in_danger(Position(2, 0)) is True

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [black_pawn_, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, white_pawn_, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn_ next to the Black pawn_
    chessboard_instance.move(Position(0, 0), Position(1, 0))
    chessboard_instance.move(Position(1, 0), Position(2, 0))

    # Is white pawn_ in danger from the black pawn_?
    # Answer: No, pawn_ took 2 moves to get into dest
    assert chessboard_instance.in_danger(Position(2, 0)) is False


def test_in_danger_knigh_threats():
    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, black_knigh, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Check so the attacked square matches the expected results.
    assert chessboard_instance.in_danger(Position(0, 0), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(0, 1), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(0, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(0, 3), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(0, 4), Color.WHITE) is False

    assert chessboard_instance.in_danger(Position(1, 0), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(1, 1), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(1, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(1, 3), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(1, 4), Color.WHITE) is True

    assert chessboard_instance.in_danger(Position(2, 0), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 1), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 3), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 4), Color.WHITE) is False

    assert chessboard_instance.in_danger(Position(3, 0), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(3, 1), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(3, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(3, 3), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(3, 4), Color.WHITE) is True

    assert chessboard_instance.in_danger(Position(4, 0), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(4, 1), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(4, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(4, 3), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(4, 4), Color.WHITE) is False

    # Same checks but full board as knigh should NOT be affected by collisions
    board_state: list[list[ChessPiece]] = [
        [white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_],
        [white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_],
        [white_pawn_, white_pawn_, black_knigh, white_pawn_, white_pawn_],
        [white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_],
        [white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_]
    ]
    chessboard_instance = Chessboard(board_state)

    # Check so the attacked square matches the expected results.
    assert chessboard_instance.in_danger(Position(0, 0), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(0, 1), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(0, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(0, 3), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(0, 4), Color.WHITE) is False

    assert chessboard_instance.in_danger(Position(1, 0), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(1, 1), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(1, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(1, 3), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(1, 4), Color.WHITE) is True

    assert chessboard_instance.in_danger(Position(2, 0), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 1), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 3), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(2, 4), Color.WHITE) is False

    assert chessboard_instance.in_danger(Position(3, 0), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(3, 1), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(3, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(3, 3), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(3, 4), Color.WHITE) is True

    assert chessboard_instance.in_danger(Position(4, 0), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(4, 1), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(4, 2), Color.WHITE) is False
    assert chessboard_instance.in_danger(Position(4, 3), Color.WHITE) is True
    assert chessboard_instance.in_danger(Position(4, 4), Color.WHITE) is False


def test_TBA():
    chessboard: list[list[ChessPiece]] = [
        # 0     1     2     3     4     5     6     7
        [black_rook_, black_knigh, black_bisho, black_queen, black_king_, black_bisho, black_knigh, black_rook_],  # 0 # noqa E501
        [black_pawn_, black_pawn_, black_pawn_, black_pawn_, black_pawn_, black_pawn_, black_pawn_, black_pawn_],  # 1 # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 2 # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 3 # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 4 # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 5 # noqa E501
        [white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_, white_pawn_],  # 6 # noqa E501
        [white_rook_, white_knigh, white_bisho, white_queen, white_king_, white_bisho, white_knigh, white_rook_],  # 7 # noqa E501
    ]

    board_refrence = Chessboard(chessboard)
    # check
    assert board_refrence.in_danger(Position(0, 0), Color.BLACK) is False
    assert board_refrence.in_danger(Position(0, 0), Color.WHITE) is False
    assert board_refrence.in_danger(Position(0, 1), Color.BLACK) is False
    assert board_refrence.in_danger(Position(0, 1), Color.WHITE) is True

    assert board_refrence.in_danger(Position(1, 1), Color.BLACK) is False
    assert board_refrence.in_danger(Position(3, 1), Color.BLACK) is False
    assert board_refrence.in_danger(Position(5, 1), Color.BLACK) is True

    board_refrence.add_piece(white_queen, Position(3, 3))
    assert board_refrence.in_danger(Position(1, 0), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 1), Color.BLACK) is True
    assert board_refrence.in_danger(Position(1, 2), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 3), Color.BLACK) is True
    assert board_refrence.in_danger(Position(1, 4), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 5), Color.BLACK) is True
    assert board_refrence.in_danger(Position(1, 6), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 7), Color.BLACK) is False
