#!/usr/bin/python3
"""
safe_print_division(a, b) - divides 2 integers and prints the result
a, b - integers to divide
Return - if no error is received, inside result. Else, None
"""


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
