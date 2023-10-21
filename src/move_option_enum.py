from enum import Enum

class MoveOption(Enum):
    # Can the piece take Enemy on destination
    TAKE = 1

    # Dose the destination and path need to be safe
    PROTECTED = 2

    # Must piece be unmoved
    FIRST = 4

    # Dose move propegate to edges
    PROPEGATES = 8
    
    def __str__(self):
        """Overriden to String method

        Returns Enum name such as TAKE instead of Number 1"""
        return f'{self.name}'