# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/15/2023
# Description: This program evaluates if a certain row puzzle is solvable.

def rec_row_puzzle(row, token, memory):
    """
    This function will return true if the row puzzle can be solved and false if
    it cannot.
    """
    if memory is None:
        memory = {}

    if token not in memory:

        if (token - row[token]) >= 0:
            memory[token] = (token - row[token])

            rec_row_puzzle(row, (token - row[token]), memory)

        if (token + row[token]) <= (len(row) - 1):
            memory[token] = (token + row[token])

            rec_row_puzzle(row, (token + row[token]), memory)

    if (len(row) - 1) in memory.values():
        return True
    else:
        return False


def row_puzzle(row):
    """
    Calls recursive row_puzzle function with zero for the second parameter
    and None for the third parameter
    """
    return rec_row_puzzle(row, 0, None)

print(row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0]))