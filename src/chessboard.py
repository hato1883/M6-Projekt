import copy
import chessboard_helper as ChessHelper
from piece_type_enum import PieceType
from chess_piece_class import ChessPiece
from chess_piece_class import EMPTY_PIECE
from piece_color_enum import Color
from move_type_enum import MoveType
from move_option_enum import MoveOption
from status_enum import Status
from position_class import Position
from move_class import Move
import valid_move_helper as vmh


class Chessboard:

    def __init__(self, chessboard: list[list[ChessPiece]] = []) -> None:
        # chessboard is a 2d list of ChessPiece objects
        self._chessboard: list[
            list[
                ChessPiece]
            ] = chessboard

        # Move history is a list of tuple of ChessPiece, origin and destination
        # Moves are in order (1st move is at index 0 2nd at next etc)
        self.move_history: list[
            tuple[
                ChessPiece,
                Position,
                Move]
            ] = []

        # A dictionary of all king PieceType on this instance of chessboard.
        # Key will be the king's current location,
        # and value will be a ref to the king (ChessPiece)
        self._kings_location: dict[Position: ChessPiece] = {}

        # size of chessboard
        self._board_size: int = len(self._chessboard)

        if self._board_size != 0:
            # Find kings in loaded list
            for row in range(self._board_size):
                for col in range(self._board_size):
                    pos = Position(row, col)
                    if self.get_piece(pos) is EMPTY_PIECE:
                        continue
                    if self.get_piece(pos).get_type() is PieceType.KING:
                        # add king chess piece to list
                        self._kings_location[pos] = self.get_piece(pos)

    def create_board(self, size: int = 8):
        """Creates a empty board with given size (default is 8)

        returns None (new chessboard is saved in object)
        """
        self._chessboard = []
        for row in range(size):
            col = [EMPTY_PIECE]*size
            self._chessboard.append(col)

        self._board_size: int = len(self._chessboard)

    def create_default_board(self):
        """Creates the default 8x8 chess board with 16 pieces in each color

        returns None (new chessboard is saved in object)
        """
        self.create_board()

        # Black Pieces
        self._chessboard: list[list[ChessPiece]] = [
            [ChessPiece(Color.BLACK, PieceType.ROOK), ChessPiece(Color.BLACK, PieceType.KNIGHT), ChessPiece(Color.BLACK, PieceType.BISHOP), ChessPiece(Color.BLACK, PieceType.QUEEN), ChessPiece(Color.BLACK, PieceType.KING), ChessPiece(Color.BLACK, PieceType.BISHOP), ChessPiece(Color.BLACK, PieceType.KNIGHT), ChessPiece(Color.BLACK, PieceType.ROOK)],  # noqa E501
            [ChessPiece(Color.BLACK, PieceType.PAWN), ChessPiece(Color.BLACK, PieceType.PAWN), ChessPiece(Color.BLACK, PieceType.PAWN), ChessPiece(Color.BLACK, PieceType.PAWN), ChessPiece(Color.BLACK, PieceType.PAWN), ChessPiece(Color.BLACK, PieceType.PAWN), ChessPiece(Color.BLACK, PieceType.PAWN), ChessPiece(Color.BLACK, PieceType.PAWN)],  # noqa E501
            [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
            [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
            [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
            [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],  # noqa E501
            [ChessPiece(Color.WHITE, PieceType.PAWN), ChessPiece(Color.WHITE, PieceType.PAWN), ChessPiece(Color.WHITE, PieceType.PAWN), ChessPiece(Color.WHITE, PieceType.PAWN), ChessPiece(Color.WHITE, PieceType.PAWN), ChessPiece(Color.WHITE, PieceType.PAWN), ChessPiece(Color.WHITE, PieceType.PAWN), ChessPiece(Color.WHITE, PieceType.PAWN)],  # noqa E501
            [ChessPiece(Color.WHITE, PieceType.ROOK), ChessPiece(Color.WHITE, PieceType.KNIGHT), ChessPiece(Color.WHITE, PieceType.BISHOP), ChessPiece(Color.WHITE, PieceType.QUEEN), ChessPiece(Color.WHITE, PieceType.KING), ChessPiece(Color.WHITE, PieceType.BISHOP), ChessPiece(Color.WHITE, PieceType.KNIGHT), ChessPiece(Color.WHITE, PieceType.ROOK)],  # noqa E501
        ]

        # Add kings to dictionary so we can check if they are in danger later.
        self._kings_location[Position(0, 4)] = ChessPiece(Color.BLACK, PieceType.KING)  # noqa E501
        self._kings_location[Position(7, 4)] = ChessPiece(Color.WHITE, PieceType.KING)  # noqa E501

    def get_piece(self, location: Position) -> ChessPiece:
        """Get a chess piece at location

        location the posistion to retrive

        Returns a ChessPiece or EMPTY_PIECE if it was empty"""
        return self._chessboard[location.row][location.col]

    def add_piece(self, chess_piece: ChessPiece, dest: Position):
        """adds a chess piece to specifed empty position

        returns True if the position was empty,
        returns False if it was already taken
        """
        if self.get_piece(dest) is EMPTY_PIECE:

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
        if self.get_piece(dest) is not EMPTY_PIECE:

            # if we are removing a king then remove it from king dict
            if self.get_piece(dest).get_type() is PieceType.KING:
                del self._kings_location[dest]

            self._chessboard[dest.row][dest.col] = EMPTY_PIECE
            return True
        return False

    def move(self,
             origin: Position,
             dest: Position) -> tuple[bool, Status]:

        # assume origin piece is current players piece
        player_color = self.get_piece(origin).get_color()

        # get list of valid moves
        valid_moves = self.get_valid_moves(player_color)

        if len(valid_moves) == 0:
            return (False, Status.IN_CHECKMATE, None)
        # Not checkmate.

        # Check if move is valid
        for (pos, move) in valid_moves:
            if (origin, dest) == (pos, Position(pos.row + move.capture.row * player_color.value.row,  # noqa: E501
                                                pos.col + move.capture.col * player_color.value.col)):  # noqa: E501
                break
        else:
            # Loop not broken
            # not valid due to check?
            if self.in_check(player_color):
                # Player in check
                return (False, Status.IN_CHECK, None)
            else:
                # Move simply is invalid
                return (False, Status.INVALID_MOVE, None)
        # Loop broken
        # Move is valid

        # Get chess piece at origin
        moved_piece = self.get_piece(origin)
        attacked_piece = self.get_piece(dest)

        # Add move to move_history (at end of list)
        self.move_history.append((moved_piece, origin, move))

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
                        return (
                                True,
                                Status.PAWN_PROMOTION,
                                (moved_piece, attacked_piece)
                            )

                case Color.BLACK:
                    # Piece is moving towards max size
                    if dest.row == self._board_size-1:
                        return (
                                True,
                                Status.PAWN_PROMOTION,
                                (moved_piece, attacked_piece)
                            )
            # End of Pawn Promotion check
            if MoveType.PAWN_EN_PASSANT is move.type:
                # get killed pawn location
                pawn_location = Position(origin.row, dest.col)
                # remove killed enemy pawn
                self.remove_piece(pawn_location)

        # Check if we was castling on this move
        if (moved_piece.get_type() is PieceType.KING
                and MoveType.KING_CASTLE is move.type):
            # Move rook the rook to the oposite side of the king.

            # find rook in direction of king.
            if origin.col > dest.col:
                # origin is to the right of dest so rook is towards the left
                for searched_col in range(origin.col-3, -1, -1):
                    searched_pos = Position(origin.row, searched_col)
                    if self.get_piece(searched_pos) is EMPTY_PIECE:
                        continue
                    # assume piece is rook due to move being valid
                    rook_loaction = Position(dest.row, searched_col)

            else:
                # origin is to the right of dest so rook is towards the left
                for searched_col in range(origin.col+3, self._board_size, 1):
                    searched_pos = Position(origin.row, searched_col)
                    if self.get_piece(searched_pos) is EMPTY_PIECE:
                        continue
                    # assume piece is rook due to move being valid
                    rook_loaction = Position(dest.row, searched_col)

            # rook lands between origin and dest
            rook_landing = Position(origin.row, int((origin.col + dest.col)/2))

            # save rook piece
            rook_piece = self.get_piece(rook_loaction)
            # rook piece has now moved
            rook_piece.set_has_moved_true()
            # add it to new dest
            self.add_piece(rook_piece, rook_landing)
            # remove it from the old
            self.remove_piece(rook_loaction)

        # is destination Empty?
        if self.get_piece(dest) is not EMPTY_PIECE:
            # Clear destination
            self.remove_piece(dest)

        # Add piece to destination
        self.add_piece(moved_piece, dest)

        # Remove it from origin
        self.remove_piece(origin)

        # Succsesful move
        return (True, Status.SUCCESS, (moved_piece, attacked_piece))

    def is_valid(self,
                 origin: Position,
                 dest: Position,
                 dest_color: Color = None
                 ) -> tuple[bool, Move]:

        # is origin out of bounds
        if not ChessHelper.in_bounds(origin, Position(0, 0),
                                     max=self._board_size):
            # Invalid move, Can't move from a pos that is out of bounds.
            return (False, None)

        # is destnation out of bounds
        if not ChessHelper.in_bounds(dest, Position(0, 0),
                                     max=self._board_size):
            # Invalid move, Can't move to a dest that is out of bounds.
            return (False, None)

        # is destnation empty
        if self.get_piece(origin) is EMPTY_PIECE:
            # Invalid move, Can't move empty tile.
            return (False, None)

        chess_piece: PieceType = self.get_piece(origin).get_type()

        # get Calculated offset between dest and origin
        calc_offset = Position(
            dest.row - origin.row,
            dest.col - origin.col)
        norm_offset = Position(ChessHelper.clamp(calc_offset.row, -1, 1),
                               ChessHelper.clamp(calc_offset.col, -1, 1))

        reflec_tup = self.get_piece(origin).get_color().value

        # create a list with offsets equal to calculated or normalized offset
        potential_valid_moves = []
        for moveset in chess_piece.value:
            reflec_offset = Position(moveset.dest.row * reflec_tup.row,
                                     moveset.dest.col * reflec_tup.col)

            # Check if calculated offset exists in list
            if reflec_offset == calc_offset:
                # add move to potential valid moves
                potential_valid_moves.append(moveset)  # noqa E501

            # Check if normalized offset exists in list
            elif reflec_offset == norm_offset:
                # add move to potential valid moves
                potential_valid_moves.append(moveset)

        # loop thru ddetermined potential moves
        for moveset in potential_valid_moves:
            # reflect the offset using our tuple.
            reflec_offset = Position(moveset.dest.row * reflec_tup.row,
                                     moveset.dest.col * reflec_tup.col)

            # Go thru each move for the given offset
            for move in moveset.moves:

                if reflec_offset != calc_offset:
                    # offset is equal to normalized offset

                    # check if move can propegate
                    if MoveOption.PROPEGATES not in move.conditions:
                        continue

                # check against MoveType rules
                match move.type:
                    case MoveType.COLLISION_AXIS:
                        if self.__is_axis_move_valid(origin,
                                                     dest,
                                                     move.conditions,
                                                     dest_color):
                            return (True, move)
                        continue

                    case MoveType.COLLISION_DIAG:
                        if self.__is_diag_move_valid(origin,
                                                     dest,
                                                     move.conditions,
                                                     dest_color):
                            return (True, move)
                        continue

                    case MoveType.ABSOLUTE:
                        if self.__is_abs_move_valid(origin,
                                                    dest,
                                                    move.conditions,
                                                    dest_color):
                            return (True, move)
                        continue

                    case MoveType.KING_CASTLE:
                        if self.__is_king_castling_valid(origin,
                                                         dest):
                            return (True, move)
                        continue

                    case MoveType.PAWN_EN_PASSANT:
                        if self.__is_pawn_en_passant_valid(origin,
                                                           dest):
                            return (True, move)
                        continue
                # End of match case

            # End of Move evaluation, check next

        # All moves have been check, none did a early exit with return
        # Move must be invalid
        return (False, None)

    def in_danger(self, origin: Position, piece_color: Color = None) -> bool:
        """Checks if a enemy piece can land on the specifed origin

        This would mean that if you provide a empty origin
        that normal pawn moves can threaten it"""

        if piece_color is None and self.get_piece(origin) is EMPTY_PIECE:
            raise ValueError("Can't check if a empty square is in danger if no Color is given")  # noqa E501

        elif piece_color is None:
            piece_color = self.get_piece(origin).get_color()

        if piece_color is Color.WHITE:
            positions = self.get_pieces(Color.BLACK)
        else:
            positions = self.get_pieces(Color.WHITE)

        for pos in positions:
            (valid, move) = self.is_valid(pos, origin, piece_color)

            if valid:
                # Enemy has a valid move to given origin
                # The origin is in danger
                return True

            elif self.get_piece(pos).get_type() is PieceType.PAWN:
                # check position behind dest
                # and check if valid used move is en passant

                # row that en passant move would move to
                passant_row = origin.row + piece_color.value.row

                # position that the pawn would be arriving at
                en_passant_pos = Position(passant_row, origin.col)

                (valid, move) = self.is_valid(pos,
                                              en_passant_pos,
                                              piece_color)

                if valid and move.type is MoveType.PAWN_EN_PASSANT:
                    return True
        return False

    def in_check(self, king_color: Color) -> bool:
        """Checks if the given color's king is in danger

        uses in danger method on kings location"""
        # Assume no king on board
        king_location: Position = None

        # declare types
        pos: Position
        piece: ChessPiece
        # get kings location from the dictionary
        for pos, piece in self._kings_location.items():
            # check it's color
            if piece.get_color() is king_color:
                # save location
                king_location = pos
                # break loop (assumes only 1 king per color)
                break

        # if king_location is still empty,
        # that would mean player dose not have a king
        if king_location is None:
            # no king can be in danger, so not in check
            return False

        # returns if the king is in danger
        return self.in_danger(king_location, king_color)

    def get_valid_moves(self, player_color: Color) -> list[tuple[Position, Move]]:  # noqa E501
        """returns a list of valid moves

        uses in check method so we can disgared moves that put king in check"""
        # list of valid moves
        valid_moves: list[tuple[Position, Move]] = []

        piece_list: list[Position] = self.get_pieces(player_color)

        # loop thru all pieces and check thier moves
        pos: Position
        for pos in piece_list:
            piece_type: PieceType = self.get_piece(pos).get_type()

            # check all moves in the pieces moveset
            for moveset in piece_type.value:

                # Get destination of move
                dest = Position(pos.row + moveset.dest.row * player_color.value.row, pos.col + moveset.dest.col * player_color.value.col)  # noqa E501

                # check if move is valid:
                (valid, move) = self.is_valid(pos, dest)
                if not valid:
                    # Invalid move continue to the next
                    continue

                # Move is valid but might put player in check, lets test.
                simulated = self.deep_copy()
                # we know move is valid acording to move rules
                # set resulting board instead checking move rules again
                simulated.remove_piece(dest)
                simulated.add_piece(simulated.get_piece(pos), dest)
                simulated.get_piece(dest).set_has_moved_true()
                simulated.remove_piece(pos)

                # check if king is being attacked after the move
                if simulated.in_check(player_color):
                    # move puts king in check so its invalid.
                    continue

                # move did not put king in check so it's valid
                valid_moves.append((pos, move))

        # returns all moves that did not result in the king
        # being in danger
        return valid_moves

    def get_pieces(self, piece_color: Color) -> list[Position]:
        """Returns a list of all pieces of the given color

        Usefull when you need to itterate thru a players pieces"""
        piece_list: list[Position] = []

        # declare types
        row: int
        col: int
        # get piece loactions
        for row in range(self._board_size):
            for col in range(self._board_size):
                pos = Position(row, col)

                if self.get_piece(pos).get_color() is not piece_color:
                    # Ignore piece from other players
                    continue

                # piece of give color found
                piece_list.append(pos)
        return piece_list

    def get_chessboard(self) -> list[list[ChessPiece]]:
        """Returns a 2d list of ChessPiece enums
        which represents the chessboard"""
        return self._chessboard

    def get_move_history(self) -> list[
        tuple[
            ChessPiece,
            Position,
            Move]]:
        """Retrives the move history list

        Returns a list of tuples that contains all information needed.
        where ChessPiece stores information of PieceType and PieceColor
        1st tuple stores the valid move used and its options,
        1st Position obj is the move origin and
        2nd Position obj is move destination"""
        return self.move_history

    def reset_move_history(self) -> None:
        """Clears the instance move history

        Useful if reseting chessboard instance"""
        self._move_history.clear

    def __is_abs_move_valid(self,
                            origin: Position,
                            destination: Position,
                            options: list[MoveOption],
                            destination_color: Color) -> bool:
        """Checks if the move is valid
        Validation depends on given option input

        With options: \n
        MoveOption.FIRST - Has Piece been moved before, If yes -> False \n
        MoveOption.PROTECTED - Is Piece at risk of being taken if move is made?
        If yes -> False"""

        if self.get_piece(origin) is EMPTY_PIECE:
            raise ValueError("Origin is empty")

        if MoveOption.FIRST in options:
            if self.get_piece(origin).get_has_moved() is True:
                return False

        if MoveOption.MUST_TAKE in options:

            if self.get_piece(destination) is EMPTY_PIECE:
                # Destination must have enemy piece
                return False

            if destination_color is None:
                # Set destination color if not already set
                destination_color = self.get_piece(destination).get_color()

            if destination_color == self.get_piece(origin).get_color():
                # Can not take allied piece
                return False

        if MoveOption.CAN_TAKE in options:
            if self.get_piece(destination) is not EMPTY_PIECE:

                if destination_color is EMPTY_PIECE:
                    # Set destination color if not already set
                    destination_color = self.get_piece(destination).get_color()

                if destination_color == self.get_piece(origin).get_color():
                    return False

        if MoveOption.PROTECTED in options:
            color = self.get_piece(origin).get_color()

            if self.in_danger(destination, color):
                return False

        return True

    def __is_diag_move_valid(self,
                             origin: Position,
                             destination: Position,
                             options: list[MoveOption],
                             destination_color: Color) -> bool:
        """Checks if the move is valid
        Validation depends on given option input

        No options:\n
        Move not diagonal? If yes -> False \n
        Obstacle between origin and/at destination? If yes -> False

        With options:\n
        Move not diagonal? If yes -> False \n
        MoveOption.FIRST - Has Piece been moved before, If yes -> False \n
        MoveOption.CAN_TAKE - Obstacle between origin and destination?
        Is destination same color? If yes -> False \n
        MoveOption.MUST_TAKE - Obstacle between origin and destination?
        is destination empty? If yes -> False \n
        MoveOption.PROTECTED - Is Piece at risk of being taken if move is made?
        If yes -> False  """

        if self.get_piece(origin) is EMPTY_PIECE:
            raise ValueError("Origin is empty")

        if not vmh.diagonal_move(origin, destination):
            return False

        disregard_dest_square = False

        if MoveOption.FIRST in options:
            if self.get_piece(origin).get_has_moved() is True:
                return False

        if MoveOption.MUST_TAKE in options:
            disregard_dest_square = True

            if self.get_piece(destination) is EMPTY_PIECE:
                # Destination must have enemy piece
                return False

            if destination_color is None:
                # Set destination color if not already set
                destination_color = self.get_piece(destination).get_color()

            if destination_color == self.get_piece(origin).get_color():
                # Can not take allied piece
                return False

        if MoveOption.CAN_TAKE in options:
            disregard_dest_square = True
            if self.get_piece(destination) is not EMPTY_PIECE:

                if destination_color is None:
                    # Set destination color if not already set
                    destination_color = self.get_piece(destination).get_color()

                if destination_color == self.get_piece(origin).get_color():
                    return False

        if MoveOption.PROTECTED in options:
            color = self.get_piece(origin).get_color()

            if self.in_danger(destination, color):
                return False

        if vmh.obstacle_in_path(self._chessboard,
                                origin, destination,
                                disregard_dest_square):
            return False

        return True

    def __is_axis_move_valid(self,
                             origin: Position,
                             destination: Position,
                             options: list[MoveOption],
                             destination_color: Color) -> bool:
        """Returns True if no of the below questions has answer yes,
        otherwise False

        \b No options: \n
        Move not along single axis? If yes -> False \n
        Obstacle between origin and/at destination? If Yes -> False

        \b With options: \n

        Move not along single axis? If yes -> False \n
        MoveOption.FIRST - Has Piece been moved before, If yes -> False \n
        MoveOption.CAN_TAKE - Obstacle between origin and destination?
        Is destination same color? If yes -> False \n
        MoveOption.PROTECTED - Is Piece at risk of being taken if move is made?
        If yes -> False"""

        if self.get_piece(origin) is EMPTY_PIECE:
            raise ValueError("Origin is empty")

        disregard_dest_square = False

        if not vmh.axis_move(origin, destination):
            return False

        if MoveOption.FIRST in options:
            if self.get_piece(origin).get_has_moved() is True:
                return False

        if MoveOption.MUST_TAKE in options:
            disregard_dest_square = True

            if self.get_piece(destination) is EMPTY_PIECE:
                # Destination must have enemy piece
                return False

            if destination_color is None:
                # Set destination color if not already set
                destination_color = self.get_piece(destination).get_color()

            if destination_color == self.get_piece(origin).get_color():
                # Can not take allied piece
                return False

        if MoveOption.CAN_TAKE in options:
            disregard_dest_square = True
            if self.get_piece(destination) is not EMPTY_PIECE:

                if destination_color is None:
                    # Set destination color due to it not being set
                    destination_color = self.get_piece(destination).get_color()

                if destination_color == self.get_piece(origin).get_color():
                    return False

        if MoveOption.PROTECTED in options:
            color = self.get_piece(origin).get_color()

            if self.in_danger(destination, color):
                return False

        if vmh.obstacle_in_path(self._chessboard,
                                origin,
                                destination,
                                disregard_dest_square):
            print("obstacle")
            return False

        return True

    def __is_king_castling_valid(self,
                                 origin: Position,
                                 dest: Position) -> bool:
        """Private Helper Method:
        Checks if a king castling type move is valid to destination.

        Returns True if all of the requierments are met otherwise returns False

        Requierments for valid move are:
          1. origin piece (normaly the king) has NOT moved before
          2. origin piece can not be under threat
          3. space between origin piece and rook must be empty
          4. can only castle with PieceType.ROOK
          5. rook piece has NOT moved before
          6. distance between rook and origin must be atleast 2 tiles
          (2 empty spots between them)
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

        # Check if destination is left or right of king
        if origin.col > dest.col:
            # origin is to the right of dest so rook is towards the left
            for searched_col in range(origin.col-1, -1, -1):
                searched_pos = Position(origin.row, searched_col)

                # Check if spot is empty (req 3)
                if self.get_piece(searched_pos) is EMPTY_PIECE:

                    # Check if the 2 spaces left of king is not under threat
                    # (req 7 & 8)
                    if abs(origin.col - searched_col) <= 2:
                        if self.in_danger(searched_pos,
                                          self.get_piece(origin).get_color()):
                            # cant castle under threat
                            break

                    # Empty continue to next col
                    continue

                # col contains a chess piece
                # Is it a rook? (req 4)
                if self.get_piece(searched_pos).get_type() is not PieceType.ROOK:  # noqa E501
                    # Not a rook exit loop
                    break

                # Piece is a Rook
                # Has the rook moved? (req 5)
                if self.get_piece(searched_pos).get_has_moved():

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
                searched_pos = Position(origin.row, searched_col)

                # Check if spot is empty (req 3)
                if self.get_piece(searched_pos) is EMPTY_PIECE:

                    # Check if the 2 spaces left of king is not under threat
                    # (req 7 & 8)
                    if abs(origin.col - searched_col) <= 2:
                        if self.in_danger(searched_pos,
                                          self.get_piece(origin).get_color()):
                            # Can't castle undre threat
                            break

                    # Empty continue to next col
                    continue

                # col contains a chess piece
                # Is it a rook? (req 4)
                if self.get_piece(searched_pos).get_type() is not PieceType.ROOK:  # noqa E501
                    # Not a rook exit loop
                    break

                # Piece is a Rook
                # Has the rook moved? (req 5)
                if self.get_piece(searched_pos).get_has_moved():

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

    def __is_pawn_en_passant_valid(self,
                                   origin: Position,
                                   dest: Position) -> bool:
        """Private Helper method: Checks if Pawn En Passant MoveType is valid

        Returns True if all of the requierments are met otherwise returns False

        Requierments for valid move are:
          1. Origin must be a PieceType.PAWN
          2. Destination must be empty
          3. The tile (origin_row, dest_col) must contain enemy pawn
          (enemy pawn adjecent to origin)
          4. Enemy pawn must have moved using a move with the MoveOption.FIRST
        """

        # check if origin is a Pawn (req 1)
        if self.get_piece(origin).get_type() is not PieceType.PAWN:
            # None pawn pieces are not allowed to preform this move
            return False

        # Piece is a PAWN
        # Check if dest is empty (req 2)
        if self.get_piece(dest) is not EMPTY_PIECE:
            # destination is occupied, en passant is not valid
            return False
        # destination is empty

        adjecent_pos = Position(origin.row, dest.col)

        # origin_row, dest_col must contain a pawn (req 3)
        if self.get_piece(adjecent_pos).get_type() is not PieceType.PAWN:
            # Not a pawn, Not valid
            return False

        if self.get_piece(adjecent_pos).get_color() is self.get_piece(origin).get_color():  # noqa E501
            # Allied pawn, Not valid
            return False

        # Enemy pawn is adjecent to origin and destination is empty.
        # Check move_history to see if enemy pawn moved adjecent last move
        # keep checking the latest move until we get one of the piece color
        # (req 4)

        move_index = len(self.get_move_history()) - 1  # last index
        (moved_piece,
         move_orig,
         move) = self.get_move_history()[move_index]
        enemy_color = self.get_piece(adjecent_pos).get_color()
        while moved_piece.get_color() is not enemy_color:
            # Move is not from the same player as what we are checking

            # next move
            move_index -= 1

            # check so we are not indexing outside list
            if move_index < 0:
                # move_index cant be less than 0
                # that would mean that the searched color
                # has not made a move yet.
                break

            # index is in range, get next move
            (moved_piece,
             move_orig,
             move) = self.get_move_history()[move_index]
        else:
            move_dest = Position(move_orig.row + move.capture.row * enemy_color.value.row,  # noqa E501
                                 move_orig.col + move.capture.col * enemy_color.value.col)  # noqa E501
            # Found move from enemy pawn color
            # Check if found move is to the pawn destination
            if move_dest != Position(origin.row, dest.col):
                # was not the move that moved the pawn
                # pawn was moved more than 1 turn ago so En passant is invalid
                return False

            # Enemy pawn was moved to location last move
            # check if it was a double forward move or another type.
            if MoveOption.FIRST not in move.conditions:
                # move was not a double forward move
                # double forward move has MoveOption.FIRST flag
                return False

            # Move is valid
            return True

        # loop was broken, in other words enemy player has not made a move yet
        # En Passant can't be valid.
        return False

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

            return True
        else:
            return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def copy(self):
        """Returns a shallow copy of the class

        (original is original.copy()) is False and
        (original == original.copy()) is True. But
        (original.get_chessboard() is original.copy().get_chessboard()) is True"""  # noqa E501
        return copy.copy(self)

    def deep_copy(self, memo: dict = {}):
        """Returns a deep copy of the class

        (original is original.copy()) is False and
        (original == original.copy()) is True. But
        (original.get_chessboard() is original.copy().get_chessboard()) is False but we still get
        (original.get_chessboard() == original.copy().get_chessboard()) is True

        This means that chessboard layout is the same
        but modifications can be made withot affecting the original"""  # noqa E501
        return copy.deepcopy(self, memo)
