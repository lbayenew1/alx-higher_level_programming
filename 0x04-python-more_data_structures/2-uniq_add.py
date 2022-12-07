#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set([])
    for i in my_list:
        new_list.add(i)
    add = 0
    for i in new_list:
        add = add + i
    return add
