from config import CONFIG
from .base import BaseServer
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
    def host_decorator(func):
        def func_wrapper(*args, **kwargs):
            if host is None:
                host = CONFIG.get('HOST_MACHINE')
            # assert User.host() == host, "AberMUD is only available on {}, not on {}".format(host, User.host())
            func_wrapper(*args, **kwargs)
        return func
    return host_decorator


def check_nologin(func):
    '''
    Check if there is a no logins file active
    '''
    def func_wrapper(*args, **kwargs):
        try:
            with open(CONFIG.get("NOLOGIN")) as a:
                s = a.read()
                print(s)
            sys.exit(0)
        except:
            func_wrapper(*args, **kwargs)
        print(func)
    return func


class NoServer(BaseServer):
    @check_host()
    @check_nologin
    def stats(self):
        def created():
            try:
                created = os.path.getmtime(self.config.get("EXE"))
                return datetime.fromtimestamp(created)
            except:
                return None

        def elapsed():
            a = self.config.get("RESET_N")
            try:
                with open(a) as f:
                    d = yaml.load(f)
                    r = d['started']
            except:
                return None
            return datetime.now() - r

        return {
            'created': created(),
            'elapsed': elapsed(),
        }
