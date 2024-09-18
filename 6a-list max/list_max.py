# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/15/2023
# Description: This program contains a function named list_max that takes as its parameter
# a list of numbers and returns the maximum value in the list.

def rec_list_max(list_of_numbers, position, max_of_list):
    """
    Returns the max number of a list of numbers. The position and max of
    list parameters must be zero
    """

    if int(list_of_numbers[position]) > max_of_list:
        max_of_list = int(list_of_numbers[position])

    if position == (len(list_of_numbers) - 1):
        return max_of_list

    return rec_list_max(list_of_numbers, position + 1, max_of_list)


def list_max(list_of_numbers):
    """
    Calls recursive rec_list_max function with zero for the second and third parameter
    """
    return rec_list_max(list_of_numbers, 0, 0)
