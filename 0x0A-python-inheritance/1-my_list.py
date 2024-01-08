#!/usr/bin/python3
"""
    1-my_list: MyList()
"""


class MyList(list):
    """
        inherits from list
        Methods: print_sorted(prints list in ascending order)
    """
    def print_sorted(self):
        """
        prints a list in ascending order
        """
        print(sorted(self))
