from piece_type import PieceType
from piece_color import Color
from chess_piece import ChessPiece

class Chessboard:

    def __init__(self) -> None:
        chessboard_list = []


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
    
    def __str__(self) -> str:
        out = ""
        for row in range(len(self.chessboard_list)):
            for col in range(len(self.chessboard_list)):
                out += f"[{str(self.chessboard_list[row][col])}],"
            out += "\n"
        return out

if __name__ == "__main__":
    ref = Chessboard()
    ref.create_default_board()
    print(str(ref))