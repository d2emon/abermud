from d2log import mud_logger as logger
from models.user.models import User
from getpass import getpass


def cls():
    print("=-" * 40)
    print("\n" * 24)


def askYN(prompt="(Y/N)?"):
    answer = input(prompt).lower()
    return answer[0] == 'y'


def input_username(username, prompt="By what name shall I call you?\n*\t"):
    if not username:
        username = input(prompt)[:15]

    # user = load_user(username)
    # if not user:
    #     user = new_user(username)
    # return user
    return load_user(username) or new_user(username)


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
    if askYN("Did I get the name right {}? ".format(username)):
        return User(username=username)
    return None
