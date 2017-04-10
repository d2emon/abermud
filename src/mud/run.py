import os
import logging
import socket
import yaml

import config



from datetime import datetime

from d2lib import cuserid, printfile
from mud.utils import getty, cls, crapup
from mud.talker import talker
from user.models import User
from user.login import chknolog, login, authenticate
from getpass import getpass


# include "files.h"
# include <stdio.h>
# include <sys/types.h>
# include <sys/stat.h>
# include "System.h"


# char lump[256];
namegiv = False
namegt = None
qnmrq = False
FILES = dict()
# char usrnam[44];


def time_created():
    try:
        created = os.path.getmtime(FILES["EXE"])
        return datetime.fromtimestamp(space).strftime("%x %X")
    except:
        return "<unknown>"


def time_elapsed():
    import humanize
    a = FILES["RESET_N"]
    try:
        with open(a) as f:
            d = yaml.load(f)
            r = d['started']
    except:
        return "AberMUD has yet to ever start!!!"

    dt = humanize.naturaltime(datetime.now() - r)
    return "Game time elapsed: {}".format(dt)


def check_host(game_host):
    '''
    Check we are running on the correct host
    see the notes about the use of flock();
    and the affects of lockf();
    '''
    user_host = socket.gethostname()
    assert user_host == game_host, "AberMUD is only available on {}, not on {}".format(game_host, user_host)


def show_title():
    '''
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    '''
    cls()
    print("""
                     A B E R  M U D

              By Alan Cox, Richard Acott Jim Finnis

    This AberMUD was created: {}
    {}
    """.format(time_created(), time_elapsed()))


def show_motd():
    '''
    list the message of the day
    '''
    cls()
    printfile(FILES['MOTD'])
    getpass("")
    print("\n\n")


def main(*argv):
    '''
    The initial routine
    '''
    global FILES
    FILES = config.load()

    check_host(FILES['HOST_MACHINE'])

    # Check if there is a no logins file active
    print("\n\n\n\n")
    chknolog()

    user = None
    if len(argv) > 1:
        arg = argv[1].upper()
    else:
        arg = ' '

    if arg[0] == '-':
        # Now check the option entries
        # -n(name)
        key = arg[1]
        if key == 'N':
            user = User.by_username(arg[2:])
            authenticate(user)
            user.qnmrq = True
            user.ttyt = 0
        else:
            getty()
    else:
        getty()

    if user is None:
        show_title()
        user = login()

    if not user.qnmrq:
        show_motd()

    # Log entry
    logging.info("Game entry by %s : UID %s", user, os.getuid())

    # Run system
    talker(user)

    # Exit
    crapup("Bye Bye")


# void getunm(name)
# void showuser()
# long shu(name,block)  /* for show user and edit user */
# void deluser()
# void edituser()
# void ed_fld(name,string)
# void delu2(name)   /* For delete and edit */
# void chpwd(user)   /* Change your password */
