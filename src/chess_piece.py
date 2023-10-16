from enum import Enum
from piece_color import Color
from piece_type import PieceType



class chess_piece:

    def __init__(self, piece_color,piece_type):
        self.piece_type = piece_type
        self.piece_color = piece_color

    def __str__(self):
        return f'{self.piece_color} {self.piece_type}'
    
    def getType(self):
        return self.piece_type.name

    def getColor(self):
        return self.piece_color.name