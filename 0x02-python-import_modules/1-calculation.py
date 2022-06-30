#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    addition = add(a, b)
    multiply = mul(a, b)
    subtract = sub(a, b)
    division = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, addition))
    print("{:d} - {:d} = {:d}".format(a, b, subtract))
    print("{:d} * {:d} = {:d}".format(a, b, multiply))
    print("{:d} / {:d} = {:d}".format(a, b, division))
