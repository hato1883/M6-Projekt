from chess_piece_class import EMPTY_PIECE
from position_class import Position
from piece_type_enum import PieceType
from piece_color_enum import Color


class TextFormater:
    # Print line of specified char with specified length
    @classmethod
    def print_divider(cls, char, length):
        print(f"{char*length}")

    # Print line of specified length with content centered,
    # beginning and ending with specified char
    @classmethod
    def print_box_row_with_content(cls, char, length, content):
        left_margin = (length*len(char) - len(content)) // 2 - len(char)
        right_margin = left_margin

        if len(content) % 2 == 1:
            right_margin += 1

        print(f"{char}{' '*left_margin}{content}", end='')
        print(f"{' '*right_margin}{char}")

    # returns unicode chess symbol based on supplied ChessPiece Enum
    @classmethod
    def piece_type_to_unicode_chess_symbol(cls, chess_piece):
        suffix = ("A", "B", "C", "D", "E", "F")
        if chess_piece.get_color() is Color.BLACK:
            suffix = ("4", "5", "6", "7", "8", "9")

        match chess_piece.get_type():
            case PieceType.KING:
                unicode_str = "\\u265" + suffix[0]
            case PieceType.QUEEN:
                unicode_str = "\\u265" + suffix[1]
            case PieceType.ROOK:
                unicode_str = "\\u265" + suffix[2]
            case PieceType.BISHOP:
                unicode_str = "\\u265" + suffix[3]
            case PieceType.KNIGHT:
                unicode_str = "\\u265" + suffix[4]
            case PieceType.PAWN:
                unicode_str = "\\u265" + suffix[5]

        return unicode_str.encode().decode('unicode_escape')

    # Print a numbered row of chess board with unicode symbols
    @classmethod
    def print_chess_board_row(cls, row, row_list, narration_line: str):
        if row % 2 == 0:
            even_square = "\u2610"  # unicode for white square
            odd_square = "\u2630"  # unicode for black square
        else:
            even_square = "\u2630"
            odd_square = "\u2610"

        print(f"{row})", end='')

        i = 0
        for square in row_list:
            if square is not EMPTY_PIECE:
                print(f" {cls.piece_type_to_unicode_chess_symbol(square)} ", end='')  # noqa E501
            else:
                print(f" { even_square if i % 2 == 0 else odd_square} ", end='')  # noqa E501
            i += 1
        print(f"   {narration_line}", end='')
        print()

    # Prints evenly spaced letters for column orientatin
    @classmethod
    def print_column_letters(cls, column_letters):
        print("  ", end='')
        for column in column_letters:
            print(f" {column} ", end='')
        print()

    # coverts algebraic chess notation to coordinates e.g string "a1" to (7,0)
    @classmethod
    def algebra_to_coordinates(cls, algebraic, number_of_rows: int = 8):

        colum = abs(ord(algebraic[0]) - 97)
        row = abs(number_of_rows-int(algebraic[1]))
        coordinates = Position(row, colum)

        return coordinates

    # coverts coordinates algebraic chess notation e.g  (7,0) to string "a1"
    @classmethod
    def coordinates_to_algebra(cls, coordinates, number_of_rows: int = 8):
        (row, column) = coordinates
        column = chr(column + 97)
        row = number_of_rows - row

        return f"{column}{row}"

    @classmethod
    def create_column_letter_tuple(cls, number_of_letters: int):
        column_letters = []
        for i in range(number_of_letters):
            column_letters.append(chr(65+i))
        return tuple(column_letters)

    @classmethod
    def create_column_number_tuple(cls, numbers: int):
        column_numbers = []
        for i in range(numbers):
            column_numbers.append(f"{i}")
        return tuple(column_numbers)

    @classmethod
    def split_string_into_rows(cls, str: str):
        split_str = str.split(' ')
        row_list = []

        end_words = ''
        if not len(split_str) % 4 == 0:
            end_words = end_words + f"{split_str[-1]} "
            split_str = split_str[:-1]

        if len(split_str) < 4:
            row_list = [end_words]
            return row_list

        words_per_line = len(split_str) // 4
        rows = len(split_str) // words_per_line

        for _ in range(rows):
            row_list.append('')

        for r in range(rows):
            for i in range(words_per_line):
                row_list[r] = row_list[r] + f"{split_str[i]} "
            split_str = split_str[words_per_line:]

        row_list.append(end_words)

        return row_list
