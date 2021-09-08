#!/usr/bin/python3
def uppercase(str):
    for currentLetter in str:
        currentLetter = ord(currentLetter)
        if currentLetter >= 97 and currentLetter <= 122:
            currentLetter -= 32
        currentLetter = chr(currentLetter)
        print("{}".format(currentLetter), end= "")
    print("")
