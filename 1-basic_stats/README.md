# project-1

For this project, you will `import` the **statistics** module.

Write a class called Student that has two **private** data members - the student's name and grade.  It should have an init method that takes two values and uses them to initialize the data members. It should have a `get_grade` method.

Write a separate function (not part of the Student class) called `basic_stats` that takes as a parameter a list of Student objects and returns a tuple containing the mean, median, and mode of all the grades.  To do this, use the mean, median and mode functions in the [statistics module](https://docs.python.org/3/library/statistics.html).  Your `basic_stats` function should return those three values as a tuple, in the exact order given above.

As an example, your code could be called as follows by the grader:
```
s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values
```
You can test your program with the above example but make sure to not leave
that as part of your submission.

The file must be named: **basic_stats.py**

**Mini-review:** A private data member of a class has a name that begins with a **single** underscore.  Private data members can be directly accessed from within the class, but **not** from outside the class.  Instead, if a data member needs to be accessed or manipulated from outside the class, then the class should provide a method that can be called to carry out the necessary actions.  This access restriction is not enforced by the Python language as it is in some other languages, due to the Python philosophy of "we're all adults here".

