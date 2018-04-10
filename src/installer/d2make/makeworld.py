from .compiler import gcc


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
    gcc(main())
    print("--->\tmakeworld.util")
    print('Game universe intialised')
