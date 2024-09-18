# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/10/2023
# Description: The following program returns class grade statistics (mean, median, mode)
# when given student names and grades. The program does so by creating a Student class
# (that stores a student's name and grade and can return a student's grade) and by
# defining a basic_stats function that will print class grade statistics when passed
# a list of Students.


from statistics import mean
from statistics import median
from statistics import mode

class Student:
    '''
    Represents a Student
    '''
    def __init__(self, name, grade):
        "Creates a Student with specific name and grade"
        self._name = name
        self._grade = grade

    def get_grade(self):
        "Returns student's grade"
        return self._grade


def basic_stats(list_of_students):
    '''
    Returns class grade mean, median, and mode when given list of Students
    '''
    list_of_grades = []

    for student in list_of_students:
        list_of_grades.append(student.get_grade())

    class_mean = mean(list_of_grades)
    class_median = median(list_of_grades)
    class_mode = mode(list_of_grades)
    class_stats = (class_mean, class_median, class_mode)

    return class_stats