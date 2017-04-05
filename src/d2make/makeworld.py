import d2make


def main():
    OBJ = [
        "makeworld",
        "blib",
    ]

    INCL = []

    res = {
        "obj": OBJ,
        "include": INCL,
        "filename": "makeworld.util",
    }
    return res


def compile():
    print('Compiling world maker')
    d2make.gcc_compiler(main())
    print("--->\tmakeworld.util")
    print('Game universe intialised')
