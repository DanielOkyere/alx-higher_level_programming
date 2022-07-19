#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            print("{}".format(my_list[count]), end="")
            count += 1
        print("", end="\n")
        return count
    except IndexError:
        return count
