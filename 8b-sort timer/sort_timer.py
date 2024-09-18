# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 3/1/2023
# Description: This program decorates sort functions so that the time it takes the
# sort functions to run is recorded and creates a sort function that will plot the
# run times of two decorated sort functions

import time
import random
from matplotlib import pyplot
import functools


def sort_timer(func):
    """
    Times how many seconds it takes a sort function to run.
    Returns elapsed time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - begin_time
        return elapsed_time
    return wrapper


@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order. Decorated with sort time
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order. Decorated with sort time
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(sort_func_1, sort_func_2):
    """
    Takes two decorated sort functions as parameters and generates a
    graph of sort times.

    X-axis: the number of elements being sorted
    Y-axis: time in seconds
    """
    x_coordinates = []
    func_1_y_coordinates = []
    func_2_y_coordinates = []
    x = 1
    while x <= 10:
        length_of_list = 1000 * x
        x_coordinates.append(length_of_list)

        list_1 = []
        for i in range(length_of_list):
            list_1.append(random.randint(1, 10000))
        list_2 = list(list_1)

        func_1_y_coordinates.append(sort_func_1(list_1))
        func_2_y_coordinates.append(sort_func_2(list_2))
        x += 1

    pyplot.plot(x_coordinates, func_1_y_coordinates, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(x_coordinates, func_2_y_coordinates, 'go--', linewidth=2, label='Insert Sort')
    pyplot.xlabel("the number of elements being sorted")
    pyplot.ylabel("time in seconds")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)
