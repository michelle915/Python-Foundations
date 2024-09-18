# project-8a

Write a generator function named count_seq that doesn't require any arguments and generates a sequence that starts like this: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112, ...

To get a term of the sequence, count how many there are of each digit (in a row) in the **previous** term.  For example, the first term is "one 2", which gives us the second term "12".  That term is "one 1" followed by "one 2", which gives us the third term "1112".  That term is "three 1" followed by "one 2", or 3112.  Etc.

Your generator function won't just go up to some limit - it will keep going indefinitely. It may need to treat the first one or two terms as special cases, which is fine.  It should yield the terms of the sequence as **strings**, rather than numeric values, for example "1112" instead of 1112.

Here's an example of how your generator function could be used:
```
my_gen = count_seq()
for i in range(10):
    print(next(my_gen))
```

Your file must be named: **count_seq.py**
