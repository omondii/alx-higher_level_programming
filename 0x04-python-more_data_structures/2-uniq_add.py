#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    for number in my_list:
        if number not in unique:
            unique.add(number)

    sum = 0
    for i in unique:
        sum += i

    return (sum)
