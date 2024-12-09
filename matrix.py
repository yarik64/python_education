#!/usr/bin/env python3

import sys


def main(argv):
    print("Hello! This is matrix!!!\nARGV:= ", argv)

    x, y = map(int, argv[:])
    a = [ i+1 for i in range(x)]
    for i in range(y):
        print(*a)
        a.append(a.pop(0))


if __name__ == "__main__": main(sys.argv[1:])
