# project-4d

Write a bubble sort that counts the number of comparisons and the number of exchanges made while sorting a list and returns a tuple of the two values (comparisons first, exchanges second).  Do the same for insertion sort.  Name these functions **bubble_count** and **insertion_count**.

Your functions should **only** count comparisons between the values that are being sorted. Specifically, this line in the insertion sort:

    while pos >= 0 and a_list[pos] > value:
    
contains **two** comparisons - the first one compares a list index to zero, but it doesn't compare values from the list, so it shouldn't be counted. The second one does compare values from the list, so it should be counted, but **remember that if the first comparison is False, the second comparison won't be made** due to the short-circuit behavior of the _and_ operator (Python knows that if the first part is False, then the whole thing will be False, so there's no need to evaluate the second part).

Try sorting various lists with both functions.  What do you notice about the number of comparisons and exchanges made for lists of different sizes?  What do you notice for lists that are nearly sorted vs. lists that are nearly reversed?  You don't need to submit your observations, just the functions.

Hint 1: For insertion sort, every time the value (that is currently getting "inserted" to its correct place) shifts one position to the left counts as an exchange.  Watching the visualization for insertion sort may help make that more intuitive.

Hint 2: If we assume that the insertion sort **has already finished sorting all but the last value**, then finding the right place for the 3 in [2, 4, 6, **3**] and finding the right place for the 1 in [2, 4, 6, **1**] would both take three comparisons, because in both cases the number being placed is first compared to 6, then 4, then 2.

The file must be named: **sorts_count.py**
