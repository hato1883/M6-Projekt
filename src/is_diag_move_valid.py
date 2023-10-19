from chess_piece import *
from chess_board_test import *
from text_user_interface import *
from move_option import *

# vector addition
def vector_addition(t1:tuple[int,int], t2:tuple[int,int]):
    min_len = min(len(t1), len(t2))
    temp = []
    
    for i in range(min_len):
        temp.append(t1[i] + t2[i])
    
    return tuple(temp)

#Vector subtraction and conversion of result to unit vector, sort of.
def return_step_vector(origin:tuple[int,int], destination:tuple[int, int]) -> tuple[int, int]:
  (row_origin, column_origin) = origin
  (row_dest, column_dest) = destination

  d_row = row_dest - row_origin
  d_column = column_dest - column_origin

  row_step = 0
  colum_step = 0

  if d_row > 0:
    row_step = 1
  elif d_row < 0:
    row_step = -1

  if d_column > 0:
    colum_step = 1
  elif d_column < 0:
    colum_step = -1

  step_vector = (row_step, colum_step)

  return step_vector

#Checks if move is diagonal
def diagonal_move(origin, destination):
  (row_origin, column_origin) = origin
  (row_dest, column_dest) = destination

  d_row = row_dest - row_origin
  d_column = column_dest - column_origin
    
  try:
    if abs(d_row / d_column)== 1:
      return True
    else:
      return False
  except ZeroDivisionError:
    return False
  
#Check if move is straight line
def vert_hori_move(origin, destination):
  (row_origin, column_origin) = origin
  (row_dest, column_dest) = destination

  d_row = row_dest - row_origin
  d_column = column_dest - column_origin

  if d_row != 0 and d_column == 0:
    return True
  elif d_row == 0 and d_column != 0:
    return True
  else:
    return False
  


def is_diag_move_valid(chess_board:list, origin:tuple[int,int], destination:tuple[int, int], move_options:list[MoveOption]) -> bool:
  
  step_vector = return_step_vector(origin, destination)

  print(f"Diagonal move: {diagonal_move(origin, destination)}")
  print(f"Vertical/Horizontal move: {vert_hori_move(origin,destination)}")
  print(f"| Origin: {origin} | Destination: {destination} | Step vector: {step_vector} |")
  print("****Checking****")

  next_square = vector_addition(origin, step_vector)
  after_end_square = vector_addition(destination, step_vector)

  if after_end_square == next_square: # rewarite, bad names
     if chess_board[next_square[0]][next_square[1]] != None:
        print(f"{next_square} is not empty")
        return False


  while after_end_square != next_square:
    
    if chess_board[next_square[0]][next_square[1]] == None:
       print(f"{next_square} is empty")
       next_square = vector_addition(next_square, step_vector)
       continue
    

    print(f"{next_square} is not empty")
    return False
    
  return True
    

#Testing
chess_board = create_board()

while True:
  TextUserInterface.show_chess_board(chess_board, debug=False)
  move = TextUserInterface.input_user_move()
  print()
  (origin, dest) = move
  valid_move = is_diag_move_valid(chess_board,origin,dest, [])
  print(valid_move)
  if valid_move:
    move_piece(chess_board, move)
  TextUserInterface.show_chess_board(chess_board, debug=True)
  input("Enter to continue")
  






