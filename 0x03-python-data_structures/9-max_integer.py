#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        tmp = my_list[0]
        for i in range(len(my_list) - 1):
            if tmp < my_list[i+1]:
                tmp = my_list[i + 1]
    return tmp
