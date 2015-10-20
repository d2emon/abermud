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


def time_created():
    import time
    import os

    import aberbase.files

    return time.ctime(os.path.getmtime(aberbase.files.config().EXE))


def time_started():
    import sys_stubs
    import datetime
    import json

    import aberbase.files

    try:
        current = datetime.datetime.now() - json.load(open(aberbase.files.config().RESET_N, "r"))
        return "Game time elapsed: %s" % (sys_stubs.elapsed(current))
    except OSError:
        return "AberMUD has yet to ever start!!!"


def listfl(name):
    try:
        with open(name, "r+") as f:
            print(f.read())
    except OSError:
        print("[Cannot Find -> %s]\n" % (name))
