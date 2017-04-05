#! /usr/bin/env python
from dummysh import mkdir, clear_file
import d2make
import d2make.exe
import mud
import d2make.makeworld
import d2make.ogenerate
import d2make.makeuaf


def make_dirs():
    print('Making directories')
    mkdir("TEXT")
    mkdir("SNOOP")
    mkdir("EXAMINES")
    mkdir("TEXT/ROOMS")


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
    mud.compile()
    print('Done')

    d2make.makeworld.compile()
    d2make.ogenerate.compile()
    d2make.makeuaf.compile()
    print('Ok')

    print('Now set up a password for arthur the archwizard')


if __name__ == "__main__":
    main()
