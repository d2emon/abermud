from .noserver import NoServer
from config import CONFIG
from mud.errors import LoginError

import requests


class Server(NoServer):
    def __init__(self, config=dict()):
        NoServer.__init__(self, config)
        self.host = self.config.get('SERVER')

    def make_url(self, url, **kwargs):
        full = self.host + url
        if len(kwargs):
            full += '?'
        for (key, value) in enumerate(kwargs):
            print(key, value)
        return full

    def sendWithErrors(self, response):
        data = response.json()
        errors = data.get('errors', dict())
        if errors:
            for error in errors:
                print("%s\t%s" % (error, errors[error].get('msg')))
        return data, errors

    def stats(self):
        try:
            data, errors = sendWithErrors(requests.get(SERVER + '/stats'))
        except requests.exceptions.ConnectionError as err:
            print(err)
            data = dict()
        return data

    def findUser(self, username):
        # Check name
        user = {
            'uid': None,
            'username': username,
            'password': None
        }
        print("\tTrying to find \"%s\"" % (user['username']))
        data, errors = sendWithErrors(requests.get(
            self.make_url('/user', username=user.get('username'))
        ))
        if len(errors):
            raise LoginError
        # user['data'] = data
        user['user'] = data.get('user')
        return user


    def addUser(self, username, password):
        user = {
            'uid': None,
            'username': username,
            'password': password
        }
        print("\tTrying to add \"%s\"" % (user['username']))
        data, errors = sendWithErrors(requests.post(self.make_url('/login'), user))
        if len(errors):
            raise LoginError
        return data


    def login(self, username, password):
        user = {
            'uid': None,
            'username': username,
            'password': password
        }
        print("\tTrying to login as \"%s\"" % (user['username']))
        data, errors = sendWithErrors(requests.post(self.make_url('/login'), user))
        if len(errors):
            raise LoginError
        return data

    pass
