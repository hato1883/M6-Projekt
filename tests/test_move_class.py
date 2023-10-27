import pytest  # noqa: F401
import sys
import os

current = os.path.dirname(__file__)
sys.path.append(current + "/../src")

from move_class import Move  # noqa: E402
from moveset_class import Moveset  # noqa: E402
from move_option_enum import MoveOption  # noqa: E402
from move_type_enum import MoveType  # noqa: E402


move = Move((1, 1),
            MoveType.ABSOLUTE,
            [MoveOption.CAN_TAKE])
move2 = Move((-1, -1),
             MoveType.COLLISION_DIAG,
             [MoveOption.CAN_TAKE, MoveOption.FIRST])
moveset = Moveset((1, 0),
                  [move,
                   move2])

print(moveset)
