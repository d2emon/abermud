from config import CONFIG
# from .user.models import User
from datetime import datetime

import os
import sys
import yaml


def check_host(host=None):
    '''
    Check we are running on the correct host
    see the notes about the use of flock();
    and the affects of lockf();
    '''
    if host is None:
        host = CONFIG.get('HOST_MACHINE')
    # assert User.host() == host, "AberMUD is only available on {}, not on {}".format(host, User.host())


def check_nologin():
    '''
    Check if there is a no logins file active
    '''
    try:
        with open(CONFIG.get("NOLOGIN")) as a:
            s = a.read()
        print(s)
    except:
        return
    sys.exit(0)


def test_login():
    check_host()
    check_nologin()


def time_created():
    try:
        created = os.path.getmtime(CONFIG.get("EXE"))
        return datetime.fromtimestamp(created)
    except:
        return None


def time_elapsed():
    a = CONFIG.get("RESET_N")
    try:
        with open(a) as f:
            d = yaml.load(f)
            r = d['started']
    except:
        return None

    return datetime.now() - r


def stats():
    test_login()
    return {
        'created': time_created(),
        'elapsed': time_elapsed(),
    }
