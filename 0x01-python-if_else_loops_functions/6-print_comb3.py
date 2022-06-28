#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if y > x:
            print('{:d}{:d}'.format(x, y), end='')
            if '{:d}{:d}'.format(x, y) == '89':
                print('')
            else:
                print(', ', end='')
        else:
            continue
