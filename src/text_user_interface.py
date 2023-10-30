from chess_piece_class import ChessPiece
from piece_color_enum import Color
from piece_type_enum import PieceType
from position_class import Position
from status_enum import Status
from ui_interface import UI_Interface
from text_formater import TextFormater
from narration_interface import NarrationInterface
from chessboard import Chessboard


class TextUserInterface(UI_Interface):

    def __init__(self, chessboard: Chessboard, narration: NarrationInterface) -> None:
        super().__init__()
        self.chessboard = chessboard
        self.narration = narration

    def show_splash_screen(self, char: chr, width: int, game_name: str, authors: str, build_date: str, greeting):
        """ Display game name, authors, date/build in box of specified width. Box border of spcified char"""
        TextFormater.print_divider( char, width)
        TextFormater.print_box_row_with_content(char, width, game_name)
        TextFormater.print_box_row_with_content(char, width, authors)
        TextFormater.print_box_row_with_content(char, width, build_date)
        TextFormater.print_divider(char, width)
        print(f"{greeting}")

    def run(self):

        # show titel screen
        self.show_splash_screen("@", 40, "Sagoschak", "DVA-J",
                                "2023-10-17", "Welcome to Sagoschack!")
        has_ended = False

        ai_naration_text = ""
        while not has_ended:
            # TODO: check if king is being attacked.
            # TODO: If king is attacked, can the king move,
            # Or can something block attacker.
            for color_turn in list(Color)[:2]:

                # Show user the chess board
                self.show_chess_board(self.chessboard.get_chessboard(), ai_naration_text)

                # Loop until valid move
                while True:  # Wait for valid move
                    # get origin and destination of the move
                    (origin, dest) = self.input_user_move()

                    # Check if origin contains piece
                    # of color equal to current player
                    if self.chessboard.get_piece(origin).get_color() != color_turn:
                        # Can't move enemy piece on your turn

                        # TODO: TextUserInterface needs
                        # to display that move is invalid
                        continue

                    # Move chess piece
                    (succeeded, status, pieces) = self.chessboard.move(origin, dest)
                    # Check if it worked
                    if not succeeded:
                        # Moved failed valid check

                        # TODO: TextUserInterface needs
                        # to display that move is invalid
                        continue

                    ai_naration_text = self.narration.generate_move_text(origin,
                                                                         dest,
                                                                         pieces[0],
                                                                         pieces[1])

                    # Did a Pawn promote?
                    if status is Status.PAWN_PROMOTION:
                        # Remove pawn
                        self.chessboard.remove_piece(origin)

                        # Remove piece on destination
                        self.chessboard.remove_piece(dest)

                        # Add chosen promoted piece
                        self.chessboard.add_piece(ChessPiece(color_turn,
                                                             self.input_promotion()),
                                                  dest)

                    # End this players turn.
                    break

            # Next color
            continue
        # Game has ended


    def show_chess_board(self, chessboard: list, ai_narration: str, debug: bool = False):

        if ai_narration != '':
            row_lines = TextFormater.split_string_into_rows(ai_narration)
        else:
            row_lines = []
            
        while len(row_lines) != len(chessboard):
            row_lines.append('')

        if debug:
            column_names = TextFormater.create_column_number_tuple(len(chessboard))
            TextFormater.print_column_letters(column_names)
            for i in range(len(chessboard)):
                TextFormater.print_chess_board_row(i, chessboard[i], row_lines[i])
        else:
            column_names = TextFormater.create_column_letter_tuple(len(chessboard))
            TextFormater.print_column_letters(column_names)
            for i in range(len(chessboard)):
                TextFormater.print_chess_board_row(len(chessboard)-i, chessboard[i], row_lines[i])

    def recount_user_move(self, move:tuple[Position, Position]):
        """ Returns string recounting user move  """
        (coordinates_origin, coordinates_dest) = move
        algebraic_origin = TextFormater.coordinates_to_algebra(coordinates_origin)
        algebraic_dest = TextFormater.coordinates_to_algebra(coordinates_dest)

        print(f"Moved {algebraic_origin} to {algebraic_dest}")

    def input_user_move(self, prompt_one:str = "From", prompt_two:str ="To"):
        """ Prompts user to enter a chess move in algebraic chess notation. Returns tuple of Postion objects, origin and destination"""

        while True:
            algebraic_origin = input(f"{prompt_one}: ").lower()
            try:
                if algebraic_origin[0].isalpha() and algebraic_origin[1].isnumeric():
                    origin = TextFormater.algebra_to_coordinates(algebraic = algebraic_origin)
                    break
            except:
                continue

        while True:
            algebraic_dest = input(f"{prompt_two}: ").lower()
            try:
                if algebraic_dest[0].isalpha() and algebraic_dest[1].isnumeric():
                    dest = TextFormater.algebra_to_coordinates(algebraic= algebraic_dest)
                    break
            except:
                continue


        return (origin, dest)
    
    @classmethod
    def input_game_setup_parameters():
        # Present user with successive choices of:
        # 1 or 2 player game (if 1, 2nd player is computer) 1 player == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # return (narration True/False)
        pass
    
    @classmethod
    def input_promotion(self):
        """  Prompt's user to select promotion for pawn.
        Multiple choice: queen, rook, bishop or knight
        by text (q, r, b or k)  """
        choice = None
        while not choice in ("q","r","b","k","queen","rook","bishop","knight"):
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
 

        



    
        



