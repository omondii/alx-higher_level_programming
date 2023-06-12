#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    max_no = my_list[0]
    for number in my_list:
        if number > max_no:
            max_no = number

    return (max_no)
