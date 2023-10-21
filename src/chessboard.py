from piece_type import PieceType
from chess_piece import ChessPiece
from piece_color import Color
from move_type import MoveType
from move_option import MoveOption
from chess_piece import ChessPiece
from status_enum import Status

class Chessboard:

    def __init__(self, chessboard: list[list[ChessPiece]] = []) -> None:
        # chessboard is a 2d list of ChessPiece objects
        self.chessboard: list[list[ChessPiece]] = chessboard

        # Move history is a list of tuple of ChessPiece, origin and destination
        # Moves are in order (1st move is at index 0 2nd move if on index 1 etc)
        self.move_history: list[tuple[ChessPiece, tuple[int, int], tuple[int, int]]] = []

        # A dictionary of all king PieceType on this instance of chessboard.
        # Key will be the king's current location, and value will be a ref to the king (ChessPiece)
        self.kings_location: dict[tuple[int, int]: ChessPiece] = {}


    def create_board(self, size: int = 8):
        """Creates a empty board with given size (default is 8)
        
        returns None (new chessboard is saved in object)
        """
        self.chessboard = []
        for row in range(size):
            col = [None]*size
            self.chessboard.append(col)
        return None
    
    
    def create_default_board(self):
        """Creates the default 8x8 chess board with 16 pieces in each color
        
        returns None (new chessboard is saved in object)
        """
        self.create_board()

         # Black Pieces
        b_ro = ChessPiece(Color.BLACK, PieceType.ROOK)
        b_kn = ChessPiece(Color.BLACK, PieceType.KNIGHT)
        b_bi = ChessPiece(Color.BLACK, PieceType.BISHOP)
        b_qu = ChessPiece(Color.BLACK, PieceType.QUEEN)
        b_ki = ChessPiece(Color.BLACK, PieceType.KING)
        b_pa = ChessPiece(Color.BLACK, PieceType.PAWN)
        # White Pieces
        w_ro = ChessPiece(Color.WHITE, PieceType.ROOK)
        w_kn = ChessPiece(Color.WHITE, PieceType.KNIGHT)
        w_bi = ChessPiece(Color.WHITE, PieceType.BISHOP)
        w_qu = ChessPiece(Color.WHITE, PieceType.QUEEN)
        w_ki = ChessPiece(Color.WHITE, PieceType.KING)
        w_pa = ChessPiece(Color.WHITE, PieceType.PAWN)
        self.chessboard: list[list[ChessPiece]] = [
            [b_ro, b_kn, b_bi, b_qu, b_ki, b_bi, b_kn, b_ro],
            [b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa, b_pa],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa, w_pa],
            [w_ro, w_kn, w_bi, w_qu, w_ki, w_bi, w_kn, w_ro],
        ]

        # Add kings to dictionary so we can check if they are in danger later.
        self.kings_location[(0, 4)] = b_ki
        self.kings_location[(7, 4)] = w_ki


    def get_piece(self, origin: tuple[int, int]) -> ChessPiece:
        """Get a chess piece at destination

        origin the posistion to retrive
        
        Returns a ChessPiece or None if it was empty"""
        (row, col) = origin
        return self.chessboard[row][col]


    def add_piece(self, chess_piece: ChessPiece, pos: tuple[int, int]):
        """adds a chess piece to specifed empty position
        
        returns True if the position was empty, returns False if it was already taken
        """
        (row, col) = pos
        if self.chessboard[row][col] is None:

            # if we are adding a king then add it to king dict
            if chess_piece.get_type() == PieceType.KING:
                self.kings_location[pos] = chess_piece

            self.chessboard[row][col] = chess_piece
            return True
        return False


    def remove_piece(self, pos: tuple[int, int]):
        """adds a chess piece to specifed empty position
        
        returns True if the position was not empty, else returns False
        """
        (row, col) = pos
        if self.chessboard[row][col] is not None:

            # if we are removing a king then remove it from king dict
            if self.get_piece(pos).get_type() == PieceType.KING:
                del self.kings_location[pos]

            self.chessboard[row][col] = None
            return True
        return False


    def move(self, origin: tuple[int, int], dest: tuple[int, int]) -> tuple[bool, Status]:
        # Check if move is valid
        if self.is_valid(origin, dest):
            # Move is valid

            # Get chess piece at origin
            (origin_row, origin_col) = origin
            moved_piece = self.chessboard[origin_row][origin_col]

            # Add move to move_history (at end of list)
            self.move_history.append((moved_piece, origin, dest))

            # Check if this piece is has moved before
            if not moved_piece.get_has_moved():
                # It has now
                moved_piece.set_has_moved_true()
            
            # Check if piece is a Pawn
            if moved_piece.get_type() == PieceType.PAWN:
                # Pawn might promote at edge
                (dest_row, dest_col) =  dest

                # get Color of pawn
                # TODO: add generalised search depending on Pawn direction.
                match moved_piece.get_color():
                    case Color.WHITE:
                        # Piece is moving towards 0
                        if dest_row == 0:
                            return (True, Status.PAWN_PROMOTION)
                        
                    case Color.BLACK:
                        # Piece is moving towards max size
                        if dest_row == len(self.chessboard)-1:
                            return (True, Status.PAWN_PROMOTION)
                # End of Pawn Promotion check

            # is destination Empty?       
            if self.chessboard[dest_row][dest_col] is not None:
                # Clear destination
                self.remove_piece(dest) 
            
            # Add piece to destination
            self.add_piece(moved_piece, dest)

            # Remove it from origin
            self.remove_piece(origin)

            # Succsesful move
            return (True, Status.SUCCESS)
        else:
            # Move was invalid
            return (False, Status.INVALID_MOVE)
        

    def is_valid(self, origin: tuple[int, int], dest: tuple[int, int]):
        (orgin_row, orgin_col) = origin
        chess_piece: PieceType = self.chessboard[orgin_row][orgin_col].get_type()
        
        for ((offset_row , offset_col), moves) in chess_piece.value: # value to get the associated list
            for (move_type, options) in moves:
                match move_type:
                    case MoveType.COLLISION_AXIS:
                        # evaluate move with given option
                        pass

                    case MoveType.COLLISION_DIAG:
                        # evaluate move with given option
                        pass

                    case MoveType.ABSOLUTE:
                        # evaluate move with given option
                        pass

                    case MoveType.KING_CASTLE:
                        # evaluate move with given option
                        pass

                    case MoveType.PAWN_EN_PASSANT:
                        # evaluate move with given option
                        pass
                # Move type has been checked
            # Move has been evaluated
        # All moves have been check, none did a early exit with return
        # Move must be invalid
        # return False
            
        # Debugg
        return True
    

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
                if not self.__is_in_bounds(origin, (offset_row , offset_col)):
                    # Is out of bounds
                    continue

                dest_row: int = origin_row + offset_row
                dest_col: int = origin_col + offset_col

                # Only offsets within the board are left 
                for (move_type, options) in moves:
                    if MoveOption.TAKE not in options:
                        # move can't attack
                        continue

                    # Only attacking moves are left.

                    if move_type == MoveType.COLLISION_AXIS or move_type== MoveType.COLLISION_DIAG:
                        # check axis with the same direction as offset from 0,0
  
                        # Contiune loop while origin + offset
                        while self.__is_in_bounds(origin, (offset_row, offset_col)):
                            # we have taken 1 step along the axis OR diag and are still within the board

                            if self.chessboard[dest_row][dest_col] == None:
                                # Empty space, no attacker move to next...
                                offset_row += min(1, max(-1, offset_row)) # Next row (if offset is negativ we move 1 step up)
                                offset_col += min(1, max(-1, offset_col)) # Next col (if offset is negativ we move 1 step left)
                                
                                dest_row = origin_row + offset_row
                                dest_col = origin_col + offset_col
                                # if both offset are set we will move diagonaly
                                continue

                            # Space is not empty
                            potential_attacker: ChessPiece = self.chessboard[dest_row][dest_col]

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
                        
                        
                        # End of while loop:
                        # propegation could not find a potential attacker. 
                        
                    # Not a propegation move type
                    else: 
                        # is destination empty?
                        if self.chessboard[origin_row + offset_row][origin_col + offset_col] == None:
                            # Empty space, no attacker move to next...
                            continue

                        # destination contains a piece
                        potential_attacker: ChessPiece = self.chessboard[origin_row + offset_row][origin_col + offset_col]

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
        if origin_row + offset_row >= len(self.chessboard):
            # Row to large
            return False
        if origin_row + offset_row < 0:
            # Row to small
            return False

        # Check if column is within 0 and len(self.chessboard_list) (exclusive)
        # Check for negative case
        if origin_col + offset_col >= len(self.chessboard):
            # Col to large
            return False
        if origin_col + offset_col < 0:
            # Col to small
            return False
        return True
    

    def get_chessboard(self) -> list[list[ChessPiece]]:
        return self.chessboard
    

    def set_chessboard(self, chessboard: list[list[ChessPiece]]) -> None:
        self.chessboard = chessboard


    def get_move_history(self) -> list[ tuple[ ChessPiece, tuple[int, int], tuple[int, int]]]:
        """Retrives the move history list
        
        returns a list of type list[ tuple[ ChessPiece, tuple[int, int], tuple[int, int]]]
        where ChessPiece stores information of PieceType and PieceColor
        and 1st tuple is the move origin and 2nd is move destination"""
        return self.move_history
    

    def reset_move_history(self) -> None:
        """Clears the instance move history
        
        Useful if reseting chessboard instance"""
        self.move_history.clear


    def __str__(self) -> str:
        out = ""
        for row in range(len(self.chessboard)):
            for col in range(len(self.chessboard)):
                out += f"[{str(self.chessboard[row][col])}],"
            out += "\n"
        return out