#!/usr/bin/python3
"""
    0-lookup: lookup()
"""
def lookup(obj):
    """
     returns the list of available attributes and methods of an object
     args:
            obj : objects
    """
    return (dir(obj))
