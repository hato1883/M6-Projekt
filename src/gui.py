import pygame
import sys
import os
from chess_piece_class import EMPTY_PIECE
from narration_interface import NarrationInterface
from piece_type_enum import PieceType
from ui_interface import UI_Interface
from piece_color_enum import Color
from chessboard import Chessboard
from position_class import Position


class Window_Class(UI_Interface):

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)

    WIDTH, HEIGHT = 600, 600

    SQUARE_SIZE = WIDTH // 8  # Divide the width into 8 squares
    '''Defines the width of each square of the chessboard as WIDTH/8'''
    def __init__(self, chessboard: Chessboard, narration: NarrationInterface, size=(800, 600)) -> None:
        '''Initializes the screen as it's own object and sets the size of the screen to 800 x 600 by default if no other value is given'''

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

        # Get the asset directory (the directory containing assets in this project)

        self.asset_path = asset_path = os.path.join(parent_directory, "assets")

        # Image path to the black pawn 'bp.png'
        # image_path = os.path.join(parent_directory, "assets", "bp.png")

        # Print the parent directory
        print(f"The parent directory of the current script is: {parent_directory}")
        print(f'The asset directory is {asset_path}')
        self.narrator: NarrationInterface = narration
        self.board: Chessboard = chessboard

    def run(self):
        flip = True
        marked = False
        origin = Position
        destination = Position
        self.running = True

        self.game_has_ended = False

        # show splashscreen
        self.show_splash_screen()

        self.piece_image = [[], []]

        current_turn = Color.WHITE
        potential_winner = current_turn

        colors = ("b", "w")
        suffix = ("k", "q", "r", "b", "n", "p")
        i = 0

        # Loads in and scales all assets
        for color in colors:
            for letter in suffix:
                temp = self.asset_load(f"{color}{letter}")
                self.piece_image[i].append(self.load_and_scale_sprite(temp))
            i += 1

            ip = ''
            x = 0
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if flip is True:
                        origin = self.mouse_pos_to_index(pos)
                        print(f'origins value is {origin}')
                        flip = False
                        marked = True
                        
                    else:
                        destination = self.mouse_pos_to_index(pos)
                        print(f'destinations value is {destination}')
                        if origin is not None and destination is not None:   
                            if self.board.get_piece(origin).get_color() == current_turn:
                                (succeeded, status, pieces) = self.board.move(origin, destination)
                                
                                # Check if it worked
                                if succeeded:

                                    ip = self.narrator.generate_move_text(origin,
                                                                        destination,
                                                                        pieces[0],
                                                                        pieces[1])
                                    potential_winner = current_turn
                                    current_turn = self.change_turn(current_turn)
                                    if len(self.board.get_valid_moves(current_turn)) == 0:
                                        self.game_has_ended = True
                                        self.running = False
                        self.input_user_move(origin, destination)
                        flip = True
                        marked = False

                if event.type == pygame.QUIT:
                    self.running = False

            # paint the background
            self.screen.fill(((43, 42, 51)))

            # call the show_chessboard function and draw the chessboard
            self.show_chess_board(self.board.get_chessboard())

            # If something is marked, draw a yellow box around it's cordinates
            if marked:
                self.draw_selection(origin)

            # text for the textbox


            # textbox starts at 602,0
            self.text_wrap(self.screen, ip, (602, 30), pygame.font.SysFont('Arial', 20))
            self.draw_turn(current_turn)
            pygame.display.flip()
        if self.game_has_ended:
            self.show_end_screen(potential_winner)
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    def change_turn(self, turn: Color) -> Color:
        if turn == Color.WHITE:
            return Color.BLACK
        else:
            return Color.WHITE

    def mouse_pos_to_index(self, pos):
        '''Returns the current mouse position as a board (row,column)'''
        x, y = pos
        if x > 601:
            return None
        else:
            row = y // self.SQUARE_SIZE
            col = x // self.SQUARE_SIZE

            print(f"({row},{col})")
        
        return Position(row, col)

    def text_wrap(self, surface, text, pos, font, color=pygame.Color('white')):
        '''Creates a textbox at the given co-ordinates and wraps the supplied text within it'''
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def show_splash_screen(self):
        '''Shows a short splashscreen with text'''
        # Display game name, authors, date/build

        # Display text in the middle of the screen
        text = self.font.render("Sago-Shack, by: Hampus, John & Simon", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (self.size[0] // 2, self.size[1] // 2)
        self.screen.blit(text, text_rect)

        #Draw the text
        pygame.display.flip()
        
        #Wait 500 ms
        pygame.time.delay(500)

        pass

    def show_end_screen(self, winner: Color):
        '''Shows a short splashscreen with text'''
        # Display game name, authors, date/build

        # Display text in the middle of the screen
        text = self.font.render(f" {str(winner)[0:1]}{str(winner)[1:].lower()} won the game", True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.size[0] // 2, self.size[1] // 2)
        self.screen.blit(text, text_rect)

        # Draw the text
        pygame.time.delay(500)
        pygame.display.flip()
        
        # Wait 500 ms
        pygame.time.delay(10000)

        pass

    def asset_load(self, target: str):
       '''A function that returns the image_path'''

       asset_filepath = os.path.join(self.asset_path, target)
       image_path = os.path.join(f'{asset_filepath}.png')

       return image_path

    def input_game_setup_parameters():
        # Present user with successive choices of:
        # 1 or 2 player game (if 1, 2nd player is computer) 1 player == True
        # Time limit per move in seconds, integer
        # AI narration On/Off
        # return ( two_player True/False , sec time limit integer, narration True/False)
        pass

    def piece_type_to_sprite_name(self, chess_piece: PieceType):
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

    def show_chess_board(self, Chessboard: list):
        '''First draws the black and white squares on the chessboard, then draws the sprites on top of the tiles'''
        for row in range(8):
            for col in range(8):
                x, y = col * self.SQUARE_SIZE, row * self.SQUARE_SIZE
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, self.WHITE, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.screen, self.BLACK, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))

        row_index = 0
        for row in Chessboard:
            self.paint_chess_board_row(row_index, row)
            row_index += 1

    def paint_chess_board_row(self, row_index, row_list):
        '''Given the row_index and row_list, draws the sprites in their given position'''
        x_step = self.SQUARE_SIZE
        y = self.SQUARE_SIZE * row_index

        i = 0
        for square in row_list:
            if square is not EMPTY_PIECE:
                image_name = self.piece_type_to_sprite_name(square)
                self.draw_sprite(image_name, x_step*i, y,)
            i += 1

    def recount_user_move():
        # Input two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]
        # Recount previous move to user by text or possibly graphically
        pass

    def input_user_move(self, origin, destination):

        # Used to input the user's move either through algebraic notation or graphical interacivity
        # returns two 2-tupels. Origin, Dest.
        # 2-tuple form is (row, column) were each element is integer [0,7]

        if origin == destination:
            return None
        else:
            return (origin, destination)

    def input_promotion():
        # Prompt's user to select promotion for pawn in question
        # Multiple choice: queen, rook, bishop or knight
        # Either by text (q, r, b or k) or graphical interaction
        # return  integer in [0,3]. 0 == queen, 1 == r and so on.
        pass

    def draw_turn(self, current_turn):
        if current_turn is Color.WHITE:
            ip = 'white'
        else:
            ip = 'black'

        self.text_wrap(self.screen, ip, (602, 0), pygame.font.SysFont('Arial', 25))

    def draw_sprite(self, sprite, x, y):
        '''Given a sprite path, draws a single sprite at a given coordinate'''

        self.screen.blit(sprite, (x, y))

    def load_and_scale_sprite(self, sprite_path):
        '''Given a sprite, imports and scales the sprite down to an appropriate size '''
        # Load the sprite image
        sprite_image = pygame.image.load(sprite_path)

        # Get the original dimensions
        original_width, original_height = sprite_image.get_size()

        # Scale the sprite to half of its original size
        scaled_width = original_width // 2
        scaled_height = original_height // 2

        # Scale the sprite image
        scaled_sprite = pygame.transform.scale(sprite_image, (scaled_width, scaled_height))

        return scaled_sprite

    def get_mouse_pos(self):
        '''Gets the mouse position in a (x,y)-format'''
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(f"Mouse Position: x={mouse_x}, y={mouse_y}")

    def draw_selection(self, position: Position):
        '''Given a Position draw a hollowed out yellow rectangle at the given coordinate unless Position is None, then return None'''

        if position == None:
            return None
        else:
            y = position.row
            x = position.col

            pygame.draw.rect(self.screen, self.YELLOW, (x*self.SQUARE_SIZE,y*self.SQUARE_SIZE,self.SQUARE_SIZE,self.SQUARE_SIZE),2)

if __name__ == "__main__":
    game = Window_Class()
    game.run()
