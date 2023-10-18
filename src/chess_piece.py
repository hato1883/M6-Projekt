from enum import Enum
from typing import Any
from piece_color import Color
from piece_type import PieceType



class ChessPiece:

    def __init__(self, piece_color,piece_type):
        self.piece_type = piece_type
        self.piece_color = piece_color
        self.piece_has_moved = False

    def __str__(self):
        return f'{self.piece_color} {self.piece_type} {self.piece_has_moved}'
    
    def get_type(self):
        return self.piece_type.name

    def get_color(self):
        return self.piece_color.name
    
    def get_has_moved(self):
        return self.piece_has_moved

    def set_has_moved_true(self):
        self.piece_has_moved = True