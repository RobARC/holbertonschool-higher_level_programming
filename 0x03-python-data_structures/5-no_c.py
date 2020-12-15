#!/usr/bin/python3
def no_c(my_string):
    mychr = ""
    for i in my_string:
        if i == 'C' or i == 'c':
            continue
        mychr += i
    return(mychr)
