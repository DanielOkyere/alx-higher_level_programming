#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        c = 0
        for i in sys.argv:
            if i != sys.argv[0]:
                c = c + int(i)
        print("{:d}".format(c))
    else:
        print(0)
