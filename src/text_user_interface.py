from ui_interface import UI_Interface
from text_formater import TextFormater
from piece_type_enum import PieceType


class TextUserInterface(UI_Interface):

    @classmethod
    def show_splash_screen(cls, char, width,
                           game_name, authors,
                           build_date, greeting):
        """Display game name, authors, date/build in box of specified width"""
        TextFormater.print_divider(char, width)
        TextFormater.print_box_row_with_content(char, width, game_name)
        TextFormater.print_box_row_with_content(char, width, authors)
        TextFormater.print_box_row_with_content(char, width, build_date)
        TextFormater.print_divider(char, width)
        print(f"{greeting}")

    # Present user with successive choices of:
        # 1 or 2 player game, 2 players == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # returns
        # tuple ( 2 player T/F , time limit int, narration T/F)
    @classmethod
    def input_game_setup_parameters(cls, min_time_limit: int = 30):
        while True:
            """ players = 0
            move_time_limit = 0 """
            ai_narration = False

            """ while not players in (1, 2):

                players = input("Players(1/2): ")

                if players.isnumeric():
                    players = int(players)

            two_players = bool(players - 1)

            while  min_time_limit > move_time_limit:

                input_time = input("Time limit per move (s): ")

                if input_time.isnumeric():
                    move_time_limit = int(input_time) """

            answer = None
            while answer not in ("y", "yes",
                                 "n", "no"):
                answer = input("AI Narration(y/n): ").lower()

            if answer[0] == "y":
                ai_narration = True

            current_setting = f"|AI Narration: { 'On' if ai_narration == True else 'Off' }|"  # noqa E501

            TextFormater.print_divider("-", len(current_setting))
            print(current_setting)
            TextFormater.print_divider("-", len(current_setting))

            """ current_settings = f"| Players: {players} | Time/move: {move_time_limit} s | AI Narration: { 'On' if ai_narration == True else 'Off' } |" """  # noqa E501

            answer = None
            while answer not in ("y", "yes",
                                 "n", "no"):
                answer = input("Proceed(y/n): ").lower()

            if answer[0] == "y":
                break

        return (ai_narration)

    # Display the current layout of chess board text-based represenation
    @classmethod
    def show_chess_board(cls, chess_board: list,
                         ai_narration: str,
                         debug: bool = False):

        if ai_narration != '':
            row_lines = TextFormater.split_string_into_rows(ai_narration)
        else:
            row_lines = []

        while len(row_lines) != len(chess_board):
            row_lines.append('')

        if debug:
            column_names = TextFormater.create_column_number_tuple(len(chess_board))  # noqa E501
            TextFormater.print_column_letters(column_names)
            for i in range(len(chess_board)):
                TextFormater.print_chess_board_row(i, chess_board[i], row_lines[i])  # noqa E501
        else:
            column_names = TextFormater.create_column_letter_tuple(len(chess_board))  # noqa E501
            TextFormater.print_column_letters(column_names)
            for i in range(len(chess_board)):
                TextFormater.print_chess_board_row(len(chess_board)-i, chess_board[i], row_lines[i])  # noqa E501

    # Move tuple form is (row, column) were each element is integer [0,7]
    # Recount previous move to user by text
    @classmethod
    def recount_user_move(self, move):
        (coordinates_origin, coordinates_dest) = move
        algebraic_origin = TextFormater.coordinates_to_algebra(coordinates_origin)  # noqa E501
        algebraic_dest = TextFormater.coordinates_to_algebra(coordinates_dest)

        print(f"Moved {algebraic_origin} to {algebraic_dest}")

    # Used to input the user's move either through algebraic notation
    # return 2-tuple,(row, column) were each element is integer in [0,7]
    @classmethod
    def input_user_move(self, prompt_one: str = "From",
                        prompt_two: str = "To") -> tuple[int, int]:

        while True:
            algebraic_origin = input(f"{prompt_one}: ").lower()
            if len(algebraic_origin) == 2:
                if algebraic_origin[0].isalpha() and algebraic_origin[1].isnumeric():  # noqa E501
                    origin = TextFormater.algebra_to_coordinates(algebraic = algebraic_origin)  # noqa E501
                    break

        while True:
            algebraic_dest = input(f"{prompt_two}: ").lower()
            if len(algebraic_dest) == 2:
                if algebraic_dest[0].isalpha() and algebraic_dest[1].isnumeric():  # noqa E501
                    dest = TextFormater.algebra_to_coordinates(algebraic = algebraic_dest)  # noqa E501
                    break

        return (origin, dest)

    @classmethod
    def input_promotion(self):
        """Prompt's user to select promotion for pawn in question
        Multiple choice: queen, rook, bishop or knight
        by text (q, r, b or k)"""
        choice = None
        while choice not in ["q", "r", "b", "k",
                             "queen", "rook", "bishop", "knight"]:
            choice = input('Choose promotion for pawn(q/r/b/k): ').lower()

        match choice[0]:
            case "q":
                return PieceType.QUEEN
            case "r":
                return PieceType.ROOK
            case "b":
                return PieceType.BISHOP
            case "k":
                return PieceType.KNIGHT
