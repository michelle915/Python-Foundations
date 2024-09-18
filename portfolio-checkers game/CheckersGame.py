# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 3/8/2023
# Description: This program contains a class called Checkers that allows two people
# to play the game of checkers.


class OutOfTurn(Exception):
    """Exception for invalid turn"""
    pass


class InvalidSquare(Exception):
    """Exception for move requested on invalid square"""
    pass


class InvalidPlayer(Exception):
    """Exception for invalid player name"""
    pass


class Player:
    """Represents a checker player in a checker game."""

    def __init__(self, player_name, checker_color):
        """Initializes Player object with a player_name and checker_color"""

        self._name = player_name
        self._color = checker_color
        self._king_count = 0
        self._triple_king_count = 0
        self._captured_pieces = 0

    def get_name(self):
        """
        Returns the player's name
        """
        return self._name

    def get_color(self):
        """
        Returns the player's color
        """
        return self._color

    def get_king_count(self):
        """
        Returns the number of king pieces that the player has
        """
        return self._king_count

    def get_triple_king_count(self):
        """
        Returns the number of triple king pieces that the player has
        """
        return self._triple_king_count

    def get_captured_pieces_count(self):
        """
        Returns the number of opponent pieces that the player has captured
        """
        return self._captured_pieces

    def increase_king_count(self):
        """
        Increases king piece count
        """
        self._king_count += 1

    def increase_triple_king_count(self):
        """
        Increases triple king piece count
        """
        self._triple_king_count += 1

    def increase_captured_pieces(self, type_captured):
        """
        Increases captured pieces tally bases on type of captured piece.
        """
        if len(type_captured) == 5:
            self._captured_pieces += 1
        elif len(type_captured) == 10:
            self._captured_pieces += 2
        elif len(type_captured) == 17:
            self._captured_pieces += 3


class Checkers:
    """
    Represents a checker's game. Contains information about the board
    and the players. Will communicate with all previous classes to get
    information about players and pieces and to control exceptions.
    """

    def __init__(self):
        """Initializes checkerboard"""

        self._board = [
            [None, "White", None, "White", None, "White", None, "White"],
            ["White", None, "White", None, "White", None, "White", None],
            [None, "White", None, "White", None, "White", None, "White"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["Black", None, "Black", None, "Black", None, "Black", None],
            [None, "Black", None, "Black", None, "Black", None, "Black"],
            ["Black", None, "Black", None, "Black", None, "Black", None],
        ]
        self._players = []
        self._player_turn = "White"
        self._winner = None

    def create_player(self, player_name, piece_color):
        """
        Takes as parameter the player_name and piece_color (string of value
        "Black" or "White" representing Black or White checkers pieces) that the player
        wants to play with and creates the player object. This function returns the player
        object that has been created.
        """

        player = Player(player_name, piece_color)
        self._players.append(player)

        return player

    def lookup_player_from_name(self, name):
        """
        Takes a name as parameter and searches players data member. Returns Player object
        """

        person = None

        for player in self._players:
            if player.get_name() == name:
                person = player

        return person

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """
        Takes as parameter the player_name and two square_locations (starting and
        destination) in the tuple format (row, column). The method will assess if
        the requested move is valid (according to the player name, the player turn,
        the current location of pieces, the size of the board, and the type of piece)
        and will perform the move if so and will return the number of opponent
        pieces captured, if any. The method will additionally promote pieces as they
        reach certain locations.
        """

        captures = 0

        starting_row = starting_square_location[0]
        starting_column = starting_square_location[1]

        destination_row = destination_square_location[0]
        destination_column = destination_square_location[1]

        # validate that starting and destination squares are within board:
        if starting_row < 0 or starting_row > 7 or starting_column < 0 or starting_column > 7 \
           or destination_row < 0 or destination_row > 7 or destination_column < 0 or destination_column > 7:
            raise InvalidSquare

        player = self.lookup_player_from_name(player_name)
        starting_square_details = self.get_checker_details(starting_square_location)
        destination_square_details = self.get_checker_details(destination_square_location)

        if player is None:  # validate player name
            raise InvalidPlayer
        elif player.get_color() is not self._player_turn:  # validate player turn
            raise OutOfTurn
        elif starting_square_details is None:  # validate that there is piece on starting sq
            raise InvalidSquare

        if player.get_color() == "White":  # validate that piece belongs to white
            if starting_square_details == "Black":
                raise InvalidSquare
            if starting_square_details == "Black_King":
                raise InvalidSquare
            if starting_square_details == "Black_Triple_King":
                raise InvalidSquare
        elif player.get_color() == "Black":  # validate that piece belongs to black
            if starting_square_details == "White":
                raise InvalidSquare
            if starting_square_details == "White_King":
                raise InvalidSquare
            if starting_square_details == "White_Triple_King":
                raise InvalidSquare

        # coordinates of squares around starting square:
        sw = ((starting_row + 1), (starting_column - 1))
        se = ((starting_row + 1), (starting_column + 1))
        nw = ((starting_row - 1), (starting_column - 1))
        ne = ((starting_row - 1), (starting_column + 1))

        sw2 = ((starting_row + 2), (starting_column - 2))
        se2 = ((starting_row + 2), (starting_column + 2))
        nw2 = ((starting_row - 2), (starting_column - 2))
        ne2 = ((starting_row - 2), (starting_column + 2))

        sw3 = ((starting_row + 3), (starting_column - 3))
        se3 = ((starting_row + 3), (starting_column + 3))
        nw3 = ((starting_row - 3), (starting_column - 3))
        ne3 = ((starting_row - 3), (starting_column + 3))

        sw4 = ((starting_row + 4), (starting_column - 4))
        se4 = ((starting_row + 4), (starting_column + 4))
        nw4 = ((starting_row - 4), (starting_column - 4))
        ne4 = ((starting_row - 4), (starting_column + 4))

        sw5 = ((starting_row + 5), (starting_column - 5))
        se5 = ((starting_row + 5), (starting_column + 5))
        nw5 = ((starting_row - 5), (starting_column - 5))
        ne5 = ((starting_row - 5), (starting_column + 5))

        sw6 = ((starting_row + 6), (starting_column - 6))
        se6 = ((starting_row + 6), (starting_column + 6))
        nw6 = ((starting_row - 6), (starting_column - 6))
        ne6 = ((starting_row - 6), (starting_column + 6))

        # WHITE:

        if starting_square_details == "White":
            # S No capture:
            if destination_row - starting_row == 1 and abs(destination_column - starting_column) == 1 \
                    and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White"  # move piece to destination
                captures += 0                                                    # return number of captured pieces
            # SW capture:
            elif destination_row - starting_row == 2 and destination_column - starting_column == -2 \
                    and (self.get_checker_details(sw) == "Black" or self.get_checker_details(sw) == "Black_King"
                         or self.get_checker_details(sw) == "Black_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw))                           # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None   # remove captured piece
                captures += 1                                                    # return number of captured pieces
            # SE capture:
            elif destination_row - starting_row == 2 and destination_column - starting_column == 2 \
                    and (self.get_checker_details(se) == "Black" or self.get_checker_details(se) == "Black_King"
                         or self.get_checker_details(se) == "Black_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se))                           # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column + 1] = None   # remove captured piece
                captures += 1                                                    # return number of captured pieces
            # Requested destination is invalid for piece
            else:
                raise InvalidSquare

        # BLACK:

        elif starting_square_details == "Black":
            # N no capture
            if destination_row - starting_row == -1 and abs(destination_column - starting_column) == 1 \
                    and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black"  # move piece to destination
                captures += 0  # return number of captured pieces
            # NW capture
            elif destination_row - starting_row == -2 and destination_column - starting_column == -2 \
                    and (self.get_checker_details(nw) == "White" or self.get_checker_details(nw) == "White_King"
                         or self.get_checker_details(nw) == "White_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw))  # add captured piece to player's capture tally
                self._board[starting_row - 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE capture
            elif destination_row - starting_row == -2 and destination_column - starting_column == 2 \
                    and (self.get_checker_details(ne) == "White" or self.get_checker_details(ne) == "White_King"
                         or self.get_checker_details(ne) == "White_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne))  # add captured piece to player's capture tally
                self._board[starting_row - 1][starting_column + 1] = None  # remove captured piece
                captures += 1
            # Requested destination is invalid for piece
            else:
                raise InvalidSquare

        # WHITE KING:

        elif starting_square_details == "White_King":
            # S No capture:
            if destination_row - starting_row == 1 and abs(destination_column - starting_column) == 1 \
                    and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                captures += 0  # return number of captured pieces
            # N No capture:
            elif destination_row - starting_row == -1 and abs(destination_column - starting_column) == 1 \
                    and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                captures += 0  # return number of captured pieces

            # SW Capture:
            elif destination_row - starting_row == 2 and destination_column - starting_column == -2 \
                    and (self.get_checker_details(sw) == "Black" or self.get_checker_details(sw) == "Black_King"
                         or self.get_checker_details(sw) == "Black_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and (self.get_checker_details(sw2) == "Black" or self.get_checker_details(sw2) == "Black_King"
                         or self.get_checker_details(sw2) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and (self.get_checker_details(sw3) == "Black" or self.get_checker_details(sw3) == "Black_King"
                         or self.get_checker_details(sw3) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and self.get_checker_details(sw3) is None \
                    and (self.get_checker_details(sw4) == "Black" or self.get_checker_details(sw4) == "Black_King"
                         or self.get_checker_details(sw4) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and self.get_checker_details(sw3) is None \
                    and self.get_checker_details(sw4) is None \
                    and (self.get_checker_details(sw5) == "Black" or self.get_checker_details(sw5) == "Black_King"
                         or self.get_checker_details(sw5) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and self.get_checker_details(sw3) is None \
                    and self.get_checker_details(sw4) is None \
                    and self.get_checker_details(sw5) is None \
                    and (self.get_checker_details(sw6) == "Black" or self.get_checker_details(sw6) == "Black_King"
                         or self.get_checker_details(sw6) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces

            # SE Capture:
            elif destination_row - starting_row == 2 and destination_column - starting_column == 2 \
                    and (self.get_checker_details(se) == "Black" or self.get_checker_details(se) == "Black_King"
                         or self.get_checker_details(se) == "Black_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column + 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and (self.get_checker_details(se2) == "Black" or self.get_checker_details(se2) == "Black_King"
                         or self.get_checker_details(se2) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and (self.get_checker_details(se3) == "Black" or self.get_checker_details(se3) == "Black_King"
                         or self.get_checker_details(se3) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and self.get_checker_details(se3) is None \
                    and (self.get_checker_details(se4) == "Black" or self.get_checker_details(se4) == "Black_King"
                         or self.get_checker_details(se4) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and self.get_checker_details(se3) is None \
                    and self.get_checker_details(se4) is None \
                    and (self.get_checker_details(se5) == "Black" or self.get_checker_details(se5) == "Black_King"
                         or self.get_checker_details(se5) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and self.get_checker_details(se3) is None \
                    and self.get_checker_details(se4) is None \
                    and self.get_checker_details(se5) is None \
                    and (self.get_checker_details(se6) == "Black" or self.get_checker_details(se6) == "Black_King"
                         or self.get_checker_details(se6) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces

            # NW Capture:
            elif destination_row - starting_row == -2 and destination_column - starting_column == -2 \
                    and (self.get_checker_details(nw) == "Black" or self.get_checker_details(nw) == "Black_King"
                         or self.get_checker_details(nw) == "Black_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw))  # add captured piece to player's capture tally
                self._board[starting_row - 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and (self.get_checker_details(nw2) == "Black" or self.get_checker_details(nw2) == "Black_King"
                         or self.get_checker_details(nw2) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and (self.get_checker_details(nw3) == "Black" or self.get_checker_details(nw3) == "Black_King"
                         or self.get_checker_details(nw3) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and self.get_checker_details(nw3) is None \
                    and (self.get_checker_details(sw4) == "Black" or self.get_checker_details(nw4) == "Black_King"
                         or self.get_checker_details(nw4) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and self.get_checker_details(nw3) is None \
                    and self.get_checker_details(nw4) is None \
                    and (self.get_checker_details(nw5) == "Black" or self.get_checker_details(nw5) == "Black_King"
                         or self.get_checker_details(nw5) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and self.get_checker_details(nw3) is None \
                    and self.get_checker_details(nw4) is None \
                    and self.get_checker_details(nw5) is None \
                    and (self.get_checker_details(nw6) == "Black" or self.get_checker_details(nw6) == "Black_King"
                         or self.get_checker_details(nw6) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces

            # NE Capture:
            elif destination_row - starting_row == -2 and destination_column - starting_column == 2 \
                    and (self.get_checker_details(ne) == "Black" or self.get_checker_details(ne) == "Black_King"
                         or self.get_checker_details(ne) == "Black_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne))  # add captured piece to player's capture tally
                self._board[starting_row - 1][starting_column + 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and (self.get_checker_details(ne2) == "Black" or self.get_checker_details(ne2) == "Black_King"
                         or self.get_checker_details(ne2) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and (self.get_checker_details(ne3) == "Black" or self.get_checker_details(ne3) == "Black_King"
                         or self.get_checker_details(ne3) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NECapture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and self.get_checker_details(ne3) is None \
                    and (self.get_checker_details(ne4) == "Black" or self.get_checker_details(ne4) == "Black_King"
                         or self.get_checker_details(ne4) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and self.get_checker_details(ne3) is None \
                    and self.get_checker_details(ne4) is None \
                    and (self.get_checker_details(ne5) == "Black" or self.get_checker_details(ne5) == "Black_King"
                         or self.get_checker_details(ne5) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and self.get_checker_details(ne3) is None \
                    and self.get_checker_details(ne4) is None \
                    and self.get_checker_details(ne5) is None \
                    and (self.get_checker_details(ne6) == "Black" or self.get_checker_details(ne6) == "Black_King"
                         or self.get_checker_details(ne6) == "Black_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "White_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # Requested destination is invalid for piece
            else:
                raise InvalidSquare

        # BLACK KING:

        elif starting_square_details == "Black_King":
            # S No capture:
            if destination_row - starting_row == 1 and abs(destination_column - starting_column) == 1 \
                    and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                captures += 0  # return number of captured pieces
            # N No capture:
            elif destination_row - starting_row == -1 and abs(destination_column - starting_column) == 1 \
                    and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                captures += 0  # return number of captured pieces

            # SW Capture:
            elif destination_row - starting_row == 2 and destination_column - starting_column == -2 \
                    and (self.get_checker_details(sw) == "White" or self.get_checker_details(sw) == "White_King"
                         or self.get_checker_details(sw) == "White_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and (self.get_checker_details(sw2) == "White" or self.get_checker_details(sw2) == "White_King"
                         or self.get_checker_details(sw2) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and (self.get_checker_details(sw3) == "White" or self.get_checker_details(sw3) == "White_King"
                         or self.get_checker_details(sw3) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and self.get_checker_details(sw3) is None \
                    and (self.get_checker_details(sw4) == "White" or self.get_checker_details(sw4) == "White_King"
                         or self.get_checker_details(sw4) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and self.get_checker_details(sw3) is None \
                    and self.get_checker_details(sw4) is None \
                    and (self.get_checker_details(sw5) == "White" or self.get_checker_details(sw5) == "White_King"
                         or self.get_checker_details(sw5) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SW Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(sw) is None \
                    and self.get_checker_details(sw2) is None \
                    and self.get_checker_details(sw3) is None \
                    and self.get_checker_details(sw4) is None \
                    and self.get_checker_details(sw5) is None \
                    and (self.get_checker_details(sw6) == "White" or self.get_checker_details(sw6) == "White_King"
                         or self.get_checker_details(sw6) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(sw6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces

            # SE Capture:
            elif destination_row - starting_row == 2 and destination_column - starting_column == 2 \
                    and (self.get_checker_details(se) == "White" or self.get_checker_details(se) == "White_King"
                         or self.get_checker_details(se) == "White_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column + 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and (self.get_checker_details(se2) == "White" or self.get_checker_details(se2) == "White_King"
                         or self.get_checker_details(se2) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and (self.get_checker_details(se3) == "White" or self.get_checker_details(se3) == "White_King"
                         or self.get_checker_details(se3) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and self.get_checker_details(se3) is None \
                    and (self.get_checker_details(se4) == "White" or self.get_checker_details(se4) == "White_King"
                         or self.get_checker_details(se4) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and self.get_checker_details(se3) is None \
                    and self.get_checker_details(se4) is None \
                    and (self.get_checker_details(se5) == "White" or self.get_checker_details(se5) == "White_King"
                         or self.get_checker_details(se5) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # SE Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(se) is None \
                    and self.get_checker_details(se2) is None \
                    and self.get_checker_details(se3) is None \
                    and self.get_checker_details(se4) is None \
                    and self.get_checker_details(se5) is None \
                    and (self.get_checker_details(se6) == "White" or self.get_checker_details(se6) == "White_King"
                         or self.get_checker_details(se6) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(se6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces

            # NW Capture:
            elif destination_row - starting_row == -2 and destination_column - starting_column == -2 \
                    and (self.get_checker_details(nw) == "White" or self.get_checker_details(nw) == "White_King"
                         or self.get_checker_details(nw) == "White_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw))  # add captured piece to player's capture tally
                self._board[starting_row - 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and (self.get_checker_details(nw2) == "White" or self.get_checker_details(nw2) == "White_King"
                         or self.get_checker_details(nw2) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and (self.get_checker_details(nw3) == "White" or self.get_checker_details(nw3) == "White_King"
                         or self.get_checker_details(nw3) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and self.get_checker_details(nw3) is None \
                    and (self.get_checker_details(sw4) == "White" or self.get_checker_details(nw4) == "White_King"
                         or self.get_checker_details(nw4) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and self.get_checker_details(nw3) is None \
                    and self.get_checker_details(nw4) is None \
                    and (self.get_checker_details(nw5) == "White" or self.get_checker_details(nw5) == "White_King"
                         or self.get_checker_details(nw5) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NW Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(nw) is None \
                    and self.get_checker_details(nw2) is None \
                    and self.get_checker_details(nw3) is None \
                    and self.get_checker_details(nw4) is None \
                    and self.get_checker_details(nw5) is None \
                    and (self.get_checker_details(nw6) == "White" or self.get_checker_details(nw6) == "White_King"
                         or self.get_checker_details(nw6) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(nw6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces

            # NE Capture:
            elif destination_row - starting_row == -2 and destination_column - starting_column == 2 \
                    and (self.get_checker_details(ne) == "White" or self.get_checker_details(ne) == "White_King"
                         or self.get_checker_details(ne) == "White_Triple_King") and destination_square_details is None:
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne))  # add captured piece to player's capture tally
                self._board[starting_row - 1][starting_column + 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from TWO diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and (self.get_checker_details(ne2) == "White" or self.get_checker_details(ne2) == "White_King"
                         or self.get_checker_details(ne2) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne2))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from THREE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and (self.get_checker_details(ne3) == "White" or self.get_checker_details(ne3) == "White_King"
                         or self.get_checker_details(ne3) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne3))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NECapture (from FOUR diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and self.get_checker_details(ne3) is None \
                    and (self.get_checker_details(ne4) == "White" or self.get_checker_details(ne4) == "White_King"
                         or self.get_checker_details(ne4) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne4))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from FIVE diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and self.get_checker_details(ne3) is None \
                    and self.get_checker_details(ne4) is None \
                    and (self.get_checker_details(ne5) == "White" or self.get_checker_details(ne5) == "White_King"
                         or self.get_checker_details(ne5) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne5))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces
            # NE Capture (from SIX diagonal spaces away):
            elif destination_row - starting_row == 3 and destination_column - starting_column == -3 \
                    and destination_square_details is None \
                    and self.get_checker_details(ne) is None \
                    and self.get_checker_details(ne2) is None \
                    and self.get_checker_details(ne3) is None \
                    and self.get_checker_details(ne4) is None \
                    and self.get_checker_details(ne5) is None \
                    and (self.get_checker_details(ne6) == "White" or self.get_checker_details(ne6) == "White_King"
                         or self.get_checker_details(ne6) == "White_Triple_King"):
                self._board[starting_row][starting_column] = None
                self._board[destination_row][destination_column] = "Black_King"  # move piece to destination
                player.increase_captured_pieces(
                    self.get_checker_details(ne6))  # add captured piece to player's capture tally
                self._board[starting_row + 1][starting_column - 1] = None  # remove captured piece
                captures += 1  # return number of captured pieces

            # Requested destination is invalid for piece
            else:
                raise InvalidSquare

        # WHITE TRIPLE KING:

        elif starting_square_details == "White_Triple_King":
            raise InvalidSquare

        # BLACK TRIPLE KING:

        elif starting_square_details == "Black_Triple_King":
            raise InvalidSquare

        # CHECK FOR WINNER
        if player.get_captured_pieces_count() == 12:
            self._winner = player

        # PROMOTIONS:
        destination_square_details = self.get_checker_details(destination_square_location)
        if destination_row == 7:
            if destination_square_details == "White":
                self._board[destination_row][destination_column] = "White_King"         # promote white
                player.increase_king_count()
            elif destination_square_details == "Black_King":
                self._board[destination_row][destination_column] = "Black_Triple_King"  # promote black king
                player.increase_triple_king_count()
        elif destination_row == 0:
            if destination_square_details == "White_King":
                self._board[destination_row][destination_column] = "White_Triple_King"  # promote white king
                player.increase_triple_king_count()
            elif destination_square_details == "Black":
                self._board[destination_row][destination_column] = "Black_King"         # promote black
                player.increase_king_count()

        # ADJUST TURN:
        if player.get_color() == "White":
            self._player_turn = "Black"
        else:
            self._player_turn = "White"

        # RETURN CAPTURES
        return captures

    def get_checker_details(self, square_location):
        """
        Takes as parameter a square_location on the board and returns the checker
        details present in the square_location
        """

        row = square_location[0]
        column = square_location[1]

        return self._board[row][column]

    def print_board(self):
        """
        Prints the current state of the board.
        """
        print(self._board)

    def print_board_nicely(self):
        """
        Prints the current state of the board.
        """
        print(self._board[0])
        print(self._board[1])
        print(self._board[2])
        print(self._board[3])
        print(self._board[4])
        print(self._board[5])
        print(self._board[6])
        print(self._board[7])

    def print_players(self):
        """
        Prints the current state of the board.
        """
        print(self._players)

    def get_turn(self):
        """
        Prints the current state of the board.
        """
        return self._player_turn

    def game_winner(self):
        """
        Returns status of game via string (name of winner/game has not ended)
        """
        if self._winner is None:
            return "Game has not ended"
        else:
            return self._winner.get_name
