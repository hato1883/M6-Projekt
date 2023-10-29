import pygame
import sys
from ui_interface import UI_Interface
ui = UI_Interface

WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8  # Divide the width into 8 squares

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ui.show_splash_screen

def open_window():
    pygame.init()
    def draw_chessboard():
        for row in range(8):
            for col in range(8):
                x, y = col * SQUARE_SIZE, row * SQUARE_SIZE
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(screen, BLACK, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    # Define the window size
    window_size = (WIDTH, HEIGHT)

    # Create the window
    screen = pygame.display.set_mode(window_size)

    # Set the window title
    pygame.display.set_caption("Pygame Window with Moving Circle and chessboard")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        

        # Draw the chessboard
        draw_chessboard()
        # Update the display
        pygame.display.flip()

    # Quit pygame and exit the program
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    open_window()

   