# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/8/2023
# Description: This program creates a class that reads a JSON file containing data
# on 2010 SAT results for NYC and writes the data to a text file in CSV format.

import json


class SatData:
    """
    This class reads a JSON file containing data on 2010 SAT results for
    NYC and writes the data to a text file in CSV format.
    """

    def __init__(self):
        """
        Initiates a SatData object that reads a local JSON file
        """

        try:
            with open('sat.json', 'r') as file:
                self._sat_records = json.load(file)

        except FileNotFoundError:
            print("The file was not found.")

    def save_as_csv(self, list_of_dbns):
        """
        Takes as a parameter a list of DBNs (district bureau numbers) and saves a CSV file
        that contains information related to the DBNs
        """

        column_headers = ['DBN,', 'School Name,', 'Number of Test Takers,',  'Critical Reading Mean,',
                          'Mathematics Mean,', 'Writing Mean']

        with open('output.csv', 'w') as file:
            for header in column_headers:
                file.write(header)

            file.write('\n')

            for dbn in list_of_dbns:
                for school in self._sat_records["data"]:
                    if school[8] == dbn:

                        school_name = school[9]

                        if ',' in school_name:
                            school_name = '"' + school[9] + '"'

                        school_info = [dbn, ",", school_name, ",", school[10], ",", school[11], ",",
                                       school[12], ",", school[13]]

                        for item in school_info:
                            file.write(item)

                        file.write('\n')
