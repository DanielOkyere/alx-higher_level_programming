#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    index = 0
    for i in new_string:
        new_string[index] = '' if (i == 'c' or i == 'C') else i
        index += 1
    return ''.join(new_string)
