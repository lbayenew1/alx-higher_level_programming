#!/usr/bin/python3
def element_at(my_list, idx):
    rng = len(my_list)
    if idx < 0:
        return None
    if idx >= rng:
        return None
    return my_list[idx]
