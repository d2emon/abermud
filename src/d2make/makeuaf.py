import d2make


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
    d2make.gcc_compiler(main())
