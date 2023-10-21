from enum import Enum

class MoveType(Enum):
    # Moves along x/y axis
    COLLISION_AXIS = 1

    # Moves along y = x or y = -x diagonals
    COLLISION_DIAG = 2

    # Teleporting/leaping moves
    ABSOLUTE = 4

    # Special Moves
    PAWN_EN_PASSANT = 8
    KING_CASTLE = 16

    
    def __str__(self):
        """Overriden to String method

        Returns Enum name such as COLLISION_AXIS_TAKE instead of Number 11"""
        return f'{self.name}'