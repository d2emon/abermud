#! /usr/bin/env python


def compile():
    OBJ = [
        """
        tk.o parse.o objsys.o extra.o magic.o blood.o weather.o obdat.o new1.o
        support.o zones.o mobile.o bprintf.o bbc.o blib.o opensys.o gamego.o ndebug.o
        key.o packer.o newuaf.o frob.o flock.o
        """,
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


def main(title='', user=None):
    from config import CONFIG
    print(CONFIG['EXE'])
    print({
        'title': title,
        'user': user,
    })
    return 0


if __name__ == "__main__":
    main()
