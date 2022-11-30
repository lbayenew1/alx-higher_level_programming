#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = ord(c) - 32
            c = chr(c)
        print("{}".format(c), end="")
    print()
