#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as Error:
        sys.stderr.write("Exception: " + str(Error) + "\n")
        return (None)
    return (result)
