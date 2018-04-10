from .compiler import gcc
from dummysh import cp


def main():
    OBJ = [
        "ogen",
        "blib",
    ]

    INCL = []

    res = {
        "obj": OBJ,
        "include": INCL,
        "filename": "ogenerate",
        "output": "ob.out",
    }
    return res


def compile():
    print('Compiling reset data compiler')
    gcc(main())
    cp("ob.out", "reset_data")
    print("--->\togenerate")
    print('Reset data generated')
