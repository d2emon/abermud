#! /usr/bin/env python
from dummysh import clear_file
import os
import mud
import game
import d2make
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
            print("\t", e)


def init_files():
    print('Initialising files')
    clear_file("mud_syslog")
    clear_file("reset_t")
    clear_file("reset_n")
    clear_file("user_file")


def main():
    print('='*80)

    make_dirs()
    print('-'*80, "\n")

    init_files()
    print('-'*80, "\n")

    d2make.compile_h()
    print('-'*80, "\n")

    game.compile()
    print('-'*80, "\n")

    mud.compile()
    print('-'*80, "\n")

    print('Done')
    print('='*80)

    d2make.makeworld.compile()
    print('-'*80, "\n")
    d2make.ogenerate.compile()
    print('-'*80, "\n")
    d2make.makeuaf.compile()
    print('-'*80, "\n")

    print('Ok')
    print('='*80)

    print('Now set up a password for arthur the archwizard')


if __name__ == "__main__":
    main()
