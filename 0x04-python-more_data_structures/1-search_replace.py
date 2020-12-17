#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [None] * len(my_list)
    count = 0
    for n in my_list:
        if n == search:
            new_list[count] = replace
        else:
            new_list[count] = my_list[count]
        count += 1
    return new_list
