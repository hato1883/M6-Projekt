from enum import Enum


class MoveOption(Enum):
    # Can the piece take Enemy on destination
    CAN_TAKE = 1

    # Can the piece take Enemy on destination
    MUST_TAKE = 2

    # Dose the destination and path need to be safe
    PROTECTED = 4

    # Must piece be unmoved
    FIRST = 8

    # Dose move propegate to edges
    PROPEGATES = 16

    def __str__(self):
        """Overriden to String method

        Returns Enum name such as CAN_TAKE instead of Number 1"""
        return f'{self.name}'

    def __repr__(self) -> str:
        return self.__str__()
