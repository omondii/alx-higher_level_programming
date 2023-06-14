#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = dict(sorted(a_dictionary.items(), key=lambda x: str(x[1])))
    return (sort)
