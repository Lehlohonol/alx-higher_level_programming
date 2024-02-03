#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """
    Square class with private instance attributes size
    """

    def __init__(self, size=0):
        """
        Arg:
            size: size of the square
        """
        self.__size = size
