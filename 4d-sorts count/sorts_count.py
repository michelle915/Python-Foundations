# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/25/2023
# Description: The following program represents methods that will count the
# comparisons and exchanges within bubble and insertion sort methods


def bubble_count(list):
    """
    Sorts a list and returns tuple of comparisons and exchanges
    """
    comparisons = 0
    exchanges = 0

    for pass_num in range(len(list) - 1):
        for index in range(len(list) - 1 - pass_num):
            comparisons += 1
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
                exchanges += 1

    total_counts = (comparisons, exchanges)

    return total_counts


def insertion_count(list):
    """
    Sorts a list and returns tuple of comparisons and exchanges
    """

    comparisons = 0
    exchanges = 0

    for index in range(1, len(list)):
        value = list[index]
        position = index - 1

        if list[position] < value:
            comparisons += 1

        while position >= 0 and list[position] > value:
            list[position + 1] = list[position]
            position -= 1
            exchanges += 1
            comparisons += 1
        list[position + 1] = value

    total_counts = (comparisons, exchanges)

    return total_counts

