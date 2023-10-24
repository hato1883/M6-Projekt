from narration_interface import *
import openai
import json
 
# Opening JSON file
config = open('config.json')
 
# returns JSON object as 
# a dictionary
data = json.load(config)
openai.api_key = data['openai-api']
print(openai.api_key)

class ChatGPTNarrator(NarrationInterface):
   
    @classmethod    
    def generate_move_text(cls, origin: Position, destination: Position, moved_piece: ChessPiece, attacked_piece: ChessPiece) -> str:
        if attacked_piece is None:
            return f"The {str(moved_piece.get_color()).lower()} {str(moved_piece.get_type()).lower()} on {cls.index_to_alpha_numeral(origin)} moved to {cls.index_to_alpha_numeral(destination)}"
        else:
            prompt = f"Describe dramaticly how the {str(moved_piece.get_color()).lower()} {str(moved_piece.get_type()).lower()} on {cls.index_to_alpha_numeral(origin)} takes {str(attacked_piece.get_color()).lower()} {str(attacked_piece.get_type()).lower()} at {cls.index_to_alpha_numeral(destination)} on a chess board in 3 sentances"
    
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=240
            )
            return response.choices[0].text.strip()
        