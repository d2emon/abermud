import os
import config

from d2log import mud_logger as logger
from .views import start, motd
from .utils import getty, crapup
from .talker import talker
from user.login import login  # , authenticate

from server import test_login


# char lump[256];
# char usrnam[44];


def parse_args(args):
    '''
    Now check the option entries
    '''
    if len(args) < 2:
        return None

    arg = args[1].upper()

    if len(arg) < 2:
        return None

    # -n(name)
    if arg[0] == '-' and arg[1] == 'N':
        username = arg[2:]
        # user = User.by_username(username)
        # print("USER is", user)
        # if user:
        #    # authenticate(user)
        # else:
        return username
    return None


def login_vars(username=None):
    user = login(username)
    if username is not None:
        user.ttyt = 0
    return user


def uid():
    try:
        id = os.getuid()
    except:
        id = '<UID>'
    return id


def main(*argv):
    '''
    The initial routine
    '''
    CONFIG = config.load()

    print("\n\n\n\n")
    test_login()

    username = parse_args(argv)

    if username is None:
        username = getty()
        showSplash = True
    else:
        showSplash = False

    start(showSplash)
    user = login_vars(username)
    if showSplash:
        motd(showSplash)

    # Log entry
    logger.info("Game entry by %s : UID %s", user.username, uid())

    # Run system
    talker(user)

    # Exit
    crapup("Bye Bye")
