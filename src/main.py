from tkinter import N
from chess_piece_class import EMPTY_PIECE, ChessPiece
import text_user_interface as ui
from ui_interface import UI_Interface
import chatgpt_narrator as gpt
import normal_narrator as nn
from narration_interface import NarrationInterface
import chessboard as logic
from piece_color_enum import Color
from status_enum import Status

if __name__ == "__main__":
    tui: UI_Interface = ui.TextUserInterface()
    narrator: NarrationInterface = gpt.ChatGPTNarrator()
    chessboard = logic.Chessboard()

    # show titel screen
    tui.show_splash_screen("@", 40, "Sagoschak", "DVA-J",
                           "2023-10-17", "Welcome to Sagoschack!")

    # get game parameters
    (ai_naration) = tui.input_game_setup_parameters()

    if ai_naration:
        narrator: NarrationInterface = gpt.ChatGPTNarrator()
    else:
        narrator: NarrationInterface = nn.NormalNarrator()

    # create the default 8x8 board
    chessboard.create_default_board()

    # game state bool
    has_ended = False

    ai_naration_text = ""
    while not has_ended:
        # TODO: check if king is being attacked.
        # TODO: If king is attacked, can the king move,
        # Or can something block attacker.
        for color_turn in list(Color)[:2]:

            # Show user the chess board
            tui.show_chess_board(chessboard.get_chessboard(), ai_naration_text)

            # Loop until valid move
            while True:  # Wait for valid move
                # get origin and destination of the move
                (origin, dest) = tui.input_user_move()

                # Check if origin contains piece
                # of color equal to current player
                if chessboard.get_piece(origin).get_color() != color_turn:
                    # Can't move enemy piece on your turn

                    # TODO: TextUserInterface needs
                    # to display that move is invalid
                    continue

                # Move chess piece
                (succeeded, status, pieces) = chessboard.move(origin, dest)
                # Check if it worked
                if not succeeded:
                    # Moved failed valid check

                    # TODO: TextUserInterface needs
                    # to display that move is invalid
                    continue

                ai_naration_text = narrator.generate_move_text(origin,
                                                               dest,
                                                               pieces[0],
                                                               pieces[1])

                # Did a Pawn promote?
                if status is Status.PAWN_PROMOTION:
                    # Remove pawn
                    chessboard.remove_piece(origin)

                    # Remove piece on destination
                    chessboard.remove_piece(dest)

                    # Add chosen promoted piece
                    chessboard.add_piece(ChessPiece(color_turn,
                                                    tui.input_promotion()),
                                         dest)

                # End this players turn.
                break

        # Next color
        continue
    # Game has ended
