from chess_piece import *
from move_option import *

def add_coordinate_pairs(t1:tuple[int,int], t2:tuple[int,int]):
    temp = []
    
    for i in range(2):
        temp.append(t1[i] + t2[i])

    return tuple(temp)


def return_direction_vector(origin:tuple[int,int], destination:tuple[int, int]) -> tuple[int, int]:
  """Compares destination with origin, returns unit vector pointing from origin to destination"""
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
    
  return (row_step, colum_step)

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
def axis_move(origin, destination):
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
  
def obstacle_in_path(chessboard:list, origin:tuple[int,int], destination:tuple[int, int], disregard_dest:bool, debug = False):

  step_vector = return_direction_vector(origin, destination)
  next_square = add_coordinate_pairs(origin, step_vector)

  if disregard_dest:
    do_not_check_square = destination
  else:
    do_not_check_square = add_coordinate_pairs(destination, step_vector)

  if debug:
    print(f"Diagonal move: {diagonal_move(origin, destination)}")
    print(f"Vertical/Horizontal move: {vert_hori_move(origin,destination)}")
    print(f"| Origin: {origin} | Destination: {destination} | Step vector: {step_vector} |")
    print("****Checking****")

  if next_square == do_not_check_square:
      print(f"Origin == destination, invalid move!")
      return True

  while next_square != do_not_check_square:
    
    if chessboard[next_square[0]][next_square[1]] == None:
       
       if debug:
         print(f"{next_square} is empty")

       next_square = add_coordinate_pairs(next_square, step_vector)
       continue
    
    if debug:
      print(f"{next_square} is not empty")
    return True
    
  return False