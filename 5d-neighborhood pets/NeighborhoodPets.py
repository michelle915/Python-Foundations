# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/8/2023
# Description: This program represents a neighborhood of pets and tracks various
# pet information.

import json


class DuplicateNameError(Exception):
    """Exception for duplicate name errors"""
    pass


class NeighborhoodPets:
    """
    This class has methods for adding a pet, deleting a pet, searching for the owner
    of a pet, saving data to a JSON file, loading data from a JSON file, and getting
    a set of all pet species.
    """

    def __init__(self):
        """
        Initiates NeighborhoodPets class. Creates empty list of neighborhood pets
        """
        self._neighborhood_pets = []

    def add_pet(self, name, species, owner):
        """
        Adds pet to list of neighborhood pets.
        """

        for pet in self._neighborhood_pets:
            if pet["Name"] == name:
                raise DuplicateNameError

        new_pet = {"Name": name, "Species": species, "Owner": owner}
        self._neighborhood_pets.append(new_pet)

    def delete_pet(self, name):
        """
        Removes pet from list of neighborhood pets
        """
        for pet in self._neighborhood_pets:
            if pet["Name"] == name:
                self._neighborhood_pets.remove(pet)

    def get_owner(self, name):
        """
        Returns the name of a pet's owner
        """
        for pet in self._neighborhood_pets:
            if pet["Name"] == name:
                return pet["Owner"]

    def save_as_json(self, save_as):
        """
        Saves a JSON file with neighborhood pet info
        """
        with open(save_as, 'w') as outfile:
            json.dump(self._neighborhood_pets, outfile)

    def read_json(self, user_file):
        """
         Takes as a parameter the name of a file to read and loads that file.
         This will replace all the pets currently in memory.
        """
        try:
            with open(user_file, 'r') as file:
                self._neighborhood_pets = json.load(file)

        except FileNotFoundError:
            print("The file was not found.")

    def get_all_species(self):
        """
        Returns a Python set of the species of all pets
        """
        species_list = set()

        for pet in self._neighborhood_pets:
            species_list.add(pet["Species"])

        return species_list

