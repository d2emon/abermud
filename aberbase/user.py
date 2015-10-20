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


# Some tests for logging in
# WrongHostException
# NoLoginException
# BannedException
# NoPersonaFileException


def startup_test():
    import socket
    test_host(socket.gethostname())
    test_nologin()
    return True


def test_host(local):
    """
    Check we are running on the correct host
    see the notes about the use of flock();
    and the affects of lockf();
    """
    import aberbase.files

    host = aberbase.files.config().HOST_MACHINE
    if local != host:
        raise Exception("AberMUD is only available on %s, not on %s\n" % (host, local))


def test_nologin():
    """
    Check if there is a no logins file active
    """
    import aberbase.files

    try:
        e = ""
        with open(aberbase.files.config().NOLOGIN, "r") as f:
            for s in f:
                e += s
        raise Exception(e)
    except OSError:
        pass
    return True


def getDatabase():
    import aberbase.files
    return aberbase.files.config().PFL


def install():
    with open(getDatabase(), "w+") as f:
        pass


class User:
    uid = ""
    username = ""
    password = ""
    namegive = False

    def __init__(self, **fields):
        import os

        self.username = fields.get("username", "")
        self.password = fields.get("password", "")
        self.uid = fields.get("uid", os.getuid())

        self.namegive = (self.username == True)

    def load(self, username):
        """
        Return block data for user or -1 if not exist
        """
        try:
            with open(getDatabase(), "r") as f:
                for s in f:
                    self.decode(s)
                    if self.username.lower() == username.lower():
                        return True
        except OSError:
            raise Exception("No persona file")
        self.username = username
        return False

    def save(self):
        try:
            with open(getDatabase(), "a+") as f:
                f.write("%s\n" % (self.encode()))
        except OSError:
            raise Exception("No persona file....\n")

    def validate_username(self):
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
        if not self.password:
            raise ValueError("No password")
        if re.match('^[\w]+$', self.password) is None:
            raise ValueError("Illegal characters in password")
        return True

    def setUsername(self, username):
        self.username = username[:15].replace(" ", "")
        return self.validate_username()

    def setPassword(self, password):
        self.password = password
        return self.validate_password()

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

    def test_password(self, password):
        return password == self.password

    def test_banned(self):
        """
        Check to see if UID in banned list
        """
        import aberbase.files
        try:
            with open(aberbase.files.config().BAN_FILE, "r") as f:
                for s in f:
                    if s.rstrip("\n").lower() == self.uid.lower():
                        raise Exception("I'm sorry- that userid has been banned from the Game")
        except OSError:
            pass
        return True
