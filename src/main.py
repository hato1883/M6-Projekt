from chess_piece import ChessPiece
import text_user_interface as ui
import chessboard as logic
from piece_color import Color
from status_enum import Status

if __name__ == "__main__":
    tui = ui.TextUserInterface()
    chessboard = logic.Chessboard()

    tui.show_splash_screen("@", 40, "Sagoschak", "DVA-J", "2023-10-17", "Welcome to Sagoschack!")

    (is_two_player, time_limit, ai_naration) = tui.input_game_setup_parameters()
    chessboard.create_default_board()

    has_ended = False

    while not has_ended:
        # TODO: check if king is being attacked.
        # TODO: If king is attacked, can the king move, Or can something block attacker.
        for color_turn in list(Color)[:2]:
            print(color_turn)
            tui.show_chess_board(chessboard.get_chessboard())
            while True: # Wait for valid move
                (origin, dest) = tui.input_user_move()

                # Check if origion contains piece of color equal to color_turn
                (origin_row, origin_col) = origin
                if chessboard.get_piece(origin) == None:
                    # Can't move a empty position

                    # TODO: TextUserInterface needs to display that move is invalid
                    continue

                if chessboard.get_piece(origin).get_color() != color_turn:
                    # Can't move enemy piece on your turn

                    # TODO: TextUserInterface needs to display that move is invalid
                    continue

                # Move chess piece
                (succeeded, status) = chessboard.move(origin, dest)

                # Check if it worked
                if not succeeded:
                    # Moved failed valid check
                    
                    # TODO: TextUserInterface needs to display that move is invalid
                    continue

                # Did a Pawn promote?
                if status == Status.PAWN_PROMOTION:
                    # Remove pawn
                    chessboard.remove_piece(dest)
                    # Add chosen promoted piece
                    chessboard.add_piece(ChessPiece(color_turn, tui.input_promotion()), dest)
                
                # End this players turn.
                break
        # Next color
        continue
    # Game has ended


    