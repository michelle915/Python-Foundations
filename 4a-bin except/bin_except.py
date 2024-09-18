# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/25/2023
# Description: The following program modifies a binary search function.

class TargetNotFound(Exception):
    "Exception will raise when target value is not in the list"
    pass


def bin_except(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, raises TargetNotFound exception, indicating
    the target value isn't in the list
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound
