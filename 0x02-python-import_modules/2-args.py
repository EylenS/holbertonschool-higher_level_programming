#!/usr/bin/python3
import sys

def main():
    numArguments = len(sys.argv) -1
    
    if numArguments == 0:
        print("0 arguments.")
    elif numArguments == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(numArguments))
        for i in range(1, numArguments + 1):
            print("{} arguments: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()