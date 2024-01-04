#!/usr/bin/python3

"""
defines a rectangle by a private instance attribute width and height
"""
class Rectangle:
    """The defined class Rectangle"""
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if value >= 0:
            self.__width = value
        else:
            raise Exception("width must be an integer")
    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if value >= 0:
            self.__height = value
        else:
            raise Exception("height must be an integer")

