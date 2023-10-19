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

# Test if create board returns a 2d list filed with None
def test_create_board():
    chessboard_ref = Chessboard()
    expected_board = [
        [None]
        ]
    chessboard_ref.create_board(1)
    
    assert len(expected_board) == len(chessboard_ref.chessboard_list)
    for row in range(len(expected_board)):
        # Check amount of columns in the row are equal
        assert len(expected_board[row]) == len(chessboard_ref.chessboard_list[row])
        for col in range(len(expected_board)):
            assert chessboard_ref.chessboard_list[row][col] == None
    
    expected_board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
        ]
    chessboard_ref.create_board() # default size is 8

    assert len(expected_board) == len(chessboard_ref.chessboard_list)
    for row in range(len(expected_board)):
        # Check amount of columns in the row are equal
        assert len(expected_board[row]) == len(chessboard_ref.chessboard_list[row])
        for col in range(len(expected_board)):
            assert chessboard_ref.chessboard_list[row][col] == None

