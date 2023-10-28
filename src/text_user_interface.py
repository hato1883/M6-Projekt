from ui_interface import *
from text_formater import *


class TextUserInterface(UI_Interface):
      
    @classmethod    
    def show_splash_screen(cls, char:chr, width:int, game_name:str, authors:str, build_date:str, greeting):
        """ Display game name, authors, date/build in box of specified width. Box border of spcified char"""
        TextFormater.print_divider( char, width)
        TextFormater.print_box_row_with_content(char, width, game_name)
        TextFormater.print_box_row_with_content(char, width, authors)
        TextFormater.print_box_row_with_content(char, width, build_date)
        TextFormater.print_divider(char, width)
        print(f"{greeting}")


    @classmethod
    def input_game_setup_parameters(cls):
        """ Asks user to whether AI-narration should be On/Off, returns True for Yes"""
        ai_narration = False
    
        while True:
            
            answer = None
            while not answer in ("y","yes","n","no"):
    
                answer = input("AI Narration(y/n): ").lower()
            
            if answer[0] == "y":
                ai_narration = True

            current_setting = f"|AI Narration: { 'On' if ai_narration == True else 'Off' }|"

            TextFormater.print_divider("-", len(current_setting))
            print(current_setting)
            TextFormater.print_divider("-", len(current_setting))

            answer = None
            while not answer in ("y","yes","n","no"):
    
                answer = input("Proceed(y/n): ").lower()
            
            if answer[0] == "y":
                break
        
        return (ai_narration)

    # Display the current layout of chess board text-based represenation
    @classmethod
    def show_chess_board(cls, chess_board:list, ai_narration:str, debug:bool = False):

        if ai_narration != '':
            row_lines = TextFormater.split_string_into_rows(ai_narration)
        else:
            row_lines = []
            
        while len(row_lines) != len(chess_board):
            row_lines.append('')

        if debug:
            column_names = TextFormater.create_column_number_tuple(len(chess_board))
            TextFormater.print_column_letters(column_names)
            for i in range(len(chess_board)):
                TextFormater.print_chess_board_row(i, chess_board[i], row_lines[i])
        else:
            column_names = TextFormater.create_column_letter_tuple(len(chess_board))
            TextFormater.print_column_letters(column_names)
            for i in range(len(chess_board)):
                TextFormater.print_chess_board_row(len(chess_board)-i, chess_board[i], row_lines[i])
        
        

        

    @classmethod
    def recount_user_move(self, move:tuple[Position, Position]):
        """ Returns string recounting user move  """
        (coordinates_origin, coordinates_dest) = move
        algebraic_origin = TextFormater.coordinates_to_algebra(coordinates_origin)
        algebraic_dest = TextFormater.coordinates_to_algebra(coordinates_dest)

        print(f"Moved {algebraic_origin} to {algebraic_dest}")


    @classmethod
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
 

        



    
        



