# project-5b

For this project, you will import the **json** module.

Write a class named NobelData that reads a [JSON file containing data on Nobel Prizes](http://api.nobelprize.org/v1/prize.json) and allows the user to search that data. That same JSON file will be provided as a local file in Gradescope named **nobels.json**, so you don't need to upload it to Gradescope. Your code does not need to access the internet. For testing on your computer, download the file at that link and put it in your PyCharm project.

Your class should have:
* an init method that reads the file and stores it in whatever data member(s) you prefer. Any data members of the NobelData class must be **private**.
* a method named search_nobel that takes as parameters a year and a category, and returns a sorted list (in normal English dictionary order) of the surnames for the winner(s) in that category for that year (up to three people can share the prize).  The year will be a string (e.g. "1975"), not a number.  The categories are: "chemistry", "economics", "literature", "peace", "physics", and "medicine".

Your code will not be tested on entries that don't have a surname, including cases where there are no laureates.

For example, your class could be used like this:
```
nd = NobelData()
nd.search_nobel("2001", "economics")
```

The file must be named: **NobelData.py**
