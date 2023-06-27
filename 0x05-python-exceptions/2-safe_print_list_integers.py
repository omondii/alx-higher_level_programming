#!/usr/bin/python3
"""
   safe_print_list_integers -  prints the first x elements of
a list and only integers
   my_list - list to print items from
   x - index to stop at
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except TypeError:
        print()
    finally:
        print()
        return count
