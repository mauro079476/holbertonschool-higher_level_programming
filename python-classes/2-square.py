#!/usr/bin/python3
"""python interpreter"""


class Square:
    """empty class"""


    def __init__(self, size=0):
        """initialazing class"""
        self.__size = size
            
        if size is not int
            raise TypeError('size must be an integer')
        if size is <  0
            raise ValueError('size must be >= 0')
