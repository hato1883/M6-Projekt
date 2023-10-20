from piece_type import PieceType
from chess_piece import ChessPiece
from piece_color import Color
from move_type import MoveType
from move_option import MoveOption
from chess_piece import ChessPiece
import valid_move_helper as vmh

class Chessboard:

    def __init__(self, chessboard: list[list[ChessPiece]] = []) -> None:
        self.chessboard_list: list[list[ChessPiece]] = chessboard


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

        # Add Black Rooks (Black is row 0 and 1)
        black_rook = ChessPiece(Color.BLACK, PieceType.ROOK)
        self.add_piece(black_rook, (0, 0))
        self.add_piece(black_rook, (0, 7))

        # Add Black Knight (Black is row 0 and 1)
        black_knight = ChessPiece(Color.BLACK, PieceType.KNIGHT)
        self.add_piece(black_knight, (0, 1))
        self.add_piece(black_knight, (0, 6))

        # Add Black Bishops (Black is row 0 and 1)
        black_bishop = ChessPiece(Color.BLACK, PieceType.BISHOP)
        self.add_piece(black_bishop, (0, 2))
        self.add_piece(black_bishop, (0, 5))

        # Add Black Queen (Black is row 0 and 1)
        black_queen = ChessPiece(Color.BLACK, PieceType.QUEEN)
        self.add_piece(black_queen, (0, 3))

        # Add Black King (Black is row 0 and 1)
        black_king = ChessPiece(Color.BLACK, PieceType.KING)
        self.add_piece(black_king, (0, 4))

        # Add Black Pawns (Black is row 0 and 1)
        black_pawn = ChessPiece(Color.BLACK, PieceType.PAWN)
        for col in range (len(self.chessboard_list)):
            self.add_piece(black_pawn, (1, col))


        # Add White Rooks (White is row 6 and 7)
        white_rook = ChessPiece(Color.WHITE, PieceType.ROOK)
        self.add_piece(white_rook, (7, 0))
        self.add_piece(white_rook, (7, 7))

        # Add White Knight (White is row 6 and 7)
        white_knight = ChessPiece(Color.WHITE, PieceType.KNIGHT)
        self.add_piece(white_knight, (7, 1))
        self.add_piece(white_knight, (7, 6))

        # Add White Bishops (White is row 6 and 7)
        white_bishop = ChessPiece(Color.WHITE, PieceType.BISHOP)
        self.add_piece(white_bishop, (7, 2))
        self.add_piece(white_bishop, (7, 5))

        # Add White Queen (White is row 6 and 7)
        white_queen = ChessPiece(Color.WHITE, PieceType.QUEEN)
        self.add_piece(white_queen, (7, 3))

        # Add White King (White is row 6 and 7)
        white_king = ChessPiece(Color.WHITE, PieceType.KING)
        self.add_piece(white_king, (7, 4))

        # Add White Pawns (White is row 6 and 7)
        white_pawn = ChessPiece(Color.WHITE, PieceType.PAWN)
        for col in range (len(self.chessboard_list)):
            self.add_piece(white_pawn, (6, col))


    def add_piece(self, chess_piece: ChessPiece, pos: tuple[int, int]):
        """adds a chess piece to specifed empty position
        
        returns True if the position was empty, returns False if it was already taken
        """
        (row, col) = pos
        if self.chessboard_list[row][col] is None:
            self.chessboard_list[row][col] = chess_piece
            return True
        return False


    def remove_piece(self, pos: tuple[int, int]):
        """adds a chess piece to specifed empty position
        
        returns True if the position was not empty, else returns False
        """
        (row, col) = pos
        if self.chessboard_list[row][col] is not None:
            self.chessboard_list[row][col] = None
            return True
        return False


    def is_valid(self, origin: tuple[int, int], dest: tuple[int, int]):
        (orgin_row, orgin_col) = origin
        chess_piece: PieceType = self.chessboard_list[orgin_row][orgin_col].get_type()
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

                            if self.chessboard_list[dest_row][dest_col] == None:
                                # Empty space, no attacker move to next...
                                offset_row += min(1, max(-1, offset_row)) # Next row (if offset is negativ we move 1 step up)
                                offset_col += min(1, max(-1, offset_col)) # Next col (if offset is negativ we move 1 step left)
                                
                                dest_row = origin_row + offset_row
                                dest_col = origin_col + offset_col
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
                        
                        
                        # End of while loop:
                        # propegation could not find a potential attacker. 
                        
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
    
    def is_diag_move_valid(self, origin:tuple[int,int], destination:tuple[int, int], options:list[MoveOption]) -> bool:
        """ Returns True if none of the below questions has answer yes, otherwise False

        \b No options: \n
        Move not diagonal? If yes -> False \n
        Obstacle between origin and/at destination? If yes -> False

        \b With options: \n
         
        Move not diagonal? If yes -> False \n
        MoveOption.FIRST - Has Piece been moved before, If yes -> False \n
        MoveOption.TAKE - Obstacle between origin and destination? Is destination same color? If yes -> False \n
        MoveOption.PROTECTED - Is Piece at risk of being taken if move is made? If yes -> False  """

        if not vmh.diagonal_move(origin,destination):
            return False

        disregard_dest_square = False

        if MoveOption.FIRST in options:
            try:
                if self.chessboard_list[origin[0]][origin[1]].get_has_moved() == True:
                    return False
            except:
                print("MoveOption.First error: Not a piece")

        if MoveOption.TAKE in options:
            try:
                if self.chessboard_list[destination[0]][destination[1]].get_color() == self.chessboard_list[origin[0]][origin[1]].get_color():
                    return False
                else:
                    disregard_dest_square = True
            except:
                print("MoveOption.TAKE error: Moving empty square, or moving piece to empty square")

        if MoveOption.PROTECTED in options:
            try:
                color = self.chessboard_list[origin[0]][origin[1]].get_color()
            except:
                print("MoveOption.Protected error: Not a piece")

            if self.in_danger(origin, color):
                return False

        if vmh.obstacle_in_path(self.chessboard_list, origin, destination, disregard_dest_square):
            return False
        
        return True
    
    def is_axis_move_valid(self, origin:tuple[int,int], destination:tuple[int, int], options:list[MoveOption]) -> bool:
        """ Returns True if no of the below questions has answer yes, otherwise False

        \b No options: \n
        Move not along single axis? If yes -> False \n
        Obstacle between origin and/at destination? If Yes -> False

        \b With options: \n 
         
        Move not along single axis? If yes -> False \n
        MoveOption.FIRST - Has Piece been moved before, If yes -> False \n
        MoveOption.TAKE - Obstacle between origin and destination? Is destination same color? If yes -> False \n
        MoveOption.PROTECTED - Is Piece at risk of being taken if move is made? If yes -> False  """

        disregard_dest_square = False

        if not vmh.axis_move(origin, destination):
            return False

        if MoveOption.FIRST in options:
            try:
                if self.chessboard_list[origin[0]][origin[1]].get_has_moved() == True:
                    return False
            except:
                print("MoveOption.First error: Not a piece")

        if MoveOption.TAKE in options:
            try:
                if self.chessboard_list[destination[0]][destination[1]].get_color() == self.chessboard_list[origin[0]][origin[1]].get_color():
                    return False
                else:
                    disregard_dest_square = True
            except:
                print("MoveOption.TAKE error: Moving empty square, or moving piece to empty square")

        if MoveOption.PROTECTED in options:
            try:
                color = self.chessboard_list[origin[0]][origin[1]].get_color()
            except:
                print("MoveOption.Protected error: Not a piece")

            if self.in_danger(origin, color):
                return False

        if vmh.obstacle_in_path(self.chessboard_list, origin, destination, disregard_dest_square):
            return False
        
        return True
    

    def __str__(self) -> str:
        out = ""
        for row in range(len(self.chessboard_list)):
            for col in range(len(self.chessboard_list)):
                out += f"[{str(self.chessboard_list[row][col])}],"
            out += "\n"
        return out