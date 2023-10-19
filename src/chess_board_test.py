from chess_piece import *

def create_board():   
  bp = [1] * 8
  bp[0]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.ROOK)
  bp[1]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KNIGHT)
  bp[2]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.BISHOP)
  bp[3]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.QUEEN)
  bp[4]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KING)
  bp[5]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.BISHOP)
  bp[6]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.KNIGHT)
  bp[7]= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.ROOK)

  wp = [1] * 8
  wp[0]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.ROOK)
  wp[1]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KNIGHT)
  wp[2]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.BISHOP)
  wp[3]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KING)
  wp[4]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.QUEEN)
  wp[5]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.BISHOP)
  wp[6]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.KNIGHT)
  wp[7]= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.ROOK)
        

  empty_board = [[None] * 8 for _ in range(8)]

  for i in range(8):
      temp= ChessPiece(piece_color= Color.BLACK, piece_type= PieceType.PAWN)
      empty_board[1][i] = temp

  for i in range(8):
      empty_board[0][i] = bp[i]

  for i in range(8):
      temp= ChessPiece(piece_color= Color.WHITE, piece_type= PieceType.PAWN)
      empty_board[6][i] = temp


  for i in range(8):
      empty_board[7][i] = wp[i]

  return empty_board

def move_piece(chess_board, move):
    (origin, dest) = move
    (row_origin, column_origin) = origin
    # print(origin) 
    (row_dest, column_dest) = dest
    # print(dest)

    chess_board[row_dest][column_dest] = chess_board[row_origin][column_origin]
    chess_board[row_origin][column_origin] = None