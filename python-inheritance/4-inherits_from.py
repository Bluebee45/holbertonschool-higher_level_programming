#!/usr/bin/python3
"""
4.Only sub class of
Function that returns True if the object is an instance of a class that
inherited from the specified class
"""

def inherits_from(obj, a_class):
    """
    Function that returns True or False
    """
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    return False
