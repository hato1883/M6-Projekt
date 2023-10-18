from abc import ABC, abstractmethod

class UI_Interface(ABC):

    @abstractmethod
    def show_splash_screen(self):
        # Display game name, authors, date/build
        pass

    @abstractmethod
    def game_setup_menu(self):
        # Present user with succesiv choices of:
        # 1 or 2 player game (if 1, 2nd player is computer) 1 player == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # return ( 1 player True/False , sec time limit integer, narration True/False)
        pass

    @abstractmethod
    def show_chess_board(self, ChessBoard):
        # Display the current layout of chess board either text-based or graphics-based represenation
        pass

    @abstractmethod
    def recount_user_move(self, origin, dest):
        # Input two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]
        # Recount previos move to user by text or possibly graphically
        pass

    @abstractmethod
    def input_user_move(self):
        # Used to input the user's move either through algebraic notation or graphical interacivity
        # returns two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]
        pass

    @abstractmethod
    def user_choose_promotion(self):
        # Prompt's user to select promotion for pawn in question
        # Multiple choice: queen, rook, bishop or knight
        # Either by text (q, r, b or k) or graphical interaction
        pass


    

    
        
        