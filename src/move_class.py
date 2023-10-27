from move_type_enum import MoveType
from move_option_enum import MoveOption


class Move:

    def __init__(self,
                 capture_offset: tuple[int, int],
                 move_type: MoveType,
                 conditions: list[MoveOption] = []):
        self._capture_offset = capture_offset
        self._move_type = move_type
        self._conditions = conditions

    @property
    def capture_offset(self) -> tuple[int, int]:
        return self._capture_offset

    @capture_offset.setter
    def capture_offset(self, capture_offset):
        if self._capture_offset in None:
            self._capture_offset = capture_offset

    @property
    def move_type(self) -> MoveType:
        return self._move_type

    @move_type.setter
    def move_type(self, move_type):
        if self._move_type in None:
            self._move_type = move_type

    @property
    def conditions(self) -> list[MoveOption]:
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        if self._conditions in None:
            self._conditions = conditions

    def __str__(self):
        # prints that this move is attacking [a-h][1-8]
        text = "Attacks"
        text = f"{text} {self.capture_offset}"  # noqa E501
        text = f"{text} using a"
        text = f"{text} {str(self.move_type)} move"
        text = f"{text} with the conditions: ["
        for condition in self.conditions:
            text = f"{text}{condition}, "
        text = f"{text[0:-2]}]"

        return text

    def __repr__(self) -> str:
        text = f"<Move:{self.capture_offset}"
        text = f"{text} {self.move_type}"
        text = f"{text}, {self.conditions}>"
        return text

    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, self.__class__):
            return self.__dict__ == __value.__dict__
        else:
            return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
