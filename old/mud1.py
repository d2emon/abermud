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
            "bprintf",
            "chkname",
        ),
        "gmainstubs": (),
        "gmlnk": (),
    }
    print({"mud.1": (incl, func)})
    print("TODO: mud.1 %s" % (args))
    main1(**args)


# Program starts Here!
# This forms the main loop of the code, as well as calling
# all the initialising pieces


def main1(**params):
    """ The initial routine
    """
    import logging
    import json
    import datetime

    import aberbase
    import aberbase.files
    import aberbase.user
    import sys_stubs
    import gmlnk

    logging.basicConfig(
        # filename=logfile,
        level=logging.INFO
    )


    aberbase.user.startup_test()
    user = aberbase.user.User(username=params.get("n", ""))
    user.load_data()
    print(user)

    sys_stubs.qnmrq = user.username is not False
    show_screens = sys_stubs.qnmrq

    show_logo(
        created=aberbase.time_created(),
        started=aberbase.time_started(),
        show=show_screens,
    )

    user.login()
    if get_login(user=user):
        get_password(user=user)
    else:
        new_user(user=user)

    show_motd(
        show=sys_stubs.qnmrq,
    )

    logging.info("Game entry by %s : UID %s" % (user.username, user.uid))
    gmlnk.talker(user)
    sys_stubs.crapup("Bye Bye")


def show_logo(**params):
    """
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    """
    import sys_stubs
    if not params["show"]:
        return False
    sys_stubs.clear_console()
    print("""




                         A B E R  M U D

                  By Alan Cox, Richard Acott Jim Finnis

    This AberMUD was created: %s\n%s\n""" % (params["created"], params["started"]))
    return True


def show_motd(**params):
    import sys_stubs
    import aberbase.motd
    if not params["show"]:
        return False
    sys_stubs.clear_console()
    aberbase.motd.show()
    input("\n\n")
    return True


def get_login(**params):
    """
    Does all the login stuff
    The whole login system is called from this
    """
    user = params["user"]
    while True:
        if not user.username:
            user.username = input("By what name shall I call you ?\n")

        try:
            if user.validate_username():
                break
        except ValueError as e:
            user.username = ""
            print(e)
    return user.load(user.username)


def get_password(user):
    """
    Check name
    Password checking
    """
    import getpass
    for tries in range(0, 3):
        password = getpass.getpass("This persona already exists, what is the password ?")
        if user.test_password(password):
            return True
    raise Exception("Wrong password!")


def new_user(user):
    """
    If he/she doesnt exist
    """
    import getpass
    answer = input("Did I get the name right, %s ? " % (user.username)).lower()
    if answer[0] == 'n':
        raise Exception("Wrong name")

    print("Creating new persona...")
    while True:
        try:
            user.setPassword(getpass.getpass("Give me a password for this persona: "))
            break
        except ValueError as e:
            print(e)
    return user.save()


# getunm
# showuser
# shu
# deluser
# edituser
# ed_fld
# delu2

# bprintf
# chkname


if __name__ == "__main__":
    import sys
    params = {}
    for i, arg in enumerate(sys.argv):
        if arg[0] == '-':
            params[arg[1:].lower()] = sys.argv[i + 1]
    print(params)
    run(**params)
