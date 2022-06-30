#!/usr/bin/python3

import sys


def main(*argv):
    lstring = len(sys.argv) - 1
    c = 0
    if lstring > 1:
        print("{:d} arguments:".format(lstring))
        for i in sys.argv:
            if c != 0:
                print("{:d}: {}".format(c, i))
            c += 1
    elif lstring == 0:
        print("{:d} arguments.".format(lstring))
    else:
        print("{:d} argument:".format(lstring))
        print("{:d}: {}".format(1, sys.argv[1]))


if __name__ == "__main__":
    main()
