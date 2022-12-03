#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        f_char = None
    else:
        f_char = sentence[0]
    return len(sentence), f_char
