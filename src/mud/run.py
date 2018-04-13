import os
import config

from .utils import getty, crapup
from .gmain2 import main as game
from .errors import ArgsError
from server import test_login


def parse_args(args):
    '''
    Now check the option entries
    '''
    test_login()

    print(args)
    if len(args) < 2:
        return getty()

    if len(args) > 2:
        raise ArgsError("Must recieve only 2 args")

    arg = args[1].upper()

    if len(arg) < 2:
        raise ArgsError("Name is not set")

    # -n(name)
    if arg[0] == '-' and arg[1] == 'N':
        # username = kwargs.get('n')
        username = arg[2:]
        # user = User.by_username(username)
        # print("USER is", user)
        # if user:
        #    # authenticate(user)
        # else:
        return username
    raise  ArgsError("Name is not set")
    # qnmrq = 1
    # # ttyt = 0


def main(*argv):
    '''
    The initial routine
    '''
    CONFIG = config.load()

    username = parse_args(argv)
    game(username)
    # Exit
    crapup("Bye Bye")
