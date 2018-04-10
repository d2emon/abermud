import os
import yaml

from datetime import datetime
from getpass import getpass

import config

from d2lib import printfile
from mud.utils import getty, cls, crapup
from mud.talker import talker
from user.models import User
from user.login import chknolog, login  # , authenticate

from server import check_host


# char lump[256];
namegiv = False
namegt = None
qnmrq = False
FILES = dict()
# char usrnam[44];


def time_created():
    try:
        created = os.path.getmtime(FILES["EXE"])
        return datetime.fromtimestamp(created).strftime("%x %X")
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
    CONFIG = config.load()

    global FILES
    FILES = CONFIG

    check_host(CONFIG.get('HOST_MACHINE'))

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
            username = arg[2:]
            # user = User.by_username(username)
            # print("USER is", user)
            # if user:
            #    # authenticate(user)
            # else:
            user = login(username)
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
    try:
        uid = os.getuid()
    except:
        uid = '<UID>'
    logger.info("Game entry by %s : UID %s", user.username, uid)

    # Run system
    talker(user)

    # Exit
    crapup("Bye Bye")
