#!/usr/bin/python3
"""
list_division - divides element by element 2 lists
my_list_1, my_list_2 - lists to divide
list_length - can be bigger than the len of both lists
"""


def list_division(my_list_1, my_list_2, list_length):
    return_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            return_list.append(result)
    return return_list
