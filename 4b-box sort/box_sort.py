# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/25/2023
# Description: The following program represents a function that will sort
# boxes by volume.

class Box:
    '''
    Represents a box object with given length, width and height
    '''

    def __init__(self, length, width, height):
        "Creates a box object with given length, width and height"

        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        "Returns volume of box object"
        volume = (self._length * self._width * self._height)
        return volume

    def get_length(self):
        "Returns a box object's length"
        return self._length

    def get_width(self):
        "Returns a box object's width"
        return self._width

    def get_height(self):
        "Returns a box object's height"
        return self._height

def box_sort(list):
    """
    Sorts a list of box objects from greatest volume to least volume
    """
    for index in range(1, len(list)):
        value = list[index]
        position = index - 1

        while position >= 0 and list[position].volume() < value.volume():
            list[position + 1] = list[position]
            position -= 1
        list[position + 1] = value

    return list
