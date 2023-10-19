import pytest
import sys
import os
 
# getting the name of the directory
# where the this file is present.
#current = os.path.dirname(os.path.realpath(__file__))
current = os.path.dirname(__file__)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(current + "/../src")

from chessboard import *