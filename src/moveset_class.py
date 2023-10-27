from move_class import Move


class Moveset:

    def __init__(self,
                 dest_offset: tuple[int, int],
                 moves: list[Move] = []):
        self._dest_offset = dest_offset
        self._moves = moves

    @property
    def dest_offset(self) -> tuple[int, int]:
        return self._dest_offset

    @dest_offset.setter
    def dest_offset(self, dest_offset):
        if self._dest_offset in None:
            self._dest_offset = dest_offset

    @property
    def moves(self) -> list[Move]:
        return self._moves

    @moves.setter
    def moves(self, moves):
        if self._moves in None:
            self._moves = moves

    def __str__(self):
        # prints that this move is attacking [a-h][1-8]
        text = f"{self.dest_offset}"  # noqa E501
        text = f"{text} ["
        for move in self.moves:
            text = f"{text}{str(move)}, "
        text = f"{text[0:-2]}]"

        return text

    def __repr__(self) -> str:
        text = f"<Move:{self.dest_offset}"
        text = f"{text} {self.moves}>"
        return text

    def __eq__(self, __value: object) -> bool:

        if isinstance(__value, self.__class__):
            return self.__dict__ == __value.__dict__
        else:
            return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
