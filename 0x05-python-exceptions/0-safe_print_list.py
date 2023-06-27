#!/usr/bin/python3
"""
   safe_print_list: prints x elements of a list
   using try / except:
   my_list: the list to pt=rint
   x: function stops here and returns total prints done
"""


def safe_print_list(my_list=[], x=0):

    count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    finally:
        print ()
        return min(x, count)
