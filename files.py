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


def load():
    import yaml

    global _data

    with open(filename, 'r') as f:
        _data = yaml.load(
            f.read(),
        )


def save():
    import yaml

    with open(filename, 'w+') as f:
        f.write(yaml.dump(
            _data,
            default_flow_style = False,
        ))


def install():
    import os
    import socket

    global _data

    files = {
        "UAF_RAND": "uaf.rand",
        "ROOMS": "TEXT/ROOMS/",
        "LOG_FILE": "mud_syslog",
        "BAN_FILE": "banned_file",
        "NOLOGIN": "nologin",
        "RESET_T": "reset_t",
        "RESET_N": "reset_n",
        "RESET_DATA": "reset_data",
        "MOTD": "TEXT/gmotd2",
        "GWIZ": "TEXT/gwiz",
        "HELP1": "TEXT/help1",
        "HELP2": "TEXT/help2",
        "HELP3": "TEXT/help3",
        "WIZLIST": "TEXT/wiz.list",
        "CREDITS": "TEXT/credits",
        "EXAMINES": "EXAMINES/",
        "LEVELS": "TEXT/level.txt",
        "PFL": "user_file",
        "PFT": "user_file.b",
        "EXE": "mud.exe",
        "EXE2": "mud.1",
        "SNOOP": "SNOOP/",
    }
    path = os.path.dirname(os.path.abspath(__file__))

    for k in files.keys():
        _data[k] = "%s/%s" % (path, files[k])

    _data["HOST_MACHINE"] = socket.gethostname()
    save()


filename = "files.yml"
_data = {}

if __name__ == "__main__":
    import sys

    try:
        filename = sys.argv[1]
    except IndexError:
        pass

    install()
    load()
    print(_data)
