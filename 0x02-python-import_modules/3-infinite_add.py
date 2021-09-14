#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numArguments = len(sys.argv)
    sum = 0
    for index in range(1, numArguments):
        sum += int(sys.argv[index])
    print(sum)
