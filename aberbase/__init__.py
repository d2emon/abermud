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


class AberDb:
    __data = {}
    __fields = {}
    __index = 0

    def __init__(self, **fields):
        self.__fields = fields

    def database(self):
        return("db.json")

    def install(self):
        import json
        with open(self.database(), "w+") as f:
            json.dump(self.__data, open(self.database(), "w"))

    @property
    def index(self):
        return self.__index

    def __str__(self):
        return self.__fields.__str__()

    def __getitem__(self, key):
        return self.__fields[key]

    def __setitem__(self, key, value):
        self.__fields[key] = value

    def __getattr__(self, key):
        return self.__fields[key]

    def __setattr__(self, key, value):
        if key == "_AberDb__fields":
            for k in list(value):
                self[k] = value[k]
        else:
            self.__fields[key] = value

    def load_data(self):
        import json
        self.__data = json.load(open(self.database(), "r"))
        return self.__data

    def save_data(self):
        import json
        self.__data[self.index] = self.__fields
        return json.dump(self.__data, open(self.database(), "w"))

    def load(self, index):
        """
        Return block data for user or -1 if not exist
        """
        self.load_data()
        self.fields = self.load_data().get(index)
        return self.fields

    def save(self):
        self.__data[self.index] = self.fields
        self.save_data()
