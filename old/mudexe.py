#!/usr/bin/env python
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


def run():
    obj = (
        "tk.o",
        "parse.o",
        "objsys.o",
        "extra.o",
        "magic.o",
        "blood.o",
        "weather.o",
        "new1.o",
        "support.o",
        "zones.o",
        "mobile.o",
        "bprintf.o",
        "bbc.o",
        "opensys.o",
        "gamego.o",
        "ndebug.o",
        "key.o",
        "packer.o",
        "newuaf.o",
        "frob.o",
    )
    incl = (
        "object.h",
        "files.h",
        "System.h",
        "blib.o",
        "obdat.o",
        "flock.o",
    )
    print({"mud.exe": (obj, incl)})
    print("TODO: mud.exe")
