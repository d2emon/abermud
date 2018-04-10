from .compiler import gcc


def main():
    OBJ = [
        "makeuaf",
    ]

    INCL = []

    res = {
        "obj": OBJ,
        "include": INCL,
        "filename": "makeuaf",
        "output": "uaf.rand",
    }
    return res


def compile():
    print('Compiling uaf generator')
    gcc(main())
