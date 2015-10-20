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


def talker(user):
    """
    Run system
    """
    import sys_stubs
    while True:
        if sys_stubs.qnmrq:
            if not execl("   --}----- ABERMUD -----{--    Playing as ", user.username, 0):
                crapup("mud.exe : Not found")
        sys_stubs.clear_console()
        options = {
            "1": {"wiz": False, "action": start_game, "text": "1]\tEnter The Game"},
            "2": {"wiz": False, "action": change_pwd, "text": "2]\tChange Password"},
            "0": {"wiz": False, "action": exit_mud, "text": "\n\n0]\tExit AberMUD\n"},
            "4": {"wiz": True, "action": test_mud, "text": "4]\tRun TEST game"},
            "a": {"wiz": True, "action": showuser, "text": "A]\tShow persona"},
            "b": {"wiz": True, "action": edituser, "text": "B]\tEdit persona"},
            "c": {"wiz": True, "action": deluser, "text": "C]\tDelete persona"},
        }
        items = [
            options["1"],
            options["2"],
            options["0"],
            options["4"],
            options["a"],
            options["b"],
            options["c"],
        ]
        is_wizard = (user.uid == "wisner")
        print("Welcome To AberMUD II [Unix]\n\n")
        print("Options\n")
        for i in items:
            if (not i["wiz"]) or is_wizard:
                print(i["text"])
        print("\n")
        option = options.get(input("Select > ")[:1],
            {"wiz": False, "action": bad_option})
        action = option.get("action", bad_option)
        can_run = (not option.get("wiz", False)) or is_wizard
        if can_run:
            if not action(user.username):
                break


def start_game(nam):
    import sys_stubs

    sys_stubs.clear_console()
    print("""The Hallway
You stand in a long dark hallway, which echoes to the tread of your
booted feet. You stride on down the hall, choose your masque and enter the
worlds beyond the known......

""")
    execl("   --{----- ABERMUD -----}--      Playing as ", nam, 0)
    sys_stubs.crapup("mud.exe: Not Found")
    return True


def change_pwd(user):
    import getpass
    print("TODO: chpwd(%s)" % (user))

    data = user
    # logscan(user, block)
    user = data
    # a = scan(data, block, 0, "", ".")
    # a = scan(pwd, block, a+1, "", ".")
    data = getpass.getpass("\nOld Password\n*")
    if data == pwd:
        print("\nIncorrect Password")
    else:
        print("\nNew Password")
        # chptagn:
        pwd = getpass.getpass("*")
        print("")
        if not pwd:
            pass
            # goto chptagn
        if '.' in pwd:
            print("Illegal Character in password")
            # goto chptagn;
        pv = getpass.getpass("\nVerify Password\n*")
        print("\n")
        if pv == pwd:
            print("\nNO!")
            # goto chptagn
        block = "%s%s%s%s%s%s%s%s" % (user,".",pwd,".",".",".",".",".")
        print(block)
        # delu2(user)

        # delete me and tack me on end!

        # try:
        #    with open(PFL, "a") as fl:
        #        block = qcrypt(lump)
        #        block = lump
        #        fprintf(fl,"%s\n",block);
        # except OsError:
        #    pass
        print("Changed")
    return True


def exit_mud(nam):
    return False


def test_mud(nam):
    sys_stubs.clear_console()
    print("Entering Test Version");
    return True


def showuser(nam):
    print("TODO: showuser(%s)" % (nam))
    return True


def edituser(nam):
    print("TODO: edituser(%s)" % (nam))
    return True


def deluser(nam):
    print("TODO: deluser(%s)" % (nam))
    return True


def execl(*args):
    import aberbase.files
    import mudexe

    print(aberbase.files.config().EXE + "%s %s %s" % args)
    mudexe.run()
    return True


def bad_option(nam):
    print("Bad Option")
    return True
