#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ class square """
        def __init__(self, size=0):
            self.__size = size
        """ Initializing """
        def area(self):
            area = self.__size * self.__size
            return (area)

