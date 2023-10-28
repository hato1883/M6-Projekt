import pytest  # noqa: F401
import sys
import os

current = os.path.dirname(__file__)
sys.path.append(current + "/../src")

from chessboard import Chessboard  # noqa: E402
from chess_piece_class import EMPTY_PIECE, ChessPiece  # noqa: E402
from piece_color_enum import Color  # noqa: E402
from piece_type_enum import PieceType  # noqa: E402


# Test if create board gives us a 2d list filled with EMPTY_PIECE elements
# Also test if Chessboard(list[list[]]) works as intended
def test_create_board():
    """Tests create_board(size)

    tests both for size 1 and size 8"""
    chessboard_ref = Chessboard()
    expected_board = [
        [EMPTY_PIECE]
        ]
    expected_ref = Chessboard(expected_board)
    chessboard_ref.create_board(1)

    # check if loaded 2d list is equal to created
    assert expected_ref == chessboard_ref

    # check if 2d list is deep equal to created
    assert len(expected_board) == len(chessboard_ref.get_chessboard())
    for row in range(len(expected_board)):
        # Check amount of columns in the row are equal
        assert len(expected_board[row]) == len(chessboard_ref.get_chessboard()[row])  # noqa E501
        for col in range(len(expected_board)):
            assert chessboard_ref.get_chessboard()[row][col] is EMPTY_PIECE

    # Create a 2d list of 8x8
    expected_board = [
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]  # noqa E501
        ]
    # load it into a Chessboard instance
    expected_ref = Chessboard(expected_board)

    # Create a default empty board
    chessboard_ref.create_board()  # default size is 8

    # check if loaded 2d list is equal to created
    assert expected_ref == chessboard_ref

    # check if 2d list is deep equal to created
    assert len(expected_board) == len(chessboard_ref.get_chessboard())
    for row in range(len(expected_board)):
        # Check amount of columns in the row are equal
        assert len(expected_board[row]) == len(chessboard_ref.get_chessboard()[row])  # noqa E501

        for col in range(len(expected_board)):
            assert expected_board[row][col] == chessboard_ref.get_chessboard()[row][col]  # noqa E501


# Test if we get a default chessboard
# Also test if Chessboard(list[list[]]) works as intended
def test_create_default_board():
    """tests create_default_board

    compares result with given chess board bellow"""
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
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
        [w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa],
        [w_ro, w_kn, w_bi, w_qu, w_ki, w_bi, w_kn, w_ro],
    ]
    # load it into a Chessboard instance
    expected_ref = Chessboard(expected_board)
    chessboard_ref = Chessboard()
    chessboard_ref.create_default_board()

    # check if loaded 2d list is equal to created
    assert expected_ref == chessboard_ref

    # check if 2d list is deep equal to created
    assert len(expected_board) == len(chessboard_ref.get_chessboard())
    for row in range(len(expected_board)):
        # Check amount of columns in the row are equal
        assert len(expected_board[row]) == len(chessboard_ref.get_chessboard()[row])  # noqa E501

        for col in range(len(expected_board)):
            assert expected_board[row][col] == chessboard_ref.get_chessboard()[row][col]  # noqa E501
