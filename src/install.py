#! /usr/bin/env python
from dummysh import clear_file
import os
import run_mud
import d2make
import d2make.exe
import d2make.makeworld
import d2make.ogenerate
import d2make.makeuaf


def make_dirs():
    print('Making directories')
    datadir = os.path.abspath(os.path.join(os.getcwd(), '..', 'data'))
    dirs = [
        "text",
        "snoop",
        "examines",
        os.path.join("text", "rooms"),
    ]
    for d in dirs:
        try:
            path = os.path.join(datadir, d)
            print("Making {}".format(path))
            os.mkdir(path)
        except FileExistsError as e:
            print(e)


def init_files():
    print('initialising files')
    clear_file("mud_syslog")
    clear_file("reset_t")
    clear_file("reset_n")
    clear_file("user_file")


def main():
    make_dirs()
    init_files()
    d2make.compile_h()
    d2make.exe.compile()
    run_mud.compile()
    print('Done')

    d2make.makeworld.compile()
    d2make.ogenerate.compile()
    d2make.makeuaf.compile()
    print('Ok')

    print('Now set up a password for arthur the archwizard')


if __name__ == "__main__":
    main()
