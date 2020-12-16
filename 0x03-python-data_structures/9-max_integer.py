#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    if lenght == 0:
        return None
    my_list.sort()
    return my_list[lenght - 1]
