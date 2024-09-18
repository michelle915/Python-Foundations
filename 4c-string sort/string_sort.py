# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/25/2023
# Description: The following program represents a function that will sort
# a list of strings in alphabetical order.

def string_sort(list):
    """
    Sorts a list of strings in alphabetical order
    """
    for index in range(1, len(list)):
        value = list[index]
        position = index - 1

        while position >= 0 and list[position].lower() > value.lower():
            list[position + 1] = list[position]
            position -= 1
        list[position + 1] = value

