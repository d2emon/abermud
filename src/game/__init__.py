'''
'''


def compile():
    OBJ = [
        "tk",
        """
        parse.o objsys.o extra.o magic.o blood.o weather.o obdat.o new1.o
        support.o zones.o mobile.o
        """,
        "bprintf",
        """
        bbc.o
        """,
        "blib",
        """
        opensys.o
        """,
        "gamego",
        """
        ndebug.o key.o packer.o newuaf.o frob.o
        """,
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
    import game.run
    return game.run.main(*argv)


if __name__ == "__main__":
    import sys
    main(*sys.argv)
