#!/usr/bin/python3
""" 
    interpreter 
    """


class Square:
    """ class square """
        def __init__(self, size=0):
            self.__size = size
        """ Initializing """
        def area(self):
            area = self.__size * self.__size
            return (area)
        def size(self, value):
            if size is not int
                raise TypeError("size must be an integer")
            if size < 0
                raise ValueError("size must be >= 0")

