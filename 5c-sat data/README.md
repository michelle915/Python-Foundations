# project-5c

For this project, you will import the **json** module.

Write a class named SatData that reads a [JSON file containing data on 2010 SAT results for New York City](https://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.json?accessType=DOWNLOAD) and writes the data to a text file in CSV format. That same JSON file will be provided as a local file in Gradescope named **sat.json**, so you don't need to upload it to Gradescope. Your code does not need to access the internet. For testing on your computer, download the file at that link and put it in your PyCharm project.

CSV is a very simple format - just commas separating columns and newlines separating rows (see note below about commas that are part of field names). You'll see an example of CSV format below. There is a csv module for Python, but you will not use it for this project.

Your class should have:
* an init method that reads the file and stores it in whatever data member(s) you prefer. Any data members of the SatData class must be **private**.
* a method named **save_as_csv** that takes as a parameter a list of DBNs (district bureau numbers) and saves a CSV file that looks like [this](https://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.csv?accessType=DOWNLOAD), but with only the rows that correspond to the DBNs in the list (and also the row of column headers). **To see what CSV syntax looks like, open the file as a text file rather than as a spreadsheet.** You may assume that all of the DBNs in the list passed to your method are present in the JSON file.  The rows in the CSV file must be sorted in ascending order by DBN.  The name of the output file must be **output.csv**.

For example, your class could be used like this:
```
sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)
```

You may hardcode the column headers instead of having to read them from the JSON file.

Some of the school names contain one or more commas. How should you preserve such a name as a single field in CSV format, since commas normally separate fields? The correct way to handle that is to enclose such names in double quotes in your CSV file.  If you open up the example CSV file in a text editor, you can see that's what it does.

Don't let the CSV part intimidate you. You're just taking the values for a row, making them into a string that has commas between the values (and with double quotes around the values that contain commas), and then writing those strings to a file.

The file must be named: **SatData.py**
