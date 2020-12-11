#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    if lenght == 1:
        print("0 arguments.")
    elif lenght > 2:
        print("{:d} arguments:".format(lenght - 1))
    else:
        print("1 argument:")
    for i in range(1, lenght):
        print("{:d}: {:s}".format(i, argv[i]))
