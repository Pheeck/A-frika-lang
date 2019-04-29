#! /usr/bin/env python

import sys
from brainfuck import evaluate
from re import findall


DICT = {
    "A. A?": ">",
    "A? A.": "<",
    "A. A.": "+",
    "A! A!": "-",
    "A. A!": ",",
    "A! A.": ".",
    "A! A?": "[",
    "A? A!": "]"
}


class InterpreterException(Exception):
    pass


def execute(filename):
    f = open(filename, "r")
    print(evaluate(convert(f.read())))
    f.close()

def convert(string):
    result = ""
    for seq in cleanup(string):
        if seq in DICT:
            result += DICT[seq]
        else:
            raise InterpreterException("Invalid sequence '" + str(seq) + "'")
    return result

def cleanup(string):
    foo = findall(r'A[.!?][^A.!?]*A[.!?]', string.upper())
    return [x[:2] + " " + x[-2:] for x in foo]

def main():
    if len(sys.argv) == 2: execute(sys.argv[1])
    else: print("Usage:", sys.argv[0], "filename")


if __name__ == "__main__": main()
