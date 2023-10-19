from enum import Enum
from move_type import MoveType
from move_option import MoveOption

class PieceType(Enum):
    ####
    # Pawn Move List
    ####
    PAWN = [
        # Pawn walking up
        # - o -
        # - - -
        # - * -
            (   # Offset
                (2, 0), # 2 steps up, same colum
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.FIRST])
                ]
            ),

        # Pawn attacking left
        # - - -
        # x - -
        # - * -
            (   # Offset
                (1,-1), # 1 step up, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE]),
                    (MoveType.PAWN_EN_PASSANT, [])
                ]
            ),

        # Pawn walking up
        # - - -
        # - o -
        # - * -
            (
                (1, 0),  # Offset
                [   # Moves
                    (MoveType.COLLISION_AXIS, [])
                ]
            ),

        # Pawn attacking right
        # - - -
        # - - x
        # - * -
            (
                (1, 1),
                [
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE]),
                    (MoveType.PAWN_EN_PASSANT, [])
                ]
            )
            ]
    

    ####
    # Knight Move List
    ####
    KNIGHT = [
        # Knight T facing up
        # - x - x -
        # - - - - -
        # - - * - -
        # - - - - -
        # - - - - -
            (   # Offset
                (2, -1), # 2 steps up, 1 step left
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            ),

            (   # Offset
                (2, 1), # 2 step up, 1 step right
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            ),

        # Knight T facing right
        # - - - - -
        # - - - - x
        # - - * - -
        # - - - - x
        # - - - - -
            (   # Offset
                (1, 2),  # 1 step up, 2 steps right
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            ),

            # Diag take + en passant
            (   # Offset
                (-1, 2),  # 1 step down, 2 steps right
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            ),

        # Knight T facing down
        # - - - - -
        # - - - - -
        # - - * - -
        # - - - - -
        # - x - x -
            (   # Offset
                (-2, -1), # 2 steps down, same left
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            ),

            (   # Offset
                (-2, 1), # 2 steps down, 1 step right
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            ),

        # Knight T facing left
        # - - - - -
        # x - - - -
        # - - * - -
        # x - - - -
        # - - - - -
            (   # Offset
                (1, -2), # 1 step up, 2 steps left
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            ),

            # Diag take + en passant
            (   # Offset
                (-1, -2), # 1 step down, 2 steps left
                [   # Moves
                    (MoveType.ABSOLUTE, [MoveOption.TAKE])
                ]
            )
            ]
    

    ####
    # Bishop Move List
    ####
    BISHOP = [
            # Bishop attacking diag
            # x - -
            # - * -
            # - - -
            (   # Offset
                (1, -1), # 1 step up, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - x
            # - * -
            # - - -
            (   # Offset
                (1, 1), # 1 step up, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - -
            # - * -
            # - - x
            (   # Offset
                (-1, 1), # 1 step down, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - -
            # - * -
            # x - -
            (   # Offset
                (-1, -1), # 1 step down, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            )
            ]
    

    ####
    # Rook Move List
    ####
    ROOK = [
            # Rook attacking y-axis up
            # - x -
            # - * -
            # - - -
            (   # Offset
                (1, 0), # 1 step up, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - -
            # - * x
            # - - -
            (   # Offset
                (0, 1), # same row, 1 step right
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - -
            # - * -
            # - x -
            (   # Offset
                (-1, 0), # 1 step down, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - -
            # x * -
            # - - -
            (   # Offset
                (-1, 1), # same row, 1 step left
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            )
            ]
    

    ####
    # QUEEN Move List
    ####
    QUEEN = [
            # Queen attacking diag
            # x - -
            # - * -
            # - - -
            (   # Offset
                (1, -1), # 1 step up, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),
            # Queen attacking y-axis up
            # - x -
            # - * -
            # - - -
            (   # Offset
                (1, 0), # 1 step up, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking diag
            # - - x
            # - * -
            # - - -
            (   # Offset
                (1, 1), # 1 step up, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking x-axis
            # - - -
            # - * x
            # - - -
            (   # Offset
                (0, 1), # same row, 1 step right
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking diag
            # - - -
            # - * -
            # - - x
            (   # Offset
                (-1, 1), # 1 step down, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking y-axis
            # - - -
            # - * -
            # - x -
            (   # Offset
                (-1, 0), # 1 step down, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - -
            # - * -
            # x - -
            (   # Offset
                (-1, -1), # 1 step down, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking x-axis
            # - - -
            # x * -
            # - - -
            (   # Offset
                (0, -1), # same row, 1 step left
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROPEGATES])
                ]
            )
            ]
    

    ####
    # King Move List
    ####
    KING = [
            # KING attacking diag
            # - x - - -
            # - - * - -
            # - - - - -
            (   # Offset
                (1, -1), # 1 step up, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),
            # KING attacking y-axis up
            # - - x - -
            # - - * - -
            # - - - - -
            (   # Offset
                (1, 0), # 1 step up, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),

            # KING attacking diag
            # - - - x -
            # - - * - -
            # - - - - -
            (   # Offset
                (1, 1), # 1 step up, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # - - * x -
            # - - - - -
            (   # Offset
                (0, 1), # same row, 1 step right
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),

            # KING attacking diag
            # - - - - -
            # - - * - -
            # - - - x -
            (   # Offset
                (-1, 1), # 1 step down, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),

            # KING attacking y-axis
            # - - - - -
            # - - * - -
            # - - x - -
            (   # Offset
                (-1, 0), # 1 step down, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),

            # KING attacking diag
            # - - - - -
            # - - * - -
            # - x - - -
            (   # Offset
                (-1, -1), # 1 step down, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # - x * - -
            # - - - - -
            (   # Offset
                (0, -1), # same row, 1 step left
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.TAKE, MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # s - * - -
            # - - - - -
            (   # Offset
                (0, -2), # same row, 2 steps left
                [   # Moves
                    (MoveType.KING_CASTLE, [MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # - - * - s
            # - - - - -
            (   # Offset
                (0, 2), # same row, 2 steps right
                [   # Moves
                    (MoveType.KING_CASTLE, [MoveOption.PROTECTED])
                ]
            )
            ]
    

    def __str__(self):
        """Overriden to String method

        Returns Enum name such as KING instead of object refrense"""
        return f'{self.name}'