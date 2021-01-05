#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as Error:
        sys.stderr.write("Exception: " + str(Error) + "\n")
        return(False)
    return(True)
