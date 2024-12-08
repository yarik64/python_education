#!/usr/bin/env python3

import os, sys


def main(argv):
    print("Hello! This is matrix!!!\n",
          "ARGV:= ", *argv
          )

if __name__ == "__main__": main(sys.argv[1:])
