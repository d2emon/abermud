from config import SERVER
import requests
from .errors import LoginError
from datetime import datetime
from humanize import naturaltime


def sendWithErrors(response):
    # print(r)
    data = response.json()
    errors = data.get('errors', dict())
    if errors:
        for error in errors:
            print("%s\t%s" % (error, errors[error].get('msg')))
            # print(errors[e])
    # print(response)
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


def prepareCreated(created):
    if not created:
        return naturaltime(0)

    dateformat = '%Y-%m-%dT%H:%M:%S.%fZ'
    created_date = datetime.strptime(created, dateformat)
    return naturaltime(datetime.now() - created_date)


def prepareStarted(started):
    if started:
        return naturaltime(datetime.now() - started)
    return "AberMUD has yet to ever start!!!"


def mudStats():
    try:
        data, errors = sendWithErrors(requests.get(SERVER + '/stats'))
    except requests.exceptions.ConnectionError as err:
        print(err)
        data = dict()

    created = data.get('created')
    started = data.get('reset')
    return prepareCreated(created), prepareStarted(started)
