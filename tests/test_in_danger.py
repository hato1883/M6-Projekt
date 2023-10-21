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
# Tests if in_danger() works as intended

def test_in_danger_rook_threats():
    """Tests in_danger() method using only rook pieces"""
    ####
    # Black attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [b_ro, None, None],
        [None, None, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rook? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == False

    board_state: list[list[ChessPiece]] = [
        [None, b_ro, None],
        [b_ro, None, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == False

    board_state: list[list[ChessPiece]] = [
        [b_ro, b_ro, None],
        [b_ro, b_ro, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == False

    ## Now attack the King

    board_state: list[list[ChessPiece]] = [
        [None, None, b_ro],
        [None, None, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: Yes

    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True
    board_state: list[list[ChessPiece]] = [
        [None, None, None],
        [None, None, None],
        [b_ro, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rook? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True

    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True
    board_state: list[list[ChessPiece]] = [
        [b_ro, b_ro, b_ro],
        [b_ro, b_ro, b_ro],
        [b_ro, b_ro, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the rooks? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True
    

    ####
    # White attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [w_ro, None, None],
        [None, None, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rook? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == False

    board_state: list[list[ChessPiece]] = [
        [None, w_ro, None],
        [w_ro, None, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == False

    board_state: list[list[ChessPiece]] = [
        [w_ro, w_ro, None],
        [w_ro, w_ro, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == False

    ## Now attack the King

    board_state: list[list[ChessPiece]] = [
        [None, None, w_ro],
        [None, None, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: Yes

    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True
    board_state: list[list[ChessPiece]] = [
        [None, None, None],
        [None, None, None],
        [w_ro, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rook? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True

    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True
    board_state: list[list[ChessPiece]] = [
        [w_ro, w_ro, w_ro],
        [w_ro, w_ro, w_ro],
        [w_ro, w_ro, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the rooks? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True


def test_in_danger_bishop_threats():
    """Tests in_danger() method with only bishop pieces"""

    ####
    # Black attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [None, b_bi, None],
        [None, None, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishop? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == False

    board_state: list[list[ChessPiece]] = [
        [None, b_bi, None],
        [b_bi, None, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == False

    board_state: list[list[ChessPiece]] = [
        [None, b_bi, b_bi],
        [b_bi, None, b_bi],
        [b_bi, b_bi, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == False

    ## Now attack the King

    board_state: list[list[ChessPiece]] = [
        [b_bi, None, None],
        [None, None, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: Yes

    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True
    board_state: list[list[ChessPiece]] = [
        [None, None, None],
        [None, b_bi, None],
        [None, None, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishop? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True

    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True
    board_state: list[list[ChessPiece]] = [
        [b_bi, b_bi, b_bi],
        [b_bi, b_bi, b_bi],
        [b_bi, b_bi, w_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is white king in danger from the bishops? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.WHITE) == True
    
    
    ####
    # White attacking
    ####
    board_state: list[list[ChessPiece]] = [
        [None, w_bi, None],
        [None, None, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishop? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == False

    board_state: list[list[ChessPiece]] = [
        [None, w_bi, None],
        [w_bi, None, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == False

    board_state: list[list[ChessPiece]] = [
        [None, w_bi, w_bi],
        [w_bi, None, w_bi],
        [w_bi, w_bi, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishops? Answer: No
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == False

    ## Now attack the King

    board_state: list[list[ChessPiece]] = [
        [w_bi, None, None],
        [None, None, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishop? Answer: Yes

    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True
    board_state: list[list[ChessPiece]] = [
        [None, None, None],
        [None, w_bi, None],
        [None, None, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishop? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True

    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True
    board_state: list[list[ChessPiece]] = [
        [w_bi, w_bi, w_bi],
        [w_bi, w_bi, w_bi],
        [w_bi, w_bi, b_ki]
    ]
    chessboard_instance = Chessboard(board_state)
    # Is black king in danger from the bishops? Answer: Yes
    assert chessboard_instance.in_danger(Position(2,2), Color.BLACK) == True


def test_TBA():
    chessboard: list[list[ChessPiece]] = [
        # 0     1     2     3     4     5     6     7
        [b_ro, b_kn, b_bi, b_qu, b_ki, b_bi, b_kn, b_ro], # 0
        [b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa], # 1
        [None, None, None, None, None, None, None, None], # 2
        [None, None, None, None, None, None, None, None], # 3
        [None, None, None, None, None, None, None, None], # 4
        [None, None, None, None, None, None, None, None], # 5
        [w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa], # 6
        [w_ro, w_kn, w_bi, w_qu, w_ki, w_bi, w_kn, w_ro], # 7
    ]

    board_refrence = Chessboard(chessboard)
    # check
    assert board_refrence.in_danger(Position(0,0), Color.BLACK) == False
    assert board_refrence.in_danger(Position(0,0), Color.WHITE) == False
    assert board_refrence.in_danger(Position(0,1), Color.BLACK) == False
    assert board_refrence.in_danger(Position(0,1), Color.WHITE) == True

    assert board_refrence.in_danger(Position(1,1), Color.BLACK) == False
    assert board_refrence.in_danger(Position(3,1), Color.BLACK) == False
    assert board_refrence.in_danger(Position(5,1), Color.BLACK) == False

    board_refrence.add_piece(w_qu, Position(3,3))
    assert board_refrence.in_danger(Position(1,0), Color.BLACK) == False
    assert board_refrence.in_danger(Position(1,1), Color.BLACK) == True
    assert board_refrence.in_danger(Position(1,2), Color.BLACK) == False
    assert board_refrence.in_danger(Position(1,3), Color.BLACK) == True
    assert board_refrence.in_danger(Position(1,4), Color.BLACK) == False
    assert board_refrence.in_danger(Position(1,5), Color.BLACK) == True
    assert board_refrence.in_danger(Position(1,6), Color.BLACK) == False
    assert board_refrence.in_danger(Position(1,7), Color.BLACK) == False