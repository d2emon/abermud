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


import blib


def install(src, dst, reset):
    save(dst, load(src))
    import shutil
    shutil.copyfile(dst, reset)


def save(filename, blob):
    with open(filename, "w+") as f:
        blib.sec_write(f, blob, 0, len(blob))


def load(filename):
    objs = []
    with open(filename, "r") as f:
        for s in f:
            data = []

            data.append(int(s.split()[0]))
            data.append(int(f.readline().split()[0]))
            data.append(flags(f.readline().split()[0]))
            data.append(int(f.readline().split()[0]))

            objs.append(data)
    return objs


def flags(s):
    print("Input line is %s" % (s))
    prt = s.split(":")
    res = (
        int(prt[0]),
        int(prt[1]),
        prt[2],
    )
    return res


if __name__ == "__main__":
    install("wldsrc\ob.in", "world\ob.out", "world\reset_data")
