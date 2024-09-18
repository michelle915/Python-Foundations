# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/8/2023
# Description: This program takes as a parameter the name of a text file that
# contains a list of numbers. The function sums the values in the file and writes
# the sum to a text file named sum.txt

def file_sum(infile):
    """
    Takes in a text file with numbers, sums the numbers, and creates a new text file
    with the sum.
    """

    sum_of_file = 0

    try:
        with open(infile, 'r') as file:
            for line in file:
                number = float(line)
                sum_of_file += number

    except FileNotFoundError:
        print("The file was not found.")

    with open('sum.txt', 'w') as outfile:
        outfile.write(str(sum_of_file))
