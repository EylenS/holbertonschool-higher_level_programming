#!/usr/bin/python3
import sys

def main():
    numArguments = len(sys.argv)
    sum = 0
    for index in range(1, numArguments):
        sum += int(sys.argv[index])
    print(sum)

if __name__ == "__main__":
    main()
