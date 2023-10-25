from abc import ABC, abstractmethod

from chess_piece_class import ChessPiece
from position_class import Position


class NarrationInterface(ABC):

    @abstractmethod
    def generate_move_text(origin: Position,
                           destination: Position,
                           moved_piece: ChessPiece,
                           attacked_piece: ChessPiece) -> str:
        """Generates a description for the given move

        Inputs:
        origin - Position object of moved piece starting row and column
        destination - Position object of containing destination
        row and column of the moved piece
        moved_piece - ChessPiece object of what piece got moved
        attacked_piece - ChessPiece object of what piece got killed in move.
        Can be None

        returns: A String
        """

    @classmethod
    def index_to_alpha_numeral(cls, position: Position) -> str:
        """Converts list index into Alpha numeric row col
        from row: 0-n and col: 0-n
        into row: 1-(n+1) and col: A-Z

        Undefined for columns larger than 26

        returns a string such as A1 or H8 etc"""
        board_row = (8-position.row)
        board_col = chr(ord('a') + position.col)
        return f"{board_col}{board_row}"
