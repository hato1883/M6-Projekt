from enum import Enum

from position_class import Position


class Color (Enum):
    WHITE = Position(1, 1)
    BLACK = Position(-1, 1)
    EMPTY = Position(0, 0)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return self.__str__()
