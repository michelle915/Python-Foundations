# portfolio-project

For this project you will write a class called Checkers that allows two people to play the game of Checkers. This is a variation of the original Checkers game with modified rules. 
Read about the Game rules in Checkers.pdf


**Checkers:**

The Checkers object represents the game as played. 

The class should contain information about the board and the players. The board is initialized when the Checkers object is created.

It must contain these methods (but may have more if you want):
* create_player - takes as parameter the player_name and piece_color that the player wants to play with and creates the player object. The parameter piece_color is a string of value "Black" or "White" representing Black or White checkers pieces respectively. This function returns the player object that has been created.

* play_game - takes as parameter player_name, starting_square_location and destination_square_location of the piece that the player wants to move. The square_location is a tuple in format (x,y). If a player wants to move a piece from third square in the second row to fourth square in the fifth row, the starting and destination square locations will be (1,2) to (4,3). Following the rules of the game move this piece.
    
    * If a player attempts to move a piece out of turn, raise an OutofTurn exception (you'll need to define this exception class).
    * If a player does not own the checker present in the square_location or if the square_location does not exist on the baord; raise an InvalidSquare exception (you'll need to define this exception class).
    * If the player_name is not valid, raise an InvalidPlayer exception (you'll need to define this exception class).
    * This method returns the number of captured pieces, if any, otherwise return 0.
    * If the destination piece reaches the end of opponent's side it is promoted as a king on the board. If the piece crosses back to its original side it becomes a triple king.
    * If the piece being moved is a king or a triple king assess the move according to the rules of the game.
  
* get_checker_details - takes as parameter a square_location on the board and returns the checker details present in the square_location
    * Returns None, if no piece is present in the location
    * If the square_location does not exist on the board, raise an InvalidSquare exception (use the same exception class that was created for play_game function). 
    * If black piece is present return "Black"
    * If white piece is present return "White"
    * If black king piece is present return "Black_king"
    * If white king piece is present return "White_king"
    * If black triple king piece is present return "Black_Triple_King"
    * If white triple king piece is present return "White_Triple_King"
  

* print_board - takes no parameter, prints the current board in the form of an array. Below is an example showing the current board in the initial state (Note, here only the first row is printed, you would print the entire board)

  [[None, "White", None, "White", None, "White", None, "White"],....]

*game_winner - takes no parameter, returns the name of player who won the game.
  If the game has not ended, return "Game has not ended". In this function you need not check this condition - "A less common way to win is when all of your opponent's pieces are blocked so that your opponent can't make any more moves."

**Player:**

Player object represents the player in the game. It is initialized with player_name and checker_color that the player has chosen. The parameter piece_color is a string of value "Black" or "White".

* get_king_count - takes no parameter, returns the number of king pieces that the player has
* get_triple_king_count - takes no parameter, returns the number of triple king pieces that the player has
* get_captured_pieces_count - takes no parameter, returns the number of opponent pieces that the player has captured

In addition to your file containing the code for the above classes, **you must also submit a file that contains unit tests for your classes.  It must have at least five unit tests and use at least two different assert functions.  

Your files must be named **CheckersGame.py** and **CheckersGameTester.py**

For example, your classes will be used as below:

game = Checkers()
Player1 = game.create_player("Adam", "White")

Player2 = game.create_player("Lucy", "Black")

game.play_game("Lucy", (5, 6), (4, 7))

game.play_game("Adam", (2,1), (3,0))

game.get_checker_details((3,1))

Player1.get_captured_pieces_count()
