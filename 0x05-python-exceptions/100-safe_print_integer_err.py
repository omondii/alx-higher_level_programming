#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        number = int(value)
        print("{:d}".format(number))
        return True
    except ValueError:
        error = "Exception: Cannot convert '{}' to an interger".format(value)
        print(error, file=sys.stderr)
        return False
