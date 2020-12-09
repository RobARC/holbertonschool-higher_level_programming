#!/usr/bin/python3

def islower(c):
    c_ascii = ord(c)
    if c_ascii >= 97 and c_ascii <= 1220:
        return True
    else:
        return False
