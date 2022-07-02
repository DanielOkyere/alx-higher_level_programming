#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    idx = 0
    idx_store = []
    for i in my_list:
        if i % 2 == 0:
            idx_store.append(True)
        else:
            idx_store.append(False)

    return idx_store
