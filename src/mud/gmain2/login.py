from config import SERVER
import requests
from mud.errors import LoginError
from datetime import datetime


def sendWithErrors(response):
    data = response.json()
    errors = data.get('errors', dict())
    if errors:
        for error in errors:
            print("%s\t%s" % (error, errors[error].get('msg')))
    return data, errors


def findUser(username):
    # Check name
    user = {
        'uid': None,
        'username': username,
        'password': None
    }
    print("\tTrying to find \"%s\"" % (user['username']))
    data, errors = sendWithErrors(requests.get(
      SERVER + '/user?username=' + user.get('username')
    ))
    if len(errors):
        raise LoginError
    # user['data'] = data
    user['user'] = data.get('user')
    return user


def addUser(username, password):
    user = {
        'uid': None,
        'username': username,
        'password': password
    }
    print("\tTrying to add \"%s\"" % (user['username']))
    data, errors = sendWithErrors(requests.post(SERVER + '/login', user))
    if len(errors):
        raise LoginError
    return data


def login(username, password):
    user = {
        'uid': None,
        'username': username,
        'password': password
    }
    print("\tTrying to login as \"%s\"" % (user['username']))
    data, errors = sendWithErrors(requests.post(SERVER + '/login', user))
    if len(errors):
        raise LoginError
    return data
