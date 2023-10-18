from ui_interface import *
from chess_piece import *

class TextFormater:
    
    # Print line of specified char with specified length
    @classmethod
    def print_divider(cls, char, length): 
        print(f"{char*length}")

    # Print line of specified length with content centered, beginning and ending with specified char
    @classmethod
    def print_box_row_with_content(cls, char, length, content): 
        left_margin = (length*len(char) - len(content)) // 2 - len(char)
        right_margin = left_margin
        
        if len(content) % 2 == 1:
            right_margin += 1

        print(f"{char}{' '*left_margin}{content}", end ='')
        print(f"{' '*right_margin}{char}")

    @classmethod
    def piece_type_to_unicode_chess_symbol(cls, chess_piece):
        suffix = ("4","5","6","7","8","9")
        if chess_piece.get_color() == "BLACK":
            suffix = ("A", "B","C","D","E","F")
            
        match chess_piece.get_type():
            case "KING": 
                unicode_str = "\\u265" + suffix[0]
            case "QUEEN":
                unicode_str = "\\u265" + suffix[1]
            case "ROOK":
                unicode_str = "\\u265" + suffix[2]
            case "BISHOP":
                unicode_str = "\\u265" + suffix[3]
            case "KNIGHT":
                unicode_str = "\\u265" + suffix[4]
            case "PAWN":
                 unicode_str = "\\u265" + suffix[5]
            
        return unicode_str.encode().decode('unicode_escape')

    @classmethod
    def print_chess_board_row(cls, row, row_list):
        if row % 2 == 0:
            first_square = "\u2610"
            second_square = "\u2612"
        else:
            first_square = "\u2612"
            second_square = "\u2610"

        print(f"{row})",end='')

        i = 0
        for square in row_list:
            if square != None:
                print(f" {cls.piece_type_to_unicode_chess_symbol(square)} ", end='')
            else:
                print(f" { first_square if i % 2 == 0 else second_square} ", end='')
            i += 1
        print()


    @classmethod
    def print_column_letters(cls, column_letters):
        print("  ", end='')
        for column in column_letters:
            print(f" {column} ", end='')
        print()



class TextUserInterface(UI_Interface):

    # Display game name, authors, date/build in box of specified    
    @classmethod    
    def show_splash_screen(cls, char, length, game_name, authors, build_date, greeting):
        TextFormater.print_divider( char, length)
        TextFormater.print_box_row_with_content(char, length, game_name)
        TextFormater.print_box_row_with_content(char, length, authors)
        TextFormater.print_box_row_with_content(char, length, build_date)
        TextFormater.print_divider(char, length)
        print(f"{greeting}")
        pass

    @classmethod
    def input_game_setup_parameters(cls):

        while True:
            players = 0
            move_time_limit = 0
            ai_narration = False

            while not players in (1, 2):
    
                players = input("Players(1/2): ")

                if players.isnumeric():
                    players = int(players)

            two_players = bool(players - 1)

            while  0 >= move_time_limit:
    
                input_time = input("Time limit per move (s): ")

                if input_time.isnumeric():
                    move_time_limit = int(input_time)
            

            answer = input("AI Narration(y/n): ").lower()
            while not answer in ("y","yes","n","no"):
    
                answer = input("AI Narration(y/n): ").lower()
            
            if answer[0] == "y":
                ai_narration = True

            current_settings = f"| Players: {players} | Time/move: {move_time_limit} s | AI Narration: { 'On' if ai_narration == True else 'Off' } |"

            TextFormater.print_divider("-", len(current_settings))
            print(current_settings)
            TextFormater.print_divider("-", len(current_settings))

            

            answer = input("Proceed(y/n): ").lower()
            while not answer in ("y","yes","n","no"):
    
                answer = input("Proceed(y/n): ").lower()
            
            if answer[0] == "y":
                break

            print()


        # Present user with successive choices of:
        # 1 or 2 player game (if 1, 2nd player is computer) 2 players == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # return ( 2 player True/False , time limit integer, narration True/False)
        return (two_players, move_time_limit, ai_narration)

    
    def show_chess_board(self, chess_board):
        TextFormater.print_column_letters(("A","B","C","D","E","F","G","H"))
        for i in range(8):
            TextFormater.print_chess_board_row(i+1, chess_board[i])

        # Display the current layout of chess board either text-based or graphics-based represenation
        pass

    
    def recount_user_move(self, origin, dest):
        # Input two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]
        # Recount previous move to user by text or possibly graphically
        pass

    
    def input_user_move(self):
        # Used to input the user's move either through algebraic notation or graphical interacivity
        # returns two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]
        pass

   
    def input_promotion(self):
        # Prompt's user to select promotion for pawn in question
        # Multiple choice: queen, rook, bishop or knight
        # Either by text (q, r, b or k) or graphical interaction
        pass
    
    def print_move(self, origin, dest):
        print(f"{origin} to {dest}")

    def input_move(self, origin, dest):
        return super().input_move(origin, dest)


cp = [1] * 6
cp[0]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.PAWN)
cp[1]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.ROOK)
cp[2]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.BISHOP)
cp[3]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KNIGHT)
cp[4]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.QUEEN)
cp[5]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KING)

lp = [1] * 6
lp[0]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.PAWN)
lp[1]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.ROOK)
lp[2]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.BISHOP)
lp[3]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KNIGHT)
lp[4]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.QUEEN)
lp[5]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KING)

empty_board = [[None] * 8 for _ in range(8)]
for i in range(6):
    empty_board[0][i] = cp[i]


for i in range(6):
    empty_board[7][i] = lp[i]

print(empty_board)

tui = TextUserInterface()
# tui.show_splash_screen("@", 40, "Sagoschak", "DVA-J", "2023-10-17", "Welcome to Sagoschack!")
# parameters = tui.input_game_setup_parameters()
# print(parameters)
tui.show_chess_board(empty_board)



