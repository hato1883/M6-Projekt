from position_class import Position
from move_type_enum import MoveType
from move_option_enum import MoveOption


class Move:

    def __init__(self,
                 capture: Position,
                 type: MoveType,
                 conditions: list[MoveOption] = []):
        self._capture = capture
        self._type = type
        self._conditions = conditions

    @property
    def capture(self) -> Position:
        return self._capture

    @capture.setter
    def capture(self, capture):
        if self._capture in None:
            self._capture = capture

    @property
    def type(self) -> MoveType:
        return self._type

    @type.setter
    def type(self, type):
        if self._type in None:
            self._type = type

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
        text = f"{text} {self.capture}"  # noqa E501
        text = f"{text} using a"
        text = f"{text} {str(self.type)} move"
        text = f"{text} with the conditions: ["
        for condition in self.conditions:
            text = f"{text}{condition}, "
        text = f"{text[0:-2]}]"

        return text

    def __repr__(self) -> str:
        text = f"<Move:{self.capture}"
        text = f"{text} {self.type}"
        text = f"{text}, {self.conditions}>"
        return text

    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, self.__class__):
            return self.__dict__ == __value.__dict__
        else:
            return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
