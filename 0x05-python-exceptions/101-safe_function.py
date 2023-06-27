#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        error = "Exception: {}".format(str(e))
        print(error, file=sys.stderr)
        return None
