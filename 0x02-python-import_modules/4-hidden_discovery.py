#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    l = dir(hidden_4)
    avoid = "__"
    for i in range(len(l)):
        if avoid not in l[i]:
            print(l[i])
