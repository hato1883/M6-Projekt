from narration_interface import *

class NormalNarrator(NarrationInterface):
   
    @classmethod    
    def generate_move_text(cls, origin: Position, destination: Position, moved_piece: ChessPiece, attacked_piece: ChessPiece) -> str:
        if attacked_piece is None:
            return f"The {str(moved_piece.get_color()).lower()} {str(moved_piece.get_type()).lower()} on {cls.index_to_alpha_numeral(origin)} moved to {cls.index_to_alpha_numeral(destination)}"
        else:
            return f"The {str(moved_piece.get_color()).lower()} {str(moved_piece.get_type()).lower()} on {cls.index_to_alpha_numeral(origin)} takes {str(attacked_piece.get_color()).lower()} {str(attacked_piece.get_type()).lower()} at {cls.index_to_alpha_numeral(destination)}."
        