#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        list_1 = list(map(lambda x: x * x, row))
        new_list.append(list_1)
    return new_list
