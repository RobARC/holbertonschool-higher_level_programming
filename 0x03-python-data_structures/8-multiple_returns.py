#!/usr/bin/python3
def multiple_returns(sentence):
    Chr = None
    lenght = len(sentence)
    if lenght > 0:
        Chr = sentence[0]
    new_t = lenght, Chr
    return new_t
