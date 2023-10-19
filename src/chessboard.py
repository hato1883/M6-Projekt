from piece_type import PieceType
from chess_piece import ChessPiece
from piece_color import Color
from move_type import MoveType
from move_option import MoveOption

class Chessboard:

    def __init__(self) -> None:
        self.chessboard_list: list[ChessPiece] = []


    def create_board(self, size=8):
        """Creates a empty board with given size (default is 8)
        
        returns None (new chessboard is saved in object)
        """
        self.chessboard_list = []
        for row in range(size):
            col = [None]*size
            self.chessboard_list.append(col)
        return None
    
    
    def create_default_board(self):
        """Creates the default 8x8 chess board with 16 pieces in each color
        
        returns None (new chessboard is saved in object)
        """
        self.create_board()


    def add_piece(self, chess_piece, pos):
        """adds a chess piece to specifed empty position
        
        returns True if the position was empty, returns False if it was already taken
        """
        (row, col) = pos
        if self.chessboard_list[row][col] is None:
            self.chessboard_list[row][col] = chess_piece
            return True
        return False


    def remove_piece(self, pos):
        """adds a chess piece to specifed empty position
        
        returns True if the position was not empty, else returns False
        """
        (row, col) = pos
        if self.chessboard_list[row][col] is not None:
            self.chessboard_list[row][col] = None
            return True
        return False


    def is_valid(self, origin, dest):
        (orgin_row, orgin_col) = origin
        chess_piece = self.chessboard_list[orgin_row][orgin_col].get_type()
        valid_move = False
        match chess_piece:
            case PieceType.PAWN:
                valid_move = valid_pawn_move(origin, dest)
                pass
            case PieceType.ROOK:
                valid_move = valid_rook_move(origin, dest)
                pass
            case PieceType.KNIGHT:
                valid_move = valid_knight_move(origin, dest)
                pass
            case PieceType.BISHOP:
                valid_move = valid_bishop_move(origin, dest)
                pass
            case PieceType.QUEEN:
                valid_move = valid_queen_move(origin, dest)
                pass
            case PieceType.KING:
                valid_move = valid_king_move(origin, dest)
                pass
        return valid_move


    def in_danger(self, origin: tuple[int, int], piece_color : Color) -> bool:
        (origin_row, origin_col) = origin

        chess_piece_type: PieceType
        for chess_piece_type in PieceType:
            # Check all pieces

            offset_row: int
            offset_col: int
            moves: list[tuple[MoveType,list[MoveOption]]]
            for ((offset_row , offset_col), moves) in chess_piece_type.value: # value to get the associated list
                # Check all moves the piece has
                dest_row: int = origin_row + offset_row
                dest_col: int = origin_col + offset_col
                if not self.__is_in_bounds(origin, (dest_row , dest_col)):
                    # Is out of bounds
                    continue

                # Only offsets within the board are left 
                for (move_type, options) in moves:
                    if MoveOption.TAKE not in options:
                        # move can't attack
                        continue

                    # Only attacking moves are left.
                    
                    
                    # TODO: Propegation move can have enemy pice futher away than default offset.
                    if move_type == MoveType.COLLISION_AXIS or move_type== MoveType.COLLISION_DIAG:
                        # check axis with the same direction as offset from 0,0
  
                        # Contiune loop while origin + offset
                        while self.__is_in_bounds(origin, (dest_row, dest_col)):
                            # we have taken 1 step along the axis OR diag and are still within the board
                            
                            if self.chessboard_list[dest_row][dest_col] == None:
                                # Empty space, no attacker move to next...
                                dest_row += min(1, max(-1, offset_row)) # Next row (if offset is negativ we move 1 step up)
                                dest_col += min(1, max(-1, offset_col)) # Next col (if offset is negativ we move 1 step left)
                                # if both offset are set we will move diagonaly
                                continue
                            
                            # Space is not empty
                            potential_attacker: ChessPiece = self.chessboard_list[dest_row][dest_col]

                            if potential_attacker.get_color() == piece_color:
                                # attacker is in the same faction, can't attack
                                break # We have collided along the path stop looking

                            # Potential attacker is enemy piece
                            if potential_attacker.get_type() != chess_piece_type:
                                # potential attacker dose not contain the correct move. 
                                break # We have collided along the path stop looking

                            # Potential attacker is the same type,
                            # and was not block along the way
                            # therefor it can attack
                            return True
                        
                        else: # End of while loop:
                            # propegation could not find a potential attacker. 
                            return False
                        
                    # Not a propegation move type
                    else: 
                        # is destination empty?
                        if self.chessboard_list[origin_row + offset_row][origin_col + offset_col] == None:
                            # Empty space, no attacker move to next...
                            continue

                        # destination contains a piece
                        potential_attacker: ChessPiece = self.chessboard_list[origin_row + offset_row][origin_col + offset_col]

                        # is it an ally?
                        if potential_attacker.get_color() == piece_color:
                            # piece is allied (same color)
                            continue

                        # Potential attacker is enemy piece
                        # but is it the same piece we are emulating?
                        if potential_attacker.get_type() != chess_piece_type:
                            # potential attacker is not the same
                            continue

                        # Attacker is the same type we are emulating
                        # therfore it can attack origin
                        return True
                # end of for-loop,
                # Test next move in the list
            
            # Checked all moves in the list for a given piece
            # Test next piece
        
        # Checked all pieces
        # No early return has happend so we can safely assuem the is no danger
        return False



    def __is_in_bounds(self, origin: tuple[int, int], offset: tuple[int, int]) -> bool:
        (origin_row, origin_col) = origin
        (offset_row, offset_col) = offset

        # Check if row is within 0 and len(self.chessboard_list) (exclusive)
        # Check for negative case
        if origin_row + offset_row >= len(self.chessboard_list):
            # Row to large
            return False
        if origin_row + offset_row < 0:
            # Row to small
            return False

        # Check if column is within 0 and len(self.chessboard_list) (exclusive)
        # Check for negative case
        if origin_col + offset_col >= len(self.chessboard_list):
            # Col to large
            return False
        if origin_col + offset_col < 0:
            # Col to small
            return False
        return True
