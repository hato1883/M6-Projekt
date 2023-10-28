from enum import Enum


class Status(Enum):
    # Err Origin was empty.
    EMPTY_ORIGIN = 1

    # Err Invalid move
    INVALID_MOVE = 2

    # Err Invalid move
    IN_CHECK = 3

    # Err Invalid move
    IN_CHECKMATE = 4

    # Pawn can promote due to move
    PAWN_PROMOTION = 5

    # Pawn can promote due to move
    SUCCESS = 6

    def __str__(self):
        """Overriden to String method

        Returns Enum name such as PAWN_PROMOTION instead of Number 2"""
        return f'{self.name}'

    def __repr__(self) -> str:
        return self.__str__()
