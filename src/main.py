from tkinter import N
from chess_piece_class import EMPTY_PIECE, ChessPiece
from text_formater import TextFormater
import text_user_interface as ui
import gui as gui
from ui_interface import UI_Interface
import chatgpt_narrator as gpt
import normal_narrator as nn
from narration_interface import NarrationInterface
import chessboard as logic
from piece_color_enum import Color
from status_enum import Status


def input_game_setup_parameters():
    """ Asks user to whether AI-narration should be On/Off, returns True for Yes"""
    ai_narration = False
    text_display = False

    while True:
        
        answer = None
        while answer not in ("y", "yes", "n", "no"):

            answer = input("AI Narration(y/n): ").lower()
        
        if answer[0] == "y":
            ai_narration = True

        answer = None
        while answer not in ("y", "yes", "n", "no"):

            answer = input("Text Display(y/n): ").lower()
        
        if answer[0] == "y":
            text_display = True

        current_setting = f"|AI Narration: { 'On' if ai_narration == True else 'Off' }, Text Display: { 'On' if text_display == True else 'Off' }|"

        TextFormater.print_divider("-", len(current_setting))
        print(current_setting)
        TextFormater.print_divider("-", len(current_setting))

        answer = None
        while answer not in ("y", "yes", "n", "no"):

            answer = input("Proceed(y/n): ").lower()

        if answer[0] == "y":
            break

    return (ai_narration, text_display)


if __name__ == "__main__":
    display: UI_Interface
    narrator: NarrationInterface
    chessboard = logic.Chessboard()

    # create the default 8x8 board
    chessboard.create_default_board()

    # get game parameters
    (ai_naration, text_display) = input_game_setup_parameters()

    if ai_naration:
        narrator: NarrationInterface = gpt.ChatGPTNarrator()
    else:
        narrator: NarrationInterface = nn.NormalNarrator()

    if text_display:
        display = ui.TextUserInterface(chessboard, narrator)
    else:
        display = gui.Window_Class(chessboard, narrator)

    display.run()
    # game state bool
