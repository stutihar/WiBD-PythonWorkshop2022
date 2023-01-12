#!/usr/bin/env python

import sys

def greet(name):
    print("Hello", name)

def main():
    greet(sys.argv[1])

if __name__ == '__main__':
    main()