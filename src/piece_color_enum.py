from enum import Enum

class Color (Enum):
    WHITE = 0
    BLACK = 1

    def __str__(self) -> str:
        return f"{self.name}"
    def __repr__(self) -> str:
        return self.__str__()