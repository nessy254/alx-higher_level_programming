#!/usr/bin/python3
"""Create a class Square."""


class Square:
    """The class square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): size of a side of the Square
        Return: None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the Square."""

        return (self.__size * self.__size)

    @property
    def size(self):
        """create the current size of the Square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Define the == comparison method.
        Args:
            other (Square): another area to compare to.
        """
        return (self.__size == other.__size)

    def __lt__(self, other):
        """Define the < comparison method.
        Args:
            other (Square): another area to compare to.
        """
        return (self.__size < other.__size)

    def __le__(self, other):
        """The <= comparison method.
        Args:
            other (Square): another area to compare to.
        """
        return (self.__size <= other.__size)

    def __gt__(self, other):
        """The > comparison method.
        Args:
            other (Square): another area to compare to.
        """
        return (self.__size > other.__size)

    def __ge__(self, other):
        """The >= comparison method.
        Args:
            other (Square): another area to compare to.
        """
        return (self.__size >= other.__size)

    def __ne__(self, other):
        """The != comparison method.
        Args:
            other (Square): Another area to compare to.
        """
        return (self.__size != other.__size)
