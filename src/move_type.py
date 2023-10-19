from enum import Enum

class MoveType(Enum):
    # Moves along x/y axis
    COLLISION_AXIS_TAKE = 11
    COLLISION_AXIS_MOVE = 12

    # Moves along x/y axis to ungaurded squares
    PROTECTED_COLLISION_AXIS_TAKE = 13
    PROTECTED_COLLISION_AXIS_MOVE = 14


    # Moves along y = x or y = -x diagonals
    COLLISION_DIAG_TAKE = 21
    COLLISION_DIAG_MOVE = 22

    # Moves along y = x or y = -x diagonals to ungaurded squares
    PROTECTED_COLLISION_DIAG_TAKE = 23
    PROTECTED_COLLISION_DIAG_MOVE = 24


    # Teleporting/leaping moves
    ABSOLUTE_TAKE = 31
    ABSOLUTE_MOVE = 32

    # Teleporting/leaping moves to ungaurded squares
    PROTECTED_ABSOLUTE_TAKE = 33
    PROTECTED_ABSOLUTE_MOVE = 34


    # Special Moves
    PAWN_EN_PASSANT = 111
    KING_CASTLE = 121

    
    def __str__(self):
        """Overriden to String method

        Returns Enum name such as COLLISION_AXIS_TAKE instead of Number 11"""
        return f'{self.name}'