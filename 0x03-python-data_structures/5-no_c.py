#!/usr/bin/python3
def no_c(my_string):
    nw_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            nw_str = nw_str + i
    return nw_str
