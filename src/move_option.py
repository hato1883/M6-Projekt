from enum import Enum

class MoveOption(Enum):
    # Moves along x/y axis
    TAKE = 1

    # Moves along y = x or y = -x diagonals
    PROTECTED = 2

    # Teleporting/leaping moves
    FIRST = 4
    
    def __str__(self):
        """Overriden to String method

        Returns Enum name such as COLLISION_AXIS_TAKE instead of Number 11"""
        return f'{self.name}'