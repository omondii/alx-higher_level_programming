#!/usr/bin/python3
"""
raise_exception_msg - raises a name exception and prints a message
message - what is printed incase of name exception match
"""


def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as e:
        raise e
