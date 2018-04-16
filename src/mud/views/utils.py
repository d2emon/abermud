from d2log import mud_logger as logger
from models.user.models import User
from getpass import getpass


def cls():
    print("=-" * 40)
    print("\n" * 24)


def input_username(username, prompt="By what name shall I call you?\n*\t"):
    if not username:
        username = input(prompt)[:15]

    user = load_user(username)
    print("LOADED", user)
    if not user:
        user = new_user(username)
    return user


def input_password(prompt='Password: '):
    return getpass(prompt)


def load_user(username):
    '''
    Check for legality of names
    '''
    try:
        return User.by_username(username)
    except AssertionError as e:
        print(e)
        return None


def new_user(username):
    '''
    If he/she doesnt exist
    '''
    answer = input("Did I get the name right {}? ".format(username)).lower()
    if answer[0] == 'y':
        user = User(username=username)
    user = None
    return User.by_username(username)
