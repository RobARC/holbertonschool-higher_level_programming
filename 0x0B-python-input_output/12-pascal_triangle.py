#!/usr/bin/python3
"""module pascal triangule"""


def pascal_triangle(n):
    """Function  that returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    mylist = []

    if n <= 0:
        return mylist

    for a in range(n):
        row = []
        for b in range(a + 1):
            if b == 0 or b == a:
                row.append(1)
            else:
                row.append(mylist[a-1][b-1] + mylist[a-1][b])
        mylist.append(row)
    return mylist
