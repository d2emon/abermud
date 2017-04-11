'''
Program starts Here!

This forms the main loop of the code, as well as calling
all the initialising pieces
'''


def compile():
    OBJ = {
        "blib": "d2lib",
        "gmain2": "mud",
        "gmainstubs": "mud.utils",
        "gmlnk": "mud.talker",
        "obdat": None,
        "flock": None,
    }

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
