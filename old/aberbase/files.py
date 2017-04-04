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


class Config():
    __params = {}
    filename = "files.yml"

    def __init__(self, filename = False):
        self.load(filename)

    def load(self, filename = False):
        if filename:
            self.filename = filename

        import yaml
        self.__params.update(yaml.load(open(self.filename, 'r')))

    def save(self, filename = False):
        if filename:
            self.filename = filename

        import yaml
        yaml.dump(self.__params, open(self.filename, "w+"), default_flow_style = False, )

    def __getitem__(self, key):
        if key in self.__params:
            return self.__params[key]
        else:
            return False

    def __setitem__(self, key, value):
        self.__params[key] = value

    def __getattr__(self, key):
        if key in self.__params:
            return self.__params[key]
        else:
            return False

    def __setattr__(self, key, value):
        self.__params[key] = value

    def __str__(self):
        return str(self.__params)


__config = Config()


def config():
    global __config
    return __config


def install(path):
    import socket

    files = {
        "UAF_RAND": "world/uaf.rand",
        "ROOMS": "world/text/rooms/",
        "LOG_FILE": "mud_syslog",
        "BAN_FILE": "banned_file",
        "NOLOGIN": "nologin",
        "RESET_T": "world/reset_t",
        "RESET_N": "world/reset_n",
        "RESET_DATA": "world/reset_data",
        "MOTD": "world/text/motd",
        "GWIZ": "world/text/gwiz",
        "HELP1": "world/text/help1",
        "HELP2": "world/text/help2",
        "HELP3": "world/text/help3",
        "WIZLIST": "world/text/wiz.list",
        "CREDITS": "world/text/credits",
        "EXAMINES": "world/examines/",
        "LEVELS": "world/text/level.txt",
        "PFL": "world/user_file",
        "PFT": "world/user_file.b",
        "EXE": "mudexe.py",
        "EXE2": "mud1.py",
        "SNOOP": "world/snoop/",
    }

    for k in files.keys():
        config()[k] = "%s/%s" % (path, files[k])

    config()["HOST_MACHINE"] = socket.gethostname()
    config().save()


filename = "files.yml"

if __name__ == "__main__":
    import sys

    try:
        filename = sys.argv[1]
    except IndexError:
        pass

    install()
    config().load()
    print(config())
