'''
Program starts Here!

This forms the main loop of the code, as well as calling
all the initialising pieces
'''
from .run import main

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


def compile():
    print('Compiling mud.1')
    print({
        "obj": OBJ,
        "include": INCL,
    })


if __name__ == "__main__":
    import sys
    run.main(*sys.argv)
