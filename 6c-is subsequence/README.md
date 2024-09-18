# project-6c

Write a **recursive** function named is_subsequence that takes two string parameters and returns True if the first string is a subsequence of the second string, but returns False otherwise.

We say that string A is a subsequence of string B if you can derive A by deleting zero or more letters from B without changing the order of the remaining letters. The empty string (which has zero characters) is considered a subsequence of any string (since you can derive it by deleting zero or more letters from any string). You can assume that the only characters in the strings will be lower case letters (though that shouldn't really affect your code).

**Note:** subsequences are different than substrings, since the characters of a subsequence don't have to be consecutive. For example, 'aeiou' is a subsequence of 'faceitious', since all the characters appear in the same order, even though they're not consecutive.

You may use default arguments and/or helper functions.

Your recursive function must **not**:
* use any loops
* use any variables declared outside of the function
* use any mutable default arguments (see the Code Style Requirements)

The file must be named: **is_subsequence.py**
