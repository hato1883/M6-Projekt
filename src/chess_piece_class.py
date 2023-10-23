from enum import Enum
from typing import Any
from piece_color_enum import Color
from piece_type_enum import PieceType



class ChessPiece:

    def __init__(self, piece_color,piece_type):
        self.piece_type = piece_type
        self.piece_color = piece_color
        self.piece_has_moved = False

    def get_type(self):
        return self.piece_type

    def get_color(self):
        return self.piece_color
    
    def get_has_moved(self):
        return self.piece_has_moved

    def set_has_moved_true(self):
        self.piece_has_moved = True

    def __str__(self):
        # prints □ if piece is black or ■ if piece is white
        # Followed by First letter of piece type
        # Followed by a dash, then F/T to represent if piece has moved.
        return f'{"■" if self.piece_color.name is Color.WHITE.name else "□"}{str(self.piece_type.name)[0]}-{"T" if self.piece_has_moved else "F"}'
    
    def __repr__(self) -> str:
        return f"<ChessPiece:{self.piece_color} {self.piece_type}, {self.piece_has_moved}>"

    def __eq__(self, __value: object) -> bool:
        
        if isinstance(__value, self.__class__):
            return self.__dict__ == __value.__dict__
        else:
            return NotImplemented

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
