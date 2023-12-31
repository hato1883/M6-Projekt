from chess_piece_class import EMPTY_PIECE
from position_class import Position


def add_coordinate_pairs(t1: Position, t2: Position):
    return Position(t1.row + t2.row, t1.col + t2.col)


def return_direction_vector(origin: Position,
                            destination: Position) -> Position:
    """Compares destination with origin,
    returns unit vector pointing from origin to destination"""

    d_row = destination.row - origin.row
    d_column = destination.col - origin.col

    row_step = 0
    colum_step = 0

    if d_row > 0:
        row_step = 1
    elif d_row < 0:
        row_step = -1

    if d_column > 0:
        colum_step = 1
    elif d_column < 0:
        colum_step = -1

    return Position(row_step, colum_step)


def diagonal_move(origin, destination):
    """Checks if move is diagonal"""
    d_row = abs(destination.row - origin.row)
    d_column = abs(destination.col - origin.col)
    return d_row == d_column


def axis_move(origin, destination):
    """Check if move is straight line"""
    d_row = destination.row - origin.row
    d_column = destination.col - origin.col

    return d_row != 0 and d_column == 0 or d_row == 0 and d_column != 0


def obstacle_in_path(chessboard: list,
                     origin: Position,
                     destination: Position,
                     disregard_dest: bool,
                     debug: bool = False):

    step_vector = return_direction_vector(origin, destination)
    next_square = add_coordinate_pairs(origin, step_vector)

    if disregard_dest:
        do_not_check_square = destination
        if next_square == do_not_check_square:
            return False
    else:
        do_not_check_square = add_coordinate_pairs(destination, step_vector)

    if debug:
        print(f"Diagonal move: {diagonal_move(origin, destination)}")
        print(f"Vertical/Horizontal move: {axis_move(origin,destination)}")
        print(f"| Origin: {origin} | Destination: {destination} | Step vector: {step_vector} |")  # noqa
        print("****Checking****")

    if next_square == do_not_check_square:
        print("Origin == destination, invalid move!")
        return True

    while next_square != do_not_check_square:

        if chessboard[next_square.row][next_square.col] is EMPTY_PIECE:

            if debug:
                print(f"{next_square} is empty")

            next_square = add_coordinate_pairs(next_square, step_vector)
            continue

        if debug:
            print(f"{next_square} is not empty")
        return True

    return False
