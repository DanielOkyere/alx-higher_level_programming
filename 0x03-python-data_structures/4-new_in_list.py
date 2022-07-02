#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list[:]
    if idx < 0 or idx > len(my_list):
        return cpy_list
    else:
        cpy_list[idx] = element
        return cpy_list
