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


def run(**args):
    incl = (
        # "object.h",
        # "System.h",
        "blib.o",
        # "obdat.o",
    )
    func = {
        "gmain2": (
            "getunm",
            "showuser",
            "shu",
            "deluser",
            "edituser",
            "ed_fld",
            "delu2",
            "chpwd",
            "bprintf",
            "chkname",
        ),
        "gmainstubs": (),
        "gmlnk": (
            "talker",
        ),
    }
    print({"mud.1": (incl, func)})
    print("TODO: mud.1i %s" % (args))

    main1(**args)

    import mudexe
    mudexe.run()


lump = ""
namegt = ""

namegiv = False
qnmrq = 0


# Program starts Here!
# This forms the main loop of the code, as well as calling
# all the initialising pieces

# argn = argv[1].upper()
# r = argn[0]
# Now check the option entries
# -n(name)


def main1(**params):
    """ The initial routine
    """
    import aberbase.files
    import sys_stubs
    import os
    global namegiv
    global qnmrq

    num = 0

    test_host()
    test_nologin()

    namegt = params.get("N", "")
    if namegt:
        qnmrq = 1
        ttyt = 0
        namegiv = True

    if not namegiv:
        show_logo()

    user = login(namegt)

    if not qnmrq:
        sys_stubs.clear_console()
        listfl(aberbase.files.config().MOTD)  # list the message of the day
        input()
        print("\n\n")
    uid = os.getlogin()
    syslog("Game entry by %s : UID %s" % (user, uid))  # Log entry
    talker(user)  # Run system
    crapup("Bye Bye")  # Exit


def talker(u):
    print("TODO: talker(%s)" % (u))


def syslog(t):
    print("TODO: syslog(%s)" % (t))


def show_logo():
    """
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    """
    import aberbase.files
    import os
    import time
    import datetime
    import json
    import sys_stubs

    created = time.ctime(os.path.getmtime(aberbase.files.config().EXE))
    try:
        current = datetime.datetime.now() - json.load(open(aberbase.files.config().RESET_N, "r"))
        started = "Game time elapsed: %s" % (elapsed(current))
    except OSError:
        started = "AberMUD has yet to ever start!!!"

    sys_stubs.clear_console()
    print("""




                         A B E R  M U D

                  By Alan Cox, Richard Acott Jim Finnis

    This AberMUD was created: %s\n%s\n""" % (created, started))


def elapsed(delta):
    """
    Elapsed time and similar goodies
    """
    if delta.days > 1:
        return "Over a day!!!"

    parts = []
    hour = 60 * 60
    hours = delta.seconds // hour
    seconds = delta.seconds % hour
    minutes = seconds // (60)

    if hours > 1:
        parts.append("%d hours" % (hours))
    elif hours == 1:
        parts.append("1 hour")

    if minutes > 1:
        parts.append("%d minutes" % (minutes))
        return " and ".join(parts)
    elif minutes == 1:
        parts.append("1 minute")

    seconds = (delta.seconds % 60)
    if seconds > 1:
        parts.append("%d seconds" % (seconds))
    elif seconds == 1:
        parts.append("1 second")

    return " and ".join(parts)


# Some tests for logging in
# WrongHostException
# NoLoginException
# BannedException
# NoPersonaFileException


def test_host():
    """
    Check we are running on the correct host
    see the notes about the use of flock();
    and the affects of lockf();
    """
    import socket
    import aberbase.files

    local_host = socket.gethostname()
    right_host = aberbase.files.config().HOST_MACHINE
    if local_host != right_host:
        raise Exception("AberMUD is only available on %s, not on %s\n" % (right_host, local_host))


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
        return True


def test_banned(user):
    """
    Check to see if UID in banned list
    """
    import aberbase.files
    try:
        # a=openlock(BAN_FILE, "r+")
        with open(aberbase.files.config().BAN_FILE, "r") as f:
            for s in f:
                if s.rstrip("\n").lower() == user.lower():
                    raise Exception("I'm sorry- that userid has been banned from the Game")
    except OSError:
        pass
    return True


usrnam = ""


def login(namegt=""):
    """
    Does all the login stuff
    The whole login system is called from this
    """
    import os
    import aberbase.user
    global namegiv

    # Check if banned first
    test_banned(os.getlogin())

    # Get the user name
    if namegiv:
        user = namegt
    u = aberbase.user.User()
    unnamed = True
    while unnamed:
        if not namegiv:
            user = input("By what name shall I call you ?\n")[:15].replace(" ", "")

        # Check for legality of names
        namegiv = False

        try:
            u.username = user
            unnamed = not u.validiate_username()
        except ValueError as e:
            print(e)
            continue

        break
    if u.load(username=user):
        logpass(u)
    else:
        new_user(u)


def logpass(user):
    """
    Check name
    Password checking
    """
    import sys_stubs
    import getpass

    if not user:
        return False

    for tries in range(0, 3):
        sys_stubs.clear_console()
        pwd = getpass.getpass("This persona already exists, what is the password ?")
        sys_stubs.clear_console()
        if pwd == user.password:
            return True
    crapup("\nNo!\n\n")


def new_user(u):
    """
    If he/she doesnt exist
    """
    import sys_stubs
    import getpass

    answer = input("\nDid I get the name right, %s ?" % (u.username))
    if answer.lower()[0] == 'n':
        return False

    # this bit registers the new user
    print("Creating new persona...\n")
    print("Give me a password for this persona\n")
    while True:
        try:
            sys_stubs.clear_console()
            u.password = getpass.getpass("*")
            u.validate_password()
            break
        except ValueError as e:
            print(e)
            continue
    return u.save()


# getunm
# showuser
# shu
# deluser
# edituser
# ed_fld
# delu2
# chpwd

def listfl(name):
    try:
        with open(name, "r+") as f:
            # unit=openlock(name,"r+");
            print(f.read())
    except OSError:
        print("[Cannot Find -> %s]\n" % (name))


def crapup(ptr):
    import sys

    input("\n%s\n\nHit Return to Continue...\n" % (ptr))
    sys.exit(1)


# bprintf
# chkname


if __name__ == "__main__":
    import sys
    params = {}
    for i, arg in enumerate(sys.argv):
        if arg[0] == '-':
            params[arg[1:]] = sys.argv[i + 1]
    print(params)
    run(**params)
