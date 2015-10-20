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


def getDatabase():
    import aberbase.files
    return aberbase.files.config().PFL


def install():
    with open(getDatabase(), "w+") as f:
        pass

class User:
    username = ""
    password = ""

    def __init__(self, **fields):
        self.username = fields.get("username", "")
        self.password = fields.get("password", "")

    def load(self, username):
        """
        Return block data for user or -1 if not exist
        """
        try:
            # unit=openlock(PFL,"r");f=0;
            with open(getDatabase(), "r") as f:
                for s in f:
                    self.decode(s)
                    if self.username.lower() == username.lower():
                        return True
        except OSError:
            raise Exception("No persona file")
        return False

    def save(self):
        try:
            # fl=openlock(PFL,"a");
            with open(getDatabase(), "a+") as f:
                f.write("%s\n" % (self.encode()))
        except OSError:
            raise Exception("No persona file....\n")

    def validiate_username(self):
        import aberbase.utils
        import re

        # test user
        if not self.username:
            raise ValueError("No user name")
        if re.match('^[\w]+$', self.username) is None:
            raise ValueError("Illegal characters in user name")

        # validate user
        if aberbase.utils.resword(self.username):
            raise ValueError("Sorry I cant call you that")
        if len(self.username) not in range(1, 10):
            raise ValueError("Too long name")
        if " " in self.username:
            raise ValueError("Spaces in name")
        if aberbase.utils.fobn(self.username):
            raise ValueError("I can't call you that , It would be confused with an object")
        return True

    def validate_password(self):
        import re
        if not password:
            raise ValueError("No password")
        if re.match('^[\w]+$', password) is None:
            raise ValueError("Illegal characters in password")
        return True

    def encode(self):
        import json
        return json.dumps({
            "user": self.username,
            "password": self.password
        })

    def decode(self, data):
        import json
        parsed = json.loads(data)
        self.username = parsed["user"]
        self.password = parsed["password"]
        return parsed
