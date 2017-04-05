import d2make


def main():
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
    return res


def compile():
    print('Compiling mud.1')
    d2make.gcc_compiler(main())
