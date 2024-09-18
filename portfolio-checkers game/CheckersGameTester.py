# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/18/2023
# Description: The following program contains unit tests for the Class Checkers that allows two people
# # to play the game of checkers.

import unittest
from CheckersGame import InvalidPlayer, InvalidSquare, OutOfTurn, Player, Checkers


class CheckersTester(unittest.TestCase):
    """Contains unit tests for the Class Checkers"""

    def test_1(self):
        """Tests initiation of chess board and print_board method"""

        game = Checkers()
        print(f"Test 1")
        game.print_board()

    def test_2(self):
        """Tests the create player method"""

        game = Checkers()
        player1 = game.create_player("Adam", "White")
        player2 = game.create_player("Lucy", "Black")

        self.assertEqual(player1.get_name(), 'Adam')
        self.assertEqual(player2.get_name(), 'Lucy')
        self.assertEqual(player1.get_color(), 'White')
        self.assertEqual(player2.get_color(), 'Black')

        print(f"Test 2")
        print(f"Player 1: {player1.get_name()}")
        print(f"Player 2: {player2.get_name()}")
        game.print_players()

    def test_3(self):
        """Test valid moves"""

        game = Checkers()
        game.create_player("Adam", "White")
        game.create_player("Lucy", "Black")

        print(f"Test 3")
        print("Starting board:")
        game.print_board()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (2, 1), (3, 0))
        game.print_board()

        print(f"Turn: {game.get_turn()}")
        print("Black moves:")
        game.play_game("Lucy", (5, 6), (4, 7))
        game.print_board()

    def test_4(self):
        """Test capture"""

        game = Checkers()
        player1 = game.create_player("Adam", "White")
        player2 = game.create_player("Lucy", "Black")

        print(f"Test 3")
        print("Starting board:")
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (2, 1), (3, 2))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("Black moves:")
        game.play_game("Lucy", (5, 4), (4, 3))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (3, 2), (5,4))
        game.print_board_nicely()

        self.assertEqual(player1.get_captured_pieces_count(), 1)

    def test_5(self):
        """Test king promotion"""

        game = Checkers()
        player1 = game.create_player("Adam", "White")
        player2 = game.create_player("Lucy", "Black")

        print(f"Test 3")
        print("Starting board:")
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (2, 1), (3, 2))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("Black moves:")
        game.play_game("Lucy", (5, 4), (4, 3))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (3, 2), (5,4))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("Black moves:")
        game.play_game("Lucy", (5, 6), (4, 7))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (2, 5), (3, 6))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("Black moves:")
        game.play_game("Lucy", (6, 7), (5, 6))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (1, 4), (2, 5))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("Black moves:")
        game.play_game("Lucy", (7, 6), (6, 7))
        game.print_board_nicely()

        print(f"Turn: {game.get_turn()}")
        print("White moves:")
        game.play_game("Adam", (5, 4), (7, 6))
        game.print_board_nicely()

        self.assertNotEqual(player1.get_captured_pieces_count(), 1)
        self.assertEqual(player1.get_king_count(), 1)
