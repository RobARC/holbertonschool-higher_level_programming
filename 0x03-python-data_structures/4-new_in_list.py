#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght = len(my_list)

    my_list1 = my_list.copy()

    if idx < 0 or idx > (lenght - 1):
        return my_list1
    my_list1[idx] = element
    return(my_list1)
