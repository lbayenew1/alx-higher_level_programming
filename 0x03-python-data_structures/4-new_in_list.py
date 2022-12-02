#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    rng = len(my_list)
    if idx < 0 or idx >= rng:
        return cpy_list
    cpy_list[idx] = element
    return cpy_list
