#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5
    sum = add(a, b)
    rest = sub(a, b)
    mult = mul(a, b)
    divi = div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, rest))
    print("{} * {} = {}".format(a, b, mult))
    print("{} / {} = {}".format(a, b, divi))

if __name__ == "__main__":
    main()
