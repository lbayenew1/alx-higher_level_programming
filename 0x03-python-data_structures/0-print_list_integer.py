#!/usr/bin/python3
def print_list_integer(my_list=[]):
    items = len(my_list)
    for i in range(0, items):
        print('{:d}'.format(i))
