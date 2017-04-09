import socket
import os
import config
from d2lib import cuserid
from mud.utils import getty, cls
from datetime import datetime
from user.models import User
from user.login import login
import yaml


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


def elapsed():
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


def main(*argv):
    '''
    The initial routine
    '''
    global FILES
    FILES = config.load()

    namegiv = False
    namegt = ""
    qnmrq = False
    # FILE *a;

    # Check we are running on the correct host
    # see the notes about the use of flock();
    # and the affects of lockf();
    user = socket.gethostname()
    if user != FILES["HOST_MACHINE"]:
        raise Exception("AberMUD is only available on {}, not on {}".format(FILES["HOST_MACHINE"], user))
    b = [0, 0, 0]

    # Check if there is a no logins file active
    print("\n\n\n\n")
    chknolog()
    if len(argv) > 1:
        arg = argv[1].upper()
    else:
        arg = ' '

    if arg[0] == '-':
        # Now check the option entries
        # -n(name)
        key = arg[1]
        if key == 'N':
            qnmrq = True
            ttyt = 0
            namegt = arg[2:]
            namegiv = True
        else:
            getty()
    else:
        getty()

    num = 0
    # Check for all the created at stuff
    # We use stats for this which is a UN*X system call
    if not namegiv:
        cls()
        try:
            space = os.path.getmtime(FILES["EXE"])
            space = datetime.fromtimestamp(space).strftime("%x %X")
        except:
            space = "<unknown>"
        ta = elapsed()

        print("""
                         A B E R  M U D

                  By Alan Cox, Richard Acott Jim Finnis

        This AberMUD was created: {}
        {}
        """.format(space, ta))

    login(username=namegt)
    # Does all the login stuff

    if not qnmrq:
        cls()
        # listfl(MOTD);             /* list the message of the day */
        space = input("399")
        print("\n\n")

    space = cuserid()
    # syslog("Game entry by %s : UID %s",user,space); /* Log entry */
    # talker(user);                /* Run system */
    crapup("Bye Bye")  # Exit


# char usrnam[44];


# void getunm(name)
# void showuser()
# long shu(name,block)  /* for show user and edit user */
# void deluser()
# void edituser()
# void ed_fld(name,string)
# void delu2(name)   /* For delete and edit */
# void chpwd(user)   /* Change your password */

# void listfl(name)


def crapup(ptr):
    input("\n{}\n\nHit Return to Continue...\n".format(ptr))

    import sys
    sys.exit(0)


def chknolog():
    try:
        with open(FILES["NOLOGIN"]) as a:
            s = a.read()
        print(s)
    except:
        return

    import sys
    sys.exit(0)
