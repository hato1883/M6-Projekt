from ui_interface import *
from text_formater import *




class TextUserInterface(UI_Interface):
      
    @classmethod    
    def show_splash_screen(cls, char, width, game_name, authors, build_date, greeting):
        """ Display game name, authors, date/build in box of specified width """
        TextFormater.print_divider( char, width)
        TextFormater.print_box_row_with_content(char, width, game_name)
        TextFormater.print_box_row_with_content(char, width, authors)
        TextFormater.print_box_row_with_content(char, width, build_date)
        TextFormater.print_divider(char, width)
        print(f"{greeting}")

    # Present user with successive choices of:
        # 1 or 2 player game, 2 players == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # return ( 2 player True/False , time limit integer, narration True/False)
    @classmethod
    def input_game_setup_parameters(cls, min_time_limit = 30):
        while True:
            players = 0
            move_time_limit = 0
            ai_narration = False

            while not players in (1, 2):
    
                players = input("Players(1/2): ")

                if players.isnumeric():
                    players = int(players)

            two_players = bool(players - 1)

            while  min_time_limit > move_time_limit:
    
                input_time = input("Time limit per move (s): ")

                if input_time.isnumeric():
                    move_time_limit = int(input_time)
            
            answer = None
            while not answer in ("y","yes","n","no"):
    
                answer = input("AI Narration(y/n): ").lower()
            
            if answer[0] == "y":
                ai_narration = True

            current_settings = f"| Players: {players} | Time/move: {move_time_limit} s | AI Narration: { 'On' if ai_narration == True else 'Off' } |"

            TextFormater.print_divider("-", len(current_settings))
            print(current_settings)
            TextFormater.print_divider("-", len(current_settings))

            answer = None
            while not answer in ("y","yes","n","no"):
    
                answer = input("Proceed(y/n): ").lower()
            
            if answer[0] == "y":
                break
        
        return (two_players, move_time_limit, ai_narration)

    # Display the current layout of chess board text-based represenation
    @classmethod
    def show_chess_board(cls, chess_board:list, debug:bool = False):
        if debug:
            column_names = TextFormater.create_column_number_tuple(len(chess_board))
            TextFormater.print_column_letters(column_names)
            for i in range(len(chess_board)):
                TextFormater.print_chess_board_row(i, chess_board[i])
        else:
            column_names = TextFormater.create_column_letter_tuple(len(chess_board))
            TextFormater.print_column_letters(column_names)
            for i in range(len(chess_board)):
                TextFormater.print_chess_board_row(len(chess_board)-i, chess_board[i])
        
        

        
    # Move tuple form is (row, column) were each element is integer [0,7]
    # Recount previous move to user by text 
    @classmethod
    def recount_user_move(self, move):
        (coordinates_origin, coordinates_dest) = move
        algebraic_origin = TextFormater.coordinates_to_algebra(coordinates_origin)
        algebraic_dest = TextFormater.coordinates_to_algebra(coordinates_dest)

        print(f"Moved {algebraic_origin} to {algebraic_dest}")

    # Used to input the user's move either through algebraic notation
    # return 2-tuple,(row, column) were each element is integer in [0,7]
    @classmethod
    def input_user_move(self, prompt_one = "From", prompt_two ="To"):

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
    
        
     # Prompt's user to select promotion for pawn in question
        # Multiple choice: queen, rook, bishop or knight
        # by text (q, r, b or k)
    @classmethod
    def input_promotion(self):
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





if __name__ == "__main__":
    bp = [1] * 8
    bp[0]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.ROOK)
    bp[1]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KNIGHT)
    bp[2]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.BISHOP)
    bp[3]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.QUEEN)
    bp[4]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KING)
    bp[5]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.BISHOP)
    bp[6]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KNIGHT)
    bp[7]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.ROOK)

    wp = [1] * 8
    wp[0]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.ROOK)
    wp[1]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KNIGHT)
    wp[2]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.BISHOP)
    wp[3]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KING)
    wp[4]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.QUEEN)
    wp[5]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.BISHOP)
    wp[6]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KNIGHT)
    wp[7]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.ROOK)
    

    empty_board = [[None] * 8 for _ in range(8)]
    
    for i in range(8):
        temp= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.PAWN)
        empty_board[1][i] = temp

    for i in range(8):
        empty_board[0][i] = bp[i]

    for i in range(8):
        temp= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.PAWN)
        empty_board[6][i] = temp


    for i in range(8):
        empty_board[7][i] = wp[i]

    def move_piece(chess_board, move):
        (origin, dest) = move
        (row_origin, column_origin) = origin
        print(origin) 
        (row_dest, column_dest) = dest
        print(dest)
        
        chess_board[row_dest][column_dest] = chess_board[row_origin][column_origin]
        chess_board[row_origin][column_origin] = None
    #Demo
    tui = TextUserInterface()
    """tui.show_splash_screen("@", 40, "Sagoschak", "DVA-J", "2023-10-17", "Welcome to Sagoschack!")
    parameters = tui.input_game_setup_parameters()
    print(parameters) """
        
    while True:
        tui.show_chess_board(empty_board)
        move = tui.input_user_move()
        move_piece(empty_board, move)
        tui.recount_user_move(move)
        promotion = tui.input_promotion()
        print(promotion) 

        



    
        



