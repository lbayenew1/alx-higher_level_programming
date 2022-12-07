#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        x = 0
        y = 0
        for i in my_list:
            x = x + (i[0] * i[1])
            y = y + i[1]
        return (x / y)
    else:
        return 0
