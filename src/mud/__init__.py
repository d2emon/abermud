'''
Program starts Here!

This forms the main loop of the code, as well as calling
all the initialising pieces
'''


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


def main(*argv):
    import mud.run
    return mud.run.main(*argv)


if __name__ == "__main__":
    import sys
    main(*sys.argv)
