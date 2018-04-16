from config import CONFIG
# from .user.models import User
from datetime import datetime
from humanize import naturaltime

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


class NoServer:
    def __init__(self, config=dict()):
        self.config = config


    def check_nologin(self):
        '''
        Check if there is a no logins file active
        '''
        try:
            with open(self.config.get("NOLOGIN")) as a:
                s = a.read()
            print(s)
        except:
            return
        sys.exit(0)

    @check_host
    def can_login(self):
        self.check_nologin()


    def time_created():
        try:
            created = os.path.getmtime(self.config.get("EXE"))
            return datetime.fromtimestamp(created)
        except:
            return None


    def time_elapsed():
        a = self.config.get("RESET_N")
        try:
            with open(a) as f:
                d = yaml.load(f)
                r = d['started']
        except:
            return None

        return datetime.now() - r


    def stats():
        can_login()
        return {
            'created': time_created(),
            'elapsed': time_elapsed(),
            }


    def mudStats(self):
        # try:
        #     data, errors = sendWithErrors(requests.get(SERVER + '/stats'))
        # except requests.exceptions.ConnectionError as err:
        #     print(err)
        #     data = dict()

        data = stats()
        return self.prepareCreated(data.get('created')), self.prepareStarted(data.get('elapsed'))


    def prepareCreated(created):
        if not created:
            return "<unknown>"

        # dateformat = '%Y-%m-%dT%H:%M:%S.%fZ'
        # created_date = datetime.strptime(created, dateformat)
        # return naturaltime(datetime.now() - created_date)
        return created.strftime("%x %X")

    def prepareStarted(started):
        if started:
            return "Game time elapsed: {}".format(
                humanize.naturaltime(started)
            )
        return "AberMUD has yet to ever start!!!"
