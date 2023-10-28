

from position_class import Position


def clamp(input: int, min_value: int, max_value: int) -> int:
    """Clamp the input between min and max inclusive.

    input of 10 with min -1 and max 1
    will return a 1"""
    return min(max_value, max(min_value, input))


def in_bounds(origin: Position,
              offset: Position,
              min: int = 0, max: int = 8) -> bool:
    """Checks if the given position would land
    Outside of the given min and max (Default is 0 and 8)

    Returns True if result is less than max but larger than min
    """
    if origin.row + offset.row >= max:
        # Row to large
        return False
    if origin.row + offset.row < min:
        # Row to small
        return False

    if origin.col + offset.col >= max:
        # Col to large
        return False
    if origin.col + offset.col < min:
        # Col to small
        return False

    return True
