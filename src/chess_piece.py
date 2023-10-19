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
        # prints □ if piece is black or ■ if piece is white
        # Followed by First letter of piece type
        # Followed by a dash, then F/T to represent if piece has moved.
        return f'{"■" if self.piece_color.name == Color.WHITE.name else "□"}{str(self.piece_type.name)[0]}-{"T" if self.piece_has_moved else "F"}'
    
    def get_type(self):
        return self.piece_type

    def get_color(self):
        return self.piece_color
    
    def get_has_moved(self):
        return self.piece_has_moved

    def set_has_moved_true(self):
        self.piece_has_moved = True