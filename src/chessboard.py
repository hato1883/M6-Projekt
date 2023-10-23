from piece_type_enum import PieceType
from chess_piece_class import ChessPiece
from piece_color_enum import Color
from move_type_enum import MoveType
from move_option_enum import MoveOption
from chess_piece_class import ChessPiece
from status_enum import Status
from position_class import Position

class Chessboard:

    def __init__(self, chessboard: list[list[ChessPiece]] = []) -> None:
        # chessboard is a 2d list of ChessPiece objects
        self._chessboard: list[list[ChessPiece]] = chessboard

        # Move history is a list of tuple of ChessPiece, origin and destination
        # Moves are in order (1st move is at index 0 2nd move if on index 1 etc)
        self.move_history: list[tuple[ChessPiece, tuple[MoveType, list[MoveOption]], Position, Position]] = []

        # A dictionary of all king PieceType on this instance of chessboard.
        # Key will be the king's current location, and value will be a ref to the king (ChessPiece)
        self._kings_location: dict[Position: ChessPiece] = {}

        # size of chessboard
        self._board_size: int = len(self._chessboard)

        if len(chessboard) != 0:
            # Find kings in loaded list
            for row in range(len(chessboard)):
                for col in range(len(chessboard)):
                    if chessboard[row][col] is None:
                        continue
                    if chessboard[row][col].get_type() is PieceType.KING:
                        # add king chess piece to list
                        self._kings_location[Position(row, col)] = chessboard[row][col]



    def create_board(self, size: int = 8):
        """Creates a empty board with given size (default is 8)
        
        returns None (new chessboard is saved in object)
        """
        self._chessboard = []
        for row in range(size):
            col = [None]*size
            self._chessboard.append(col)
        
        self._board_size: int = len(self._chessboard)
    
    
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
        self._chessboard: list[list[ChessPiece]] = [
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
        self._kings_location[Position(0, 4)] = b_ki
        self._kings_location[Position(7, 4)] = w_ki


    def get_piece(self, origin: Position) -> ChessPiece:
        """Get a chess piece at destination

        origin the posistion to retrive
        
        Returns a ChessPiece or None if it was empty"""
        return self._chessboard[origin.row][origin.col]


    def add_piece(self, chess_piece: ChessPiece, dest: Position):
        """adds a chess piece to specifed empty position
        
        returns True if the position was empty, returns False if it was already taken
        """
        if self._chessboard[dest.row][dest.col] is None:

            # if we are adding a king then add it to king dict
            if chess_piece.get_type() is PieceType.KING:
                self._kings_location[dest] = chess_piece

            self._chessboard[dest.row][dest.col] = chess_piece
            return True
        return False


    def remove_piece(self, dest: Position):
        """adds a chess piece to specifed empty position
        
        returns True if the position was not empty, else returns False
        """
        if self._chessboard[dest.row][dest.col] is not None:

            # if we are removing a king then remove it from king dict
            if self.get_piece(dest).get_type() is PieceType.KING:
                del self._kings_location[dest]

            self._chessboard[dest.row][dest.col] = None
            return True
        return False


    def move(self, origin: Position, dest: Position) -> tuple[bool, Status]:
        # Check if move is valid
        (valid, move) = self.is_valid(origin, dest)
        if valid:
            # Move is valid

            # Get chess piece at origin
            moved_piece = self._chessboard[origin.row][origin.col]

            # Add move to move_history (at end of list)
            self.move_history.append((moved_piece, move, origin, dest))

            # Check if this piece is has moved before
            if not moved_piece.get_has_moved():
                # It has now
                moved_piece.set_has_moved_true()
            
            # Check if piece is a Pawn
            if moved_piece.get_type() is PieceType.PAWN:
                # Pawn might promote at edge

                # get Color of pawn
                # TODO: add generalised search depending on Pawn direction.
                match moved_piece.get_color():
                    case Color.WHITE:
                        # Piece is moving towards 0
                        if dest.row == 0:
                            return (True, Status.PAWN_PROMOTION)
                        
                    case Color.BLACK:
                        # Piece is moving towards max size
                        if dest.row == self._board_size-1:
                            return (True, Status.PAWN_PROMOTION)
                # End of Pawn Promotion check

            # is destination Empty?       
            if self._chessboard[dest.row][dest.col] is not None:
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
        

    def is_valid(self, origin: Position, dest: Position) -> tuple[bool, tuple[MoveType, list[MoveOption]]]:

        # is origin out of bounds
        if self.__is_in_bounds(origin, Position(0, 0)):
            # Invalid move, Can't move from a pos that is out of bounds.
            return (False, None)
        
        # is destnation out of bounds
        if self.__is_in_bounds(dest, Position(0, 0)):
            # Invalid move, Can't move to a dest that is out of bounds.
            return (False, None)

        # is destnation empty
        if self.get_piece(origin) is None:
            # Invalid move, Can't move empty tile.
            return (False, None)
        
        chess_piece: PieceType = self.chessboard[origin.row][origin.col].get_type()
        
        offset: Position
        moves: list[tuple[MoveType, list[MoveOption]]]

        for (offset, moves) in chess_piece.value: # value to get the associated list
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
                        if self.__is_king_castling_valid(origin, dest):
                            # Move is valid, no need to check the remaining moves
                            return (True, (move_type, options))
                        # Check next move in list
                        continue

                    case MoveType.PAWN_EN_PASSANT:
                        if self.__is_pawn_en_passant_valid(origin, dest):
                            # Move is valid, no need to check the remaining moves
                            return (True, (move_type, options))
                        # Check next move in list
                        continue
                # Move type has been checked
            # Move has been evaluated
        # All moves have been check, none did a early exit with return
        # Move must be invalid
        # return (False, None)
            
        # Debugg
        return True
    

    def __is_king_castling_valid(self, origin: Position, dest: Position) -> bool:
        """Private Helper Method: Checks if a king castling type move is valid to destination.
        
        Returns True if all of the requierments are met otherwise returns False

        Requierments for valid move are:
          1. origin piece (normaly the king) has NOT moved before
          2. origin piece can not be under threat
          3. space between origin piece and rook must be empty
          4. can only castle with PieceType.ROOK
          5. rook piece has NOT moved before
          6. distance between rook and origin must be atleast 2 tiles (2 empty spots between them)
          7. destination can not be under threat
          8. rook destination can not be under threat
        """

        # Check if origin has moved before (req 1)
        if self.get_piece(origin).get_has_moved():
            # Castling is not valid if origin piece has moved.
            return False
        
        # Check if origin is attacked (req 2)
        if self.in_danger(origin, self.get_piece(origin).get_color()):
            # Can't castle when attacked
            return False
        
        # unbox tuple
        
        # Check if destination is left or right of king
        if origin.col > dest.col:
            # origin is to the right of dest so rook is towards the left
            for searched_col in range(origin.col-1, -1, -1):

                # Check if spot is empty (req 3)
                if self.get_piece((origin.row, searched_col)) is None:

                    # Check if the 2 spaces left of king is not under threat (req 7 & 8)
                    if abs(origin.col - searched_col) <= 2:
                        if self.in_danger((origin.row, searched_col), self.get_piece(origin).get_color()):
                            # Origin team will be attacked on this square which is not OK
                            break

                    # Empty continue to next col
                    continue

                # col contains a chess piece
                # Is it a rook? (req 4)
                if self.get_piece((origin.row, searched_col)).get_type() is not PieceType.ROOK:
                    
                    # Not a rook exit loop
                    break

                # Piece is a Rook
                # Has the rook moved? (req 5)
                if self.get_piece((origin.row, searched_col)).get_has_moved():

                    # Rook has moved and therfor can not castle
                    break

                # Rook has not moved
                # Do we have space to castle? (req 6) 
                if abs(origin.col - searched_col) <= 2:

                    # not enough space to castle
                    break

                # all requierments are met
                return True
            # Not valid to castle to the left
        else:
            # origin is left of dest
            # check right side
            for searched_col in range(origin.col+1, self._board_size, 1):
                
                # Check if spot is empty (req 3)
                if self.get_piece((origin.row, searched_col)) is None:

                    # Check if the 2 spaces left of king is not under threat (req 7 & 8)
                    if abs(origin.col - searched_col) <= 2:
                        if self.in_danger((origin.row, searched_col), self.get_piece(origin).get_color()):
                            # Origin team will be attacked on this square which is not OK
                            break

                    # Empty continue to next col
                    continue

                # col contains a chess piece
                # Is it a rook? (req 4)
                if self.get_piece((origin.row, searched_col)).get_type() is not PieceType.ROOK:
                    
                    # Not a rook exit loop
                    break

                # Piece is a Rook
                # Has the rook moved? (req 5)
                if self.get_piece((origin.row, searched_col)).get_has_moved():

                    # Rook has moved and therfor can not castle
                    break

                # Rook has not moved
                # Do we have space to castle? (req 6) 
                if abs(origin.col - searched_col) <= 2:

                    # not enough space to castle
                    break

                # all requierments are met
                return True
            # end of for-loop
        
        # Move must be invalid.
        return False


    def __is_pawn_en_passant_valid(self, origin: Position, dest: Position) -> bool:
        """Private Helper method: Checks if Pawn En Passant MoveType is valid

        Returns True if all of the requierments are met otherwise returns False

        Requierments for valid move are:
          1. Origin must be a PieceType.PAWN
          2. Destination must be empty
          3. The tile (origin_row, dest_col) must contain enemy pawn (enemy pawn adjecent to origin)
          4. Enemy pawn must have moved using a move with the MoveOption.FIRST
        """

        # check if origin is a Pawn (req 1)
        if self.get_piece(origin).get_type() is not PieceType.PAWN:
            # None pawn pieces are not allowed to preform this move
            return False
        
        # Piece is a PAWN
        # Check if dest is empty (req 2)
        if self.get_piece(dest) is not None:
            # destination is occupied, en passant is not valid
            return False
        # destination is empty

        # check if there is a enemy pawn in destination colum that is on origins row
        # In other words if ther is a enemy pawn next to origins position
        if self.get_piece((origin.row, dest.col)) is None:
            # No Enemy Pawn next to origin, so en passant is invalid
            return False
        
        # origin_row, dest_col must contain a pawn (req 3)
        if self.get_piece((origin.row, dest.col)).get_type() is not PieceType.PAWN:
            # Not a pawn, Not valid
            return False
        
        if self.get_piece((origin.row, dest.col)).get_color() is self.get_piece(origin).get_color():
            # Allied pawn, Not valid
            return False
        
        # Enemy pawn is adjecent to origin and destination is empty.
        # Check move_history to see if enemy pawn moved adjecent last move
        # keep checking the latest move until we get one of the piece color
        # (req 4)
        
        move_index = len(self.get_move_history()) - 1 # last index
        (moved_piece, used_move, move_origin, move_dest) = self.get_move_history()[move_index]
        while moved_piece.get_color() is not self.get_piece((origin.row, dest.col)).get_color():
            # Move is not from the same player as what we are checking

            # next move
            move_index -= 1

            # check so we are not indexing outside list
            if move_index < 0:
                # move_index cant be less than 0
                # that would mean that the searched color has not made a move yet.
                break
            
            # index is in range, get next move
            (moved_piece, used_move, move_origin, move_dest) = self.get_move_history()[move_index]
        else:
            # Found move from enemy pawn color
            # Check if found move is to the pawn destination
            if move_dest != Position(origin.row, dest.col):
                # was not the move that moved the pawn
                # pawn was moved more than 1 turn ago so En passant is invalid
                return False
            
            # Enemy pawn was moved to location last move
            (used_move_type, used_move_options) = used_move
            # check if it was a double forward move or another type.
            if MoveOption.FIRST not in used_move_options:
                # move was not a double forward move
                # double forward move has MoveOption.FIRST flag
                return False
            
            # Move is valid
            return True

        # loop was broken, in other words enemy player has not made a move yet
        # En Passant can't be valid.
        return False
    

    def in_danger(self, origin: Position, piece_color : Color) -> bool:

        chess_piece_type: PieceType
        for chess_piece_type in PieceType:
            # Check all pieces

            offset_row: int
            offset_col: int
            moves: list[tuple[MoveType,list[MoveOption]]]
            for ((offset_row, offset_col), moves) in chess_piece_type.value: # value to get the associated list
                # Check all moves the piece has
                if not self.__is_in_bounds(origin, Position(offset_row, offset_col)):
                    # Is out of bounds
                    continue

                dest: Position = Position(origin.row + offset_row, origin.col + offset_col)

                # Only offsets within the board are left 
                for (move_type, options) in moves:
                    if MoveOption.TAKE not in options:
                        # move can't attack
                        continue

                    # Only attacking moves are left.

                    if move_type is MoveType.COLLISION_AXIS or move_type is MoveType.COLLISION_DIAG:
                        # check axis with the same direction as offset from 0,0
  
                        # Contiune loop while origin + offset
                        while self.__is_in_bounds(origin, Position(offset_row, offset_col)):
                            # we have taken 1 step along the axis OR diag and are still within the board

                            if self._chessboard[dest.row][dest.col] is None:
                                # Empty space, no attacker move to next...
                                offset_row += min(1, max(-1, offset_row)) # Next row (if offset is negativ we move 1 step up)
                                offset_col += min(1, max(-1, offset_col)) # Next col (if offset is negativ we move 1 step left)
                                
                                dest.row = origin.row + offset_row
                                dest.col = origin.col + offset_col
                                # if both offset are set we will move diagonaly
                                continue

                            # Space is not empty
                            potential_attacker: ChessPiece = self._chessboard[dest.row][dest.col]

                            if potential_attacker.get_color() is piece_color:
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
                        if self._chessboard[origin.row + offset_row][origin.col + offset_col] is None:
                            # Empty space, no attacker move to next...
                            continue

                        # destination contains a piece
                        potential_attacker: ChessPiece = self._chessboard[origin.row + offset_row][origin.col + offset_col]

                        # is it an ally?
                        if potential_attacker.get_color() is piece_color:
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


    def __is_in_bounds(self, origin: Position, offset: Position) -> bool:

        # Check if row is within 0 and self._board_size (exclusive)
        # Check for negative case
        if origin.row + offset.row >= self._board_size:
            # Row to large
            return False
        if origin.row + offset.row < 0:
            # Row to small
            return False

        # Check if column is within 0 and self._board_size (exclusive)
        # Check for negative case
        if origin.col + offset.col >= self._board_size:
            # Col to large
            return False
        if origin.col + offset.col < 0:
            # Col to small
            return False
        return True
    

    def get_chessboard(self) -> list[list[ChessPiece]]:
        return self._chessboard
    

    def set_chessboard(self, chessboard: list[list[ChessPiece]]) -> None:
        self._chessboard = chessboard


    def get_move_history(self) -> list[tuple[ChessPiece, tuple[MoveType, list[MoveOption]], Position, Position]]:
        """Retrives the move history list
        
        returns a list of type list[ tuple[ ChessPiece, tuple[MoveType, list[MoveOption]], Position, Position]]
        where ChessPiece stores information of PieceType and PieceColor
        1st tuple stores the valid move used and its options,
        1st Position obj is the move origin and
        2nd Position obj is move destination"""
        return self.move_history
    

    def reset_move_history(self) -> None:
        """Clears the instance move history
        
        Useful if reseting chessboard instance"""
        self._move_history.clear


    def __str__(self) -> str:
        out = ""
        for row in range(self._board_size):
            for col in range(self._board_size):
                out += f"[{str(self._chessboard[row][col])}],"
            out += "\n"
        return out
    
    
    def __eq__(self, __value: object) -> bool:
        
        if isinstance(__value, self.__class__):

            # check chessboard
            if self._chessboard != __value._chessboard:
                return False
            
            # check move_history
            if self.move_history != __value.move_history:
                return False
            
            # check king dict
            if self._kings_location != __value._kings_location:
                return False

            return True
        else:
            return NotImplemented
        
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
    