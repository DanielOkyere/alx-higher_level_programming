#!/usr/bin/python3
def uppercase(str):
    g = ''
    for s in str:
        if ord(s) >= 97 and ord(s) < 123:
            g += chr(ord(s) - 32)
        else:
            g += s
    print(g)
