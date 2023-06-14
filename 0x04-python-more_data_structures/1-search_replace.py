#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_2 = my_list.copy()
    for i in range(len(my_list)):
        list_2[i] = replace if my_list[i] == search else my_list[i]
    return (list_2)
