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


def test_in_danger_rook_threats():
    """Tests in_danger() method using only rook pieces"""
    ####
    # Black attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [b_ro, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rook? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, b_ro, EMPTY_PIECE],
        [b_ro, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [b_ro, b_ro, EMPTY_PIECE],
        [b_ro, b_ro, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, b_ro],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [b_ro, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rook? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [b_ro, b_ro, b_ro],
        [b_ro, b_ro, b_ro],
        [b_ro, b_ro, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    ####
    # White attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [w_ro, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rook? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, w_ro, EMPTY_PIECE],
        [w_ro, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [w_ro, w_ro, EMPTY_PIECE],
        [w_ro, w_ro, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, w_ro],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [w_ro, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rook? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [w_ro, w_ro, w_ro],
        [w_ro, w_ro, w_ro],
        [w_ro, w_ro, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True


def test_in_danger_bishop_threats():
    """Tests in_danger() method with only bishop pieces"""

    ####
    # Black attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, b_bi, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishop? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, b_bi, EMPTY_PIECE],
        [b_bi, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, b_bi, b_bi],
        [b_bi, EMPTY_PIECE, b_bi],
        [b_bi, b_bi, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [b_bi, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, b_bi, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishop? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    board_state: list[list[ChessPiece]] = [
        [b_bi, b_bi, b_bi],
        [b_bi, b_bi, b_bi],
        [b_bi, b_bi, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    ####
    # White attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, w_bi, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishop? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, w_bi, EMPTY_PIECE],
        [w_bi, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, w_bi, w_bi],
        [w_bi, EMPTY_PIECE, w_bi],
        [w_bi, w_bi, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    # Now attack the King

    board_state: list[list[ChessPiece]] = [
        [w_bi, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishop? Answer: Yes

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, w_bi, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishop? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    assert chessboard_instance.in_danger(Position(2, 2)) is True
    board_state: list[list[ChessPiece]] = [
        [w_bi, w_bi, w_bi],
        [w_bi, w_bi, w_bi],
        [w_bi, w_bi, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishops? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True


def test_in_danger_pawn_diag():
    ####
    # Black attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [b_pa, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_pa],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [b_pa, b_pa, b_pa],
        [b_pa, EMPTY_PIECE, b_pa],
        [b_pa, b_pa, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: No
    assert chessboard_instance.in_danger(Position(2, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, b_pa, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    board_state: list[list[ChessPiece]] = [
        [b_pa, b_pa, b_pa],
        [b_pa, b_pa, b_pa],
        [b_pa, b_pa, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: Yes
    assert chessboard_instance.in_danger(Position(2, 2)) is True

    ####
    # White attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, b_ki],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [w_pa, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: No
    assert chessboard_instance.in_danger(Position(0, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, b_ki],
        [EMPTY_PIECE, EMPTY_PIECE, w_pa],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: No
    assert chessboard_instance.in_danger(Position(0, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [w_pa, w_pa, b_ki],
        [w_pa, EMPTY_PIECE, w_pa],
        [w_pa, w_pa, w_pa]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: No
    assert chessboard_instance.in_danger(Position(0, 2)) is False

    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, b_ki],
        [EMPTY_PIECE, w_pa, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: Yes
    assert chessboard_instance.in_danger(Position(0, 2)) is True

    board_state: list[list[ChessPiece]] = [
        [w_pa, w_pa, b_ki],
        [w_pa, w_pa, w_pa],
        [w_pa, w_pa, w_pa]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the pawn? Answer: Yes
    assert chessboard_instance.in_danger(Position(0, 2)) is True


def test_in_danger_pawn_en_passant():
    # Enpassant check

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [b_pa, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, w_pa, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn next to the Black pawn
    chessboard_instance.move(Position(3, 1), Position(1, 1))

    # Is white pawn in danger from the black pawn?
    # Answer: Yes, due to en passant
    assert chessboard_instance.in_danger(Position(1, 1)) is True

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [b_pa, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, w_pa, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn next to the Black pawn
    chessboard_instance.move(Position(3, 1), Position(2, 1))
    chessboard_instance.move(Position(2, 1), Position(1, 1))

    # Is white pawn in danger from the black pawn?
    # Answer: Yes, due to en passant
    assert chessboard_instance.in_danger(Position(1, 1)) is False

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [b_pa, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, w_pa, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn next to the Black pawn
    chessboard_instance.move(Position(0, 0), Position(2, 0))

    # Is white pawn in danger from the black pawn?
    # Answer: Yes, due to en passant
    assert chessboard_instance.in_danger(Position(2, 0)) is True

    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [b_pa, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, w_pa, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]
    ]
    chessboard_instance = Chessboard(board_state)

    # Move White pawn next to the Black pawn
    chessboard_instance.move(Position(0, 0), Position(1, 0))
    chessboard_instance.move(Position(1, 0), Position(2, 0))

    # Is white pawn in danger from the black pawn?
    # Answer: No, pawn took 2 moves to get into dest
    assert chessboard_instance.in_danger(Position(2, 0)) is False


def test_in_danger_knight_threats():
    # Start state, board must be square
    board_state: list[list[ChessPiece]] = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
        [EMPTY_PIECE, EMPTY_PIECE, b_kn, EMPTY_PIECE, EMPTY_PIECE],
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

    # Same checks but full board as knight should NOT be affected by collisions
    board_state: list[list[ChessPiece]] = [
        [w_pa, w_pa, w_pa, w_pa, w_pa],
        [w_pa, w_pa, w_pa, w_pa, w_pa],
        [w_pa, w_pa, b_kn, w_pa, w_pa],
        [w_pa, w_pa, w_pa, w_pa, w_pa],
        [w_pa, w_pa, w_pa, w_pa, w_pa]
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
        [b_ro, b_kn, b_bi, b_qu, b_ki, b_bi, b_kn, b_ro],  # 0
        [b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa],  # 1
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 2 # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 3 # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 4 # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # 5 # noqa E501
        [w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa],  # 6
        [w_ro, w_kn, w_bi, w_qu, w_ki, w_bi, w_kn, w_ro],  # 7
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

    board_refrence.add_piece(w_qu, Position(3, 3))
    assert board_refrence.in_danger(Position(1, 0), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 1), Color.BLACK) is True
    assert board_refrence.in_danger(Position(1, 2), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 3), Color.BLACK) is True
    assert board_refrence.in_danger(Position(1, 4), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 5), Color.BLACK) is True
    assert board_refrence.in_danger(Position(1, 6), Color.BLACK) is False
    assert board_refrence.in_danger(Position(1, 7), Color.BLACK) is False
