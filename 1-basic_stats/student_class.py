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