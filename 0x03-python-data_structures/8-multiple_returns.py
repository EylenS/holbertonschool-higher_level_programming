#!/usr/bin/python3
def multiple_returns(sentence):
    how_many_chars = len(sentence)
    if how_many_chars == 0:
        return (how_many_chars, None)
    return (how_many_chars, sentence[0])
