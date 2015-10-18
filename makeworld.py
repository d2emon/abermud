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


import blib


def make_world():
    filename = "world.tmp"
    c = 64
    l = 4

    b = 0
    x = [[0, 1][i < 2] for i in range(0, c * l)]
    with open(filename, "w+") as f:
        blib.sec_write(f, x, 0, c)
        for i in range(0, 600):
            blib.sec_write(f, x, i, c)
            x[0] = 0
    return x


if __name__ == "__main__":
    x = make_world()
    print(x)
