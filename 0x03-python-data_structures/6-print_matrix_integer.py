#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    count = 0
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end='')
            if count != (len(matrix) - 1):
                print('{:s}'.format(' '), end="")
                count += 1
        count = 0
        print("")
