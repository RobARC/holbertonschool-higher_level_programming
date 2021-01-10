#!/bin/usr/python3
"""module text_identation"""

 
    def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    b = 0
<<<<<<< HEAD
    if type(text) != str:
        raise TypeError("text must be a string")

    lenght = len(text)
    while b < lenght:
        print(text[b], end="")
        if text[b] is '.' or text[b] is '?' or text[b] is ':':
            print("\n")
            if (b + 1) < lenght:
                while text[b + 1] is " ":
                    b += 1
=======
    c = '?'
    d = ':'
  
    if type(text) != str:
        raise TypeError("text must be a string")
        
        lenght = len(text)
        while b < lenght:
            print(text[b], end="")
            if text[b] is a or text[b] is c or text[b] is d:
                print("\n")
                if (b + 1) < lenght:
                    while text[b + 1] is " ":
                        b += 1
>>>>>>> 744a3fd5d9c8503f94fa4b5e3defe447397bc660
        b += 1

