from enum import Enum


class Status(Enum):
    # Err Origin was empty.
    EMPTY_ORIGIN = 1

    # Err Invalid move
    INVALID_MOVE = 2

    # Move was invalid, Player is in a check but can move out of check
    IN_CHECK = 3

    # No valid moves, Player is checkmated
    IN_CHECKMATE = 4

    # No valid moves, Player is in a Draw
    DRAW = 5

    # Pawn can promote due to move
    PAWN_PROMOTION = 6

    # Pawn can promote due to move
    SUCCESS = 7

    def __str__(self):
        """Overriden to String method

        Returns Enum name such as PAWN_PROMOTION instead of Number 2"""
        return f'{self.name}'

    def __repr__(self) -> str:
        return self.__str__()
