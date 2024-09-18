# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 3/1/2023
# Description: This program creates a generator function that will indefinitely
# generate a new term that follows the pattern 2, 12, 1112, 3112, 132112, ...

def count_seq():
    """
    Generates terms for a sequence. Each term of the sequence is built by
    counting how many there are of each digit (in a row) in the previous term.
    For example, the first term is "one 2", which gives us the second term "12".
    That term is "one 1" followed by "one 2", which gives us the third term "1112".
    """
    term = "2"

    while True:
        yield term

        new_term = ""
        index = 0
        number = term[index]

        while index < len(term):
            occurrence = 0

            while index < len(term) and term[index] == number:
                occurrence += 1
                index += 1
            new_term += str(occurrence) + number

            if index < len(term):
                number = term[index]

        term = new_term
