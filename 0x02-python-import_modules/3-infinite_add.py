#!/usr/bin/python3
"""Adding the command line arg"""
from sys import argv

if __name__ == '__main__':
    a = 0
    if len(argv) == 1:
        print(a)
    else:
        for i in range(1, len(argv)):
            a += int(argv[i])
        print("{:d}".format(int(a)))
