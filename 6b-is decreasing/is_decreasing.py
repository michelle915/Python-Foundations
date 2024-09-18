# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/15/2023
# Description: This program contains a function named is_decreasing that verifies
# if a list of numbers is in descending order.

def rec_is_decreasing(list_of_numbers, position):
    """
    This function takes as its parameter a list of numbers and return True if
    the elements of the list are strictly decreasing but return False otherwise.
    """

    if int(list_of_numbers[position]) <= int(list_of_numbers[position + 1]):
        return False

    if position == (len(list_of_numbers) - 2):
        return True

    return rec_is_decreasing(list_of_numbers, position + 1)


def is_decreasing(list_of_numbers):
    """
    Calls recursive rec_is_decreasing function with zero for the second parameter
    """
    return rec_is_decreasing(list_of_numbers, 0)
