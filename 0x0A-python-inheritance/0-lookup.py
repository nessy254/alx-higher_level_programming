#!/usr/bin/python3
"""
    0-lookup: lookup()
"""


def lookup(obj):
    """
        Returns the list of available attributes and methods of an object
        Args:
            obj : objects
    """
    return (dir(obj))
