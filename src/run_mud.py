#! /usr/bin/env python
import mud


def compile():
    OBJ = [
        "blib",
        "gmain2",
        "gmainstubs",
        "gmlnk",
        "obdat",
        "flock",
    ]

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
    print(res)


def main():
    import sys
    mud.main(*sys.argv)


if __name__ == "__main__":
    main()
