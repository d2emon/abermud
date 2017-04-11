'''
'''


def compile():
    OBJ = {
        "tk": "game.talker",
        """
        parse.o objsys.o extra.o magic.o blood.o weather.o obdat.o new1.o
        """: None,
        "support": None,
        """
        zones.o mobile.o
        """: None,
        "bprintf": "buffer",
        """
        bbc.o
        """: None,
        "blib": "d2lib",
        """
        opensys.o
        """: None,
        "gamego": "game",
        """
        ndebug.o key.o packer.o newuaf.o frob.o
        """: None,
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
    import game.run
    return game.run.main(*argv)


if __name__ == "__main__":
    import sys
    main(*sys.argv)
