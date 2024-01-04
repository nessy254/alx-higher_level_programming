#!/usr/bin/python3

"""
defines a rectangle by a private instance attribute width and height
"""

class Rectangle:
    """The defined class Rectangle"""
    def __init__(self, width = 0, height = 0):
        """Initialized rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("weight must be >= 0")
        self.__height = value

    def area(self):
        """get area"""
        return self.__width * self.__height

    def perimeter(self):
        """get perimeter"""
        if self.width or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
