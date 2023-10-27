#### TODO More shit, draw the actual chesspieces[import the stolen assets], find
#### out how to make the program relate the chessboard to the graphics
import pygame
import sys
from chessboard import *
from ui_interface import UI_Interface
import os
import chessboard as cb





class Window_Class(UI_Interface):
    
    script_directory = os.path.dirname(__file__)
    parent_directory = os.path.dirname(script_directory)
    # image_path = os.path.join(parent_directory, "assets", "your_image.png")
    
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    WIDTH, HEIGHT = 600,600

    SQUARE_SIZE = WIDTH // 8  # Divide the width into 8 squares
    def __init__(self, size=(800, 600)) -> None:
        
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Sago-Schack')
        self.running = True
        self.show_splash_screen
        self.font = pygame.font.Font(None, 36)
        self.board = Chessboard()
        self.board.create_default_board()


    def run(self):
        self.running=True

        #show splashscreen
        self.show_splash_screen()
        bb = pygame.image.load("assets/bb.png")  # Replace with the path to your sprite image
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #paint the background
            self.screen.fill(((43, 42, 51)))

            #call the show_chessboard function and draw the chessboard
            self.show_chess_board()
            pygame.display.flip()

        pygame.quit()
        sys.exit()


    def show_splash_screen(self):
        # Display game name, authors, date/build

        # Display text in the middle of the screen
        text = self.font.render("Sago-Shack, by: Hampus, John & Simon", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (self.size[0] // 2, self.size[1] // 2)
        self.screen.blit(text, text_rect)

        #Draw the text
        pygame.display.flip()
        
        #Wait 2000 ms
        pygame.time.delay(2000)





        pass

    def input_game_setup_parameters():
        # Present user with successive choices of:
        # 1 or 2 player game (if 1, 2nd player is computer) 1 player == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # return ( two_player True/False , sec time limit integer, narration True/False)
        pass
    
    def piece_type_to_sprite_name(self, chess_piece):
        prefix = "w"
        if chess_piece.get_color() is Color.BLACK:
            suffix = "b"
            
        match chess_piece.get_type():
            case PieceType.KING: 
                image_name = prefix + "k"
            case PieceType.QUEEN:
                image_name = prefix + "q"
            case PieceType.ROOK:
                image_name = prefix + "r"
            case PieceType.BISHOP:
                image_name = prefix + "b"
            case PieceType.KNIGHT:
                image_name = prefix + "n"
            case PieceType.PAWN:
                 image_name = prefix + "p"
            
        return image_name

    def show_chess_board(self, chessboard:list):
        row_index = 0
        for row in Chessboard:
            self.paint_chess_board_row(row_index, row)
            row_index += 1
            

    def paint_chess_board_row(self, row, row_list):
        x = self.SQUARE_SIZE
        y= self.SQUARE_SIZE * row

        if row % 2 == 0:
            even_square =  self.WHITE
            odd_square =  self.BLACK
        else:
            even_square = self.BLACK
            odd_square =  self.WHITE

        i = 0
        for square in row_list:
            if square is not None:
                image_name = self.piece_type_to_sprite_name(square)
                pygame.draw.rect(self.screen, image_name, (x*i, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                
            elif i % 2 == 0:
                pygame.draw.rect(self.screen, even_square, (x*i, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
            else:
                pygame.draw.rect(self.screen, odd_square, (x*i, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
            i += 1


        
        

    def recount_user_move():
        # Input two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]
        # Recount previous move to user by text or possibly graphically
        pass

    def input_user_move():
        # Used to input the user's move either through algebraic notation or graphical interacivity
        # returns two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]
        pass

    def input_promotion():
        # Prompt's user to select promotion for pawn in question
        # Multiple choice: queen, rook, bishop or knight
        # Either by text (q, r, b or k) or graphical interaction
        # return  integer in [0,3]. 0 == queen, 1 == r and so on.
        pass

    def draw_sprite(self, sprite, x, y):
        self.screen.blit(sprite, (x, y))


   
if __name__ == "__main__":
    game=Window_Class()
    game.run()