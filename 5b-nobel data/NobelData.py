# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/8/2023
# Description: This program creates a class that reads a JSON file containing data
# on Nobel Prizes and allows the user to search that data.

import json


class NobelData:
    """
    This class reads a JSON file containing data on Nobel Prizes and allows the
    user to search that data
    """

    def __init__(self):
        """
        Initiates a NobelData object that reads a local JSON file and creates a dictionary with
        the information of Nobel Prize winners
        """

        try:
            with open('nobels.json', 'r') as file:
                self._winner_dictionary = json.load(file)

        except FileNotFoundError:
            print("The file was not found.")

    def search_nobel(self, year, category):
        """
        Given a year and category, returns sorted list of the surnames for the winner(s)
        in that category for that year
        """

        winners = []

        for item in self._winner_dictionary["prizes"]:
            if item["year"] == year and item["category"] == category:
                for laureate_information in item["laureates"]:
                    for info in laureate_information.keys():
                        if info == "surname":
                            winners.append(laureate_information[info])

        return winners
