# project-6d

You are given a puzzle consisting of a row of squares that contain **nonnegative** integers, with a zero in the rightmost square. Keep in mind that it's possible for other squares to contain a zero. You have a token that starts on the leftmost square.  On each turn, the token can shift left or right a number of squares **exactly** equal to the value in its current square, but is not allowed to move off either end.  For example, if the row of squares contains these values: [2, 4, 5, 3, 1, 3, 1, 4, 0], then on the first turn the only legal move is to shift right two squares, because the starting square contains a 2, and the token can't move off the left end.  The goal is to get the token to the rightmost square (that contains zero).  This row has a solution (more than one), but not all rows do.  If we start with the row [1, 3, 2, 1, 3, 4, 0], then there is no way for the token to reach the rightmost square.

Write a **recursive** function named row_puzzle that takes a list of integers (the row) as a parameter and returns True if the puzzle is solvable for that row, but returns False otherwise. **After the function has finished, the list must be the same as it was when the function was called.**

You may use default arguments and/or helper functions.

Your recursive function must **not**:
* use any loops
* use any variables declared outside of the function
* use any mutable default arguments (see the Code Style Requirements)

Hint 1: Your recursive function needs to try both directions in order to explore all of the possibilities.

Hint 2: If there are possible cycles (as in the first example above), then there are an infinite number of valid paths, but **if there is any valid path, then there is a valid path that doesn't visit any index more than once**, so you only need to worry about paths that don't revisit indices. You may find memoization useful for keeping track of what indices have been visited.

The file must be named: **row_puzzle.py**
