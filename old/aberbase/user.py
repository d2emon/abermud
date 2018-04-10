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


import aberbase

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


class User(aberbase.AberDb):
    def __init__(self, **fields):
        aberbase.AberDb.__init__(self, **fields)

        import os
        self.uid = os.getlogin()

    def database(self):
        import aberbase.files
        return aberbase.files.config().PFL

    # Fields

    @property
    def index(self):
        return self.username

    def setUsername(self, username):
        self.username = username[:15].replace(" ", "")
        return self.validate_username()

    def setPassword(self, password):
        self.password = password
        return self.validate_password()

    # Validators
    def validate_username(self):
        # test user
        import re
        if not self.username:
            raise ValueError("No user name")
        if re.match('^[\w]+$', self.username) is None:
            raise ValueError("Illegal characters in user name")

        # validate user
        import aberbase.utils
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

        import aberbase.utils
        if len(self.password) not in range(1, 10):
            raise ValueError("Too long password")
        if " " in self.password:
            raise ValueError("Spaces in password")
        if aberbase.utils.fobn(self.username):
            raise ValueError("I can't call you that , It would be confused with an object")
        return True

    # Tests
    def is_authorized(self, password):
        return password == self.password

    def is_banned(self):
        """
        Check to see if UID in banned list
        """
        import aberbase.ban
        return self.uid.lower() in aberbase.ban.banned()

    def login(self):
        if self.is_banned():
            raise Exception("I'm sorry- that userid has been banned from the Game")
