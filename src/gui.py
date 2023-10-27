#### TODO More shit, draw the actual chesspieces[import the stolen assets], find
#### out how to make the program relate the chessboard to the graphics
import pygame
import sys
import os
from chessboard import *
from ui_interface import UI_Interface






class Window_Class(UI_Interface):
    
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
        # Get the directory of the current script
        self.script_directory = script_directory = os.path.dirname(__file__)

        # Get the parent directory (the directory containing the script)
        self.parent_directory = parent_directory = os.path.dirname(script_directory)

        #Get the asset directory (the directory containing assets in this project)

        self.asset_path = asset_path = os.path.join(parent_directory, "assets")

        #Image path to the black pawn 'bp.png'
        #image_path = os.path.join(parent_directory, "assets", "bp.png")

        # Print the parent directory
        print(f"The parent directory of the current script is: {parent_directory}")
        print(f'The asset directory is {asset_path}')


    def run(self):
        self.running=True

        #show splashscreen
        self.show_splash_screen()

        self.board = Chessboard()
        self.board.create_default_board()

        self.piece_image = [[],[]]

        colors =("b","w")
        suffix = ("k","q","r","b","n","p")
        i = 0
        for color in colors:
            for letter in suffix:
                temp = self.asset_load(f"{color}{letter}")
                self.piece_image[i].append( self.load_and_scale_sprite(temp) )
            i += 1


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #paint the background
            self.screen.fill(((43, 42, 51)))

            #call the show_chessboard function and draw the chessboard
            self.show_chess_board(self.board.get_chessboard())
            # print(type(self.board.get_chessboard()))
            self.draw_sprite(self.piece_image[0][1],150,150)
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

    def asset_load(self,target:str):
       
       target

       asset_filepath=os.path.join(self.asset_path,target)
       image_path = os.path.join(f'{asset_filepath}.png')


       return image_path

    def input_game_setup_parameters():
        # Present user with successive choices of:
        # 1 or 2 player game (if 1, 2nd player is computer) 1 player == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # return ( two_player True/False , sec time limit integer, narration True/False)
        pass

    def show_chess_board_2(self):
        for row in range(8):
            for col in range(8):
                x, y = col * self.SQUARE_SIZE, row * self.SQUARE_SIZE
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, self.WHITE, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.screen, self.BLACK, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
        pass
    
    def piece_type_to_sprite_name(self, chess_piece:PieceType):
        prefix = 1
        if chess_piece.get_color() is Color.BLACK:
            prefix = 0
            
        match chess_piece.get_type():
            case PieceType.KING: 
                image_name = self.piece_image[prefix][0]
            case PieceType.QUEEN:
                image_name = self.piece_image[prefix][1]
            case PieceType.ROOK:
                image_name = self.piece_image[prefix][2]
            case PieceType.BISHOP:
                image_name = self.piece_image[prefix][3]
            case PieceType.KNIGHT:
                image_name = self.piece_image[prefix][4]
            case PieceType.PAWN:
                image_name = self.piece_image[prefix][5]
            
        return image_name

    def show_chess_board(self, Chessboard:list):
        row_index = 0

        for row in Chessboard:
            self.paint_chess_board_row(row_index, row)
            row_index += 1
            

    def paint_chess_board_row(self, row_index, row_list):
        x_step = self.SQUARE_SIZE
        y = self.SQUARE_SIZE * row_index

        if row_index % 2 == 0:
            even_square =  self.WHITE
            odd_square =  self.BLACK
        else:
            even_square = self.BLACK
            odd_square =  self.WHITE

        i = 0
        for square in row_list:
            if square is not None:
                image_name = self.piece_type_to_sprite_name(square)
                self.draw_sprite(image_name, x_step*i, y,)
                
            elif i % 2 == 0:
                pygame.draw.rect(self.screen, even_square, (x_step*i, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
            else:
                pygame.draw.rect(self.screen, odd_square, (x_step*i, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
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

    def load_and_scale_sprite(self, sprite_path):
        # Load the sprite image
        sprite_image = pygame.image.load(sprite_path)

        # Get the original dimensions
        original_width, original_height = sprite_image.get_size()

        # Scale the sprite to one-quarter of its original size
        scaled_width = original_width // 2
        scaled_height = original_height // 2

        # Scale the sprite image
        scaled_sprite = pygame.transform.scale(sprite_image, (scaled_width, scaled_height))

        return scaled_sprite


   
if __name__ == "__main__":
    game=Window_Class()
    game.run()