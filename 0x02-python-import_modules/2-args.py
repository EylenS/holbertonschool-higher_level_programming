#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numArguments = len(sys.argv)
    if numArguments == 1:
        print("0 arguments.")
    elif numArguments == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif numArguments > 2:
        for i in range(1, numArguments + 1):
            print("{} arguments: {}".format(i, sys.argv[i]))
