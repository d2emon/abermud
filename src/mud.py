#! /usr/bin/env python
import d2make


def compile():
    OBJ = ["""
    blib.o gmain2.o gmainstubs.o gmlnk.o obdat.o flock.o
    """, ]

    INCL = [
        "object.h",
        "files.h",
        "System.h",
    ]

    res = {
        "obj": OBJ,
        "include": INCL,
    }

    print('Compiling mud.1')
    d2make.gcc_compiler(res)


def main():
    pass


if __name__ == "__main__":
    main()
