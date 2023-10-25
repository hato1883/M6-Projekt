class Position:

    def __init__(self, row: int, col: int):
        self._row = row
        self._col = col

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, row):
        self._row = row

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, col):
        self._col = col

    def __str__(self) -> str:
        """String representation in format (row, col)"""
        return f"({self.row}, {self.col})"

    def __repr__(self) -> str:
        """String that is displayed when printing object
        such as the key in dict"""
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        """is value in object equal to each other

        Overloads == operator"""
        if isinstance(__value, self.__class__):
            return self.__dict__ == __value.__dict__
        else:
            return False

    def __ne__(self, __value: object) -> bool:
        """is value in object not equal to each other
        Overloads != opperator"""
        return not self.__eq__(__value)

    def __hash__(self) -> int:
        """Hashes contents of object

        a object with row and col equal to another position obj
        will have the same hash which is what we want"""
        return hash((self.row, self.col))
