#!/usr/bin/python3
"""Defines a function that changes the format of the text
according to some characters founded."""


def text_indentation(text):
    """Based on the test passed,
    prints the text with 2 new lines after each of these
    characters: ., ? and :
    On the other hand, there should be no space at the
    beginning or at the end of each printed line.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
            if i == len(text) - 1:
                break
            if text[i + 1] == " ":
                i += 1
            while text[i] == " " and text[i + 1] == " " and \
            i + 1 < len(text):
                i += 1
        i += 1
