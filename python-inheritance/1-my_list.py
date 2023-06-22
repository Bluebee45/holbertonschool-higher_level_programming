#!/usr/bin/python3
"""
1. My list
"""

class MyList(list):
    """
    Class MyList that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
