#!/usr/bin/python3

if __name__ == "__main__":
    """ A basic calculator taking arguments from CLI"""
    import sys
    from sys import argv
    from calculator_1 import add, sub, mul, div

    opr = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] in list(opr.keys()):
            print("{} {} {} = {}".format(a, argv[2], b, opr[argv[2]](a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
