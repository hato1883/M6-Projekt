from enum import Enum
from move_type_enum import MoveType
from move_option_enum import MoveOption


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
            (-2, 0),  # 2 steps up, same colum
            [   # Moves
                (MoveType.COLLISION_AXIS, [MoveOption.FIRST])
            ]
        ),

        # Pawn attacking left
        # - - -
        # x - -
        # - * -
        (   # Offset
            (-1, -1),  # 1 step up, 1 step left
            [   # Moves
                (MoveType.COLLISION_DIAG, [MoveOption.MUST_TAKE]),
                (MoveType.PAWN_EN_PASSANT, [])
            ]
        ),

        # Pawn walking up
        # - - -
        # - o -
        # - * -
        (   # Offset
            (-1, 0),  # 1 step up, same col
            [   # Moves
                (MoveType.COLLISION_AXIS, [])
            ]
        ),

        # Pawn attacking right
        # - - -
        # - - x
        # - * -
        (   # Offset
            (-1, 1),  # 1 step up, same col
            [
                (MoveType.COLLISION_DIAG, [MoveOption.MUST_TAKE]),
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
            (-2, -1),  # 2 steps up, 1 step left
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
            ]
        ),

        (   # Offset
            (-2, 1),  # 2 step up, 1 step right
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
            ]
        ),

        # Knight T facing right
        # - - - - -
        # - - - - x
        # - - * - -
        # - - - - x
        # - - - - -
        (   # Offset
            (-1, 2),  # 1 step up, 2 steps right
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
            ]
        ),

        # Diag take + en passant
        (   # Offset
            (1, 2),  # 1 step down, 2 steps right
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
            ]
        ),

        # Knight T facing down
        # - - - - -
        # - - - - -
        # - - * - -
        # - - - - -
        # - x - x -
        (   # Offset
            (2, -1),  # 2 steps down, same left
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
            ]
        ),

        (   # Offset
            (2, 1),  # 2 steps down, 1 step right
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
            ]
        ),

        # Knight T facing left
        # - - - - -
        # x - - - -
        # - - * - -
        # x - - - -
        # - - - - -
        (   # Offset
            (-1, -2),  # 1 step up, 2 steps left
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
            ]
        ),

        # Diag take + en passant
        (   # Offset
            (1, -2),  # 1 step down, 2 steps left
            [   # Moves
                (MoveType.ABSOLUTE, [MoveOption.CAN_TAKE])
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
            (-1, -1),  # 1 step up, 1 step left
            [   # Moves
                (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                           MoveOption.PROPEGATES])
            ]
        ),

        # Bishop attacking diag
        # - - x
        # - * -
        # - - -
        (   # Offset
            (-1, 1),  # 1 step up, 1 step right
            [   # Moves
                (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                           MoveOption.PROPEGATES])
            ]
        ),

        # Bishop attacking diag
        # - - -
        # - * -
        # - - x
        (   # Offset
            (1, 1),  # 1 step down, 1 step right
            [   # Moves
                (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                           MoveOption.PROPEGATES])
            ]
        ),

        # Bishop attacking diag
        # - - -
        # - * -
        # x - -
        (   # Offset
            (1, -1),  # 1 step down, 1 step left
            [   # Moves
                (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                           MoveOption.PROPEGATES])
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
                (-1, 0),  # 1 step up, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Rook attacking x-axis right
            # - - -
            # - * x
            # - - -
            (   # Offset
                (0, 1),  # same row, 1 step right
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Rook attacking y-axis down
            # - - -
            # - * -
            # - x -
            (   # Offset
                (1, 0),  # 1 step down, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Rook attacking x-axis left
            # - - -
            # x * -
            # - - -
            (   # Offset
                (0, -1),  # same row, 1 step left
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
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
                (-1, -1),  # 1 step up, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),
            # Queen attacking y-axis up
            # - x -
            # - * -
            # - - -
            (   # Offset
                (-1, 0),  # 1 step up, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking diag
            # - - x
            # - * -
            # - - -
            (   # Offset
                (-1, 1),  # 1 step up, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking x-axis
            # - - -
            # - * x
            # - - -
            (   # Offset
                (0, 1),  # same row, 1 step right
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking diag
            # - - -
            # - * -
            # - - x
            (   # Offset
                (1, 1),  # 1 step down, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking y-axis
            # - - -
            # - * -
            # - x -
            (   # Offset
                (1, 0),  # 1 step down, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Bishop attacking diag
            # - - -
            # - * -
            # x - -
            (   # Offset
                (1, -1),  # 1 step down, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
                ]
            ),

            # Queen attacking x-axis
            # - - -
            # x * -
            # - - -
            (   # Offset
                (0, -1),  # same row, 1 step left
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROPEGATES])
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
                (-1, -1),  # 1 step up, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),
            # KING attacking y-axis up
            # - - x - -
            # - - * - -
            # - - - - -
            (   # Offset
                (-1, 0),  # 1 step up, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),

            # KING attacking diag
            # - - - x -
            # - - * - -
            # - - - - -
            (   # Offset
                (-1, 1),  # 1 step up, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # - - * x -
            # - - - - -
            (   # Offset
                (0, 1),  # same row, 1 step right
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),

            # KING attacking diag
            # - - - - -
            # - - * - -
            # - - - x -
            (   # Offset
                (1, 1),  # 1 step down, 1 step right
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),

            # KING attacking y-axis
            # - - - - -
            # - - * - -
            # - - x - -
            (   # Offset
                (1, 0),  # 1 step down, same col
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),

            # KING attacking diag
            # - - - - -
            # - - * - -
            # - x - - -
            (   # Offset
                (1, -1),  # 1 step down, 1 step left
                [   # Moves
                    (MoveType.COLLISION_DIAG, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # - x * - -
            # - - - - -
            (   # Offset
                (0, -1),  # same row, 1 step left
                [   # Moves
                    (MoveType.COLLISION_AXIS, [MoveOption.CAN_TAKE,
                                               MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # s - * - -
            # - - - - -
            (   # Offset
                (0, -2),  # same row, 2 steps left
                [   # Moves
                    (MoveType.KING_CASTLE, [MoveOption.PROTECTED])
                ]
            ),

            # KING attacking x-axis
            # - - - - -
            # - - * - s
            # - - - - -
            (   # Offset
                (0, 2),  # same row, 2 steps right
                [   # Moves
                    (MoveType.KING_CASTLE, [MoveOption.PROTECTED])
                ]
            )
            ]

    def __str__(self):
        """Overriden to String method

        Returns Enum name such as KING instead of object refrense"""
        return f'{self.name}'

    def __repr__(self) -> str:
        return self.__str__()
