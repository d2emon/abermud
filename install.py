#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2014 МихалычЪ <МихалычЪ@PC>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


def mkDir(dirs):
    for dir in dirs:
        print("TODO: mkdir %s" % (dir))


def catNull(files):
    for f in files:
        print("TODO: cat <dev/null >%s" % (f))

# Installer functions


def install():
    print('Making directories')
    mkDir((
        "TEXT",
        "SNOOP",
        "EXAMINES",
        "TEXT/ROOMS"
    ))

    print('initialising files')
    catNull((
        "mud_syslog",
        "reset_t",
        "reset_n",
        "user_file"
    ))

    import files
    import makeworld
    import ogenerate
    import makeuaf

    print("Building path list")
    files.install()
    print('Built')

    print('Initializing game universe')
    makeworld.make_world()
    print('Game universe intialised')

    print('Generating reset data')
    ogenerate.install("wldsrc/ob.in", "world/ob.out", "world/reset_data")
    print('Reset data generated')

    print('Gerating uaf')
    makeuaf.install("world/uaf.rand")
    print('Uaf generated')

    print('Now set up a password for arthur the archwizard')


if __name__ == "__main__":
    install()

    print("log on as \"debugger\", set a password, and enter the game.")
    print("Enter \"reset\" to make items and mobiles appear, and you're ready to play!")

    import mud1
    mud1.run()
