from models.user.models import User
from getpass import getpass


def cls():
    print("=-" * 40)
    print("\n" * 24)


def input_username(username, prompt="By what name shall I call you?\n*\t"):
    if not username:
        username = input(prompt)[:15]

    # Check for legality of names
    try:
        user = User(username.lower())
    except AssertionError as e:
        print(e)
        return None

    user = User.by_username(username)
    if user:
        return user

    # If he/she doesnt exist
    answer = input("Did I get the name right {}? ".format(username)).lower()
    if answer[0] == 'y':
        user = User(username=username)
    return user, ''


def input_password(prompt='Password: '):
    return getpass(prompt)
