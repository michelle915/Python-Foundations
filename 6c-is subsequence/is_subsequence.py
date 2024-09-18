# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/15/2023
# Description: This program contains a function named is_subsequence that determines
# if one string is a subsequence of another string.

def is_subsequence(string_a, string_b):
    """
    This function takes two string parameters and returns True if the first string
    is a subsequence of the second string, but returns False otherwise.
    """

    if string_a == "":
        return True
    elif string_b == "":
        return False
    elif string_a[0] == string_b[0]:
        return is_subsequence(string_a[1:], string_b[1:])
    elif string_a[0] != string_b[0]:
        return is_subsequence(string_a, string_b[1:])
