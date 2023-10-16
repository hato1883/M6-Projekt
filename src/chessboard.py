class chessboard:

    def __init__(self) -> None:
        chessboard_list = []


    def create_board(self, size=8):
        """Creates a empty board with given size (default is 8)
        
        returns None (new chessboard is saved in object)
        """
        self.chessboard_list = []
        for row in range(size):
            col = [ [None]*size ] 
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
