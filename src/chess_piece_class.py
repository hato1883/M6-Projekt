from piece_color_enum import Color
from piece_type_enum import PieceType


class ChessPiece:

    def __init__(self, piece_color: Color, piece_type: PieceType):
        self.piece_type = piece_type
        self.piece_color = piece_color
        self.piece_has_moved = False

    def get_type(self) -> PieceType:
        return self.piece_type

    def get_color(self) -> Color:
        return self.piece_color

    def get_has_moved(self) -> bool:
        return self.piece_has_moved

    def set_has_moved_true(self):
        self.piece_has_moved = True

    def __str__(self):
        # prints □ if piece is black or ■ if piece is white
        # Followed by First letter of piece type
        # Followed by a dash, then F/T to represent if piece has moved.
        text = ""
        if self.piece_color is Color.WHITE:
            text = f"{text}■{str(self.piece_type.name)[0]}-"
        else:
            text = f"{text}□{str(self.piece_type.name)[0]}-"

        if self.get_has_moved():
            text = f"{text}T"
        else:
            text = f"{text}F"

        return text

    def __repr__(self) -> str:
        text = f"<ChessPiece:{self.piece_color}"
        text = f"{text} {self.piece_type}"
        text = f"{text}, {self.piece_has_moved}>"
        return text

    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, self.__class__):
            return self.__dict__ == __value.__dict__
        else:
            return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)


EMPTY_PIECE = ChessPiece(Color.EMPTY, PieceType.EMPTY)
