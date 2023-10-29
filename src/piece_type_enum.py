from enum import Enum
from move_type_enum import MoveType
from move_option_enum import MoveOption
from move_class import Move
from moveset_class import Moveset
from position_class import Position


class PieceType(Enum):
    ####
    # Pawn Move List
    ####
    PAWN = [
        # Pawn walking up
        # - o -
        # - - -
        # - * -
        Moveset(
            Position(-2, 0),  # Move destination
            [
                Move(
                    Position(-2, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,  # straight move
                    [MoveOption.FIRST]  # Move option
                    )
            ]
        ),

        # Pawn attacking left
        # - - -
        # x - -
        # - * -
        Moveset(
            Position(-1, -1),  # 1 step up, 1 step left
            [
                Move(
                    Position(-1, -1),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.MUST_TAKE]),
                Move(
                    Position(0, -1),  # Attacked destination
                    MoveType.PAWN_EN_PASSANT,
                    [])
            ]
        ),

        # Pawn walking up
        # - - -
        # - o -
        # - * -
        Moveset(
            Position(-1, 0),  # 1 step up, same col
            [
                Move(
                    Position(-1, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [])
            ]
        ),

        # Pawn attacking right
        # - - -
        # - - x
        # - * -
        Moveset(
            Position(-1, 1),  # 1 step up, same col
            [
                Move(
                    Position(-1, 1),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.MUST_TAKE]),
                Move(
                    Position(0, 1),  # Attacked destination
                    MoveType.PAWN_EN_PASSANT,
                    [])
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
        Moveset(
            Position(-2, -1),  # 2 steps up, 1 step left
            [
                Move(
                    Position(-2, -1),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
            ]
        ),

        Moveset(
            Position(-2, 1),  # 2 step up, 1 step right
            [
                Move(
                    Position(-2, 1),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
            ]
        ),

        # Knight T facing right
        # - - - - -
        # - - - - x
        # - - * - -
        # - - - - x
        # - - - - -
        Moveset(
            Position(-1, 2),  # 1 step up, 2 steps right
            [
                Move(
                    Position(-1, 2),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
            ]
        ),

        # Diag take + en passant
        Moveset(
            Position(1, 2),  # 1 step down, 2 steps right
            [
                Move(
                    Position(1, 2),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
            ]
        ),

        # Knight T facing down
        # - - - - -
        # - - - - -
        # - - * - -
        # - - - - -
        # - x - x -
        Moveset(
            Position(2, -1),  # 2 steps down, same left
            [
                Move(
                    Position(2, -1),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
            ]
        ),

        Moveset(
            Position(2, 1),  # 2 steps down, 1 step right
            [
                Move(
                    Position(2, 1),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
            ]
        ),

        # Knight T facing left
        # - - - - -
        # x - - - -
        # - - * - -
        # x - - - -
        # - - - - -
        Moveset(
            Position(-1, -2),  # 1 step up, 2 steps left
            [
                Move(
                    Position(-1, -2),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
            ]
        ),

        # Diag take + en passant
        Moveset(
            Position(1, -2),  # 1 step down, 2 steps left
            [
                Move(
                    Position(1, -2),  # Attacked destination
                    MoveType.ABSOLUTE,
                    [MoveOption.CAN_TAKE])
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
        Moveset(
            Position(-1, -1),  # 1 step up, 1 step left
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Bishop attacking diag
        # - - x
        # - * -
        # - - -
        Moveset(
            Position(-1, 1),  # 1 step up, 1 step right
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Bishop attacking diag
        # - - -
        # - * -
        # - - x
        Moveset(
            Position(1, 1),  # 1 step down, 1 step right
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Bishop attacking diag
        # - - -
        # - * -
        # x - -
        Moveset(
            Position(1, -1),  # 1 step down, 1 step left
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
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
        Moveset(
            Position(-1, 0),  # 1 step up, same col
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Rook attacking x-axis right
        # - - -
        # - * x
        # - - -
        Moveset(
            Position(0, 1),  # same row, 1 step right
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Rook attacking y-axis down
        # - - -
        # - * -
        # - x -
        Moveset(
            Position(1, 0),  # 1 step down, same col
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Rook attacking x-axis left
        # - - -
        # x * -
        # - - -
        Moveset(
            Position(0, -1),  # same row, 1 step left
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
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
        Moveset(
            Position(-1, -1),  # 1 step up, 1 step left
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),
        # Queen attacking y-axis up
        # - x -
        # - * -
        # - - -
        Moveset(
            Position(-1, 0),  # 1 step up, same col
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Queen attacking diag
        # - - x
        # - * -
        # - - -
        Moveset(
            Position(-1, 1),  # 1 step up, 1 step right
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Queen attacking x-axis
        # - - -
        # - * x
        # - - -
        Moveset(
            Position(0, 1),  # same row, 1 step right
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Queen attacking diag
        # - - -
        # - * -
        # - - x
        Moveset(
            Position(1, 1),  # 1 step down, 1 step right
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Queen attacking y-axis
        # - - -
        # - * -
        # - x -
        Moveset(
            Position(1, 0),  # 1 step down, same col
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Bishop attacking diag
        # - - -
        # - * -
        # x - -
        Moveset(
            Position(1, -1),  # 1 step down, 1 step left
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
            ]
        ),

        # Queen attacking x-axis
        # - - -
        # x * -
        # - - -
        Moveset(
            Position(0, -1),  # same row, 1 step left
            [
                Move(
                    Position(0, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROPEGATES])
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
        Moveset(
            Position(-1, -1),  # 1 step up, 1 step left
            [
                Move(
                    Position(-1, -1),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),
        # KING attacking y-axis up
        # - - x - -
        # - - * - -
        # - - - - -
        Moveset(
            Position(-1, 0),  # 1 step up, same col
            [
                Move(
                    Position(-1, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),

        # KING attacking diag
        # - - - x -
        # - - * - -
        # - - - - -
        Moveset(
            Position(-1, 1),  # 1 step up, 1 step right
            [
                Move(
                    Position(-1, 1),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),

        # KING attacking x-axis
        # - - - - -
        # - - * x -
        # - - - - -
        Moveset(
            Position(0, 1),  # same row, 1 step right
            [
                Move(
                    Position(0, 1),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),

        # KING attacking diag
        # - - - - -
        # - - * - -
        # - - - x -
        Moveset(
            Position(1, 1),  # 1 step down, 1 step right
            [
                Move(
                    Position(1, 1),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),

        # KING attacking y-axis
        # - - - - -
        # - - * - -
        # - - x - -
        Moveset(
            Position(1, 0),  # 1 step down, same col
            [
                Move(
                    Position(1, 0),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),

        # KING attacking diag
        # - - - - -
        # - - * - -
        # - x - - -
        Moveset(
            Position(1, -1),  # 1 step down, 1 step left
            [
                Move(
                    Position(1, -1),  # Attacked destination
                    MoveType.COLLISION_DIAG,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),

        # KING attacking x-axis
        # - - - - -
        # - x * - -
        # - - - - -
        Moveset(
            Position(0, -1),  # same row, 1 step left
            [
                Move(
                    Position(0, -1),  # Attacked destination
                    MoveType.COLLISION_AXIS,
                    [MoveOption.CAN_TAKE, MoveOption.PROTECTED])
            ]
        ),

        # KING attacking x-axis
        # - - - - -
        # s - * - -
        # - - - - -
        Moveset(
            Position(0, -2),  # same row, 2 steps left
            [
                Move(
                    Position(0, -2),  # Attacked destination
                    MoveType.KING_CASTLE,
                    [MoveOption.PROTECTED])
            ]
        ),

        # KING attacking x-axis
        # - - - - -
        # - - * - s
        # - - - - -
        Moveset(
            Position(0, 2),  # same row, 2 steps right
            [
                Move(
                    Position(0, 2),  # Attacked destination
                    MoveType.KING_CASTLE,
                    [MoveOption.PROTECTED])
            ]
        )
    ]

    ####
    # King Move List
    ####
    EMPTY = [
    ]

    def __str__(self):
        """Overriden to String method

        Returns Enum name such as KING instead of object refrense"""
        return f'{self.name}'

    def __repr__(self) -> str:
        return self.__str__()
