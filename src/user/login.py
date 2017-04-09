from d2lib import cuserid
from mud.utils import cls
from user.models import User


TRIES = 3


def input_username(username):
    if not username:
        username = input("By what name shall I call you?\n*\t")[:15]

    # Check for legality of names
    try:
        user = User(username)
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
    return user


def input_password():
    # repass:
    password = input("*\t")
    # fflush(stdout)
    # gepass(block)
    print("\n")
    return password


def login(username=None, session=None):
    '''
    Does all the login stuff
    The whole login system is called from this
    '''
    if username:
        user = User(username)
        authenticate(user, session)
        return user

    # Check if banned first
    b = User.chkbnid(cuserid())
    # cuserid(NULL));
    print("BANNED", b)

    # Get the user name
    user = None
    while not user:
        user = input_username(username)

    if user.id:
        # Password checking
        authenticate(user, session)
    else:
        register(user, session)
    cls()
    return user


def authenticate(user, session=None):
    '''
    Main login code
    '''
    print("This user already exists, what is the password?")
    tries = TRIES
    while tries:
        try:
            return user.check_password(input_password())
        except AssertionError as e:
            print(e)
            tries -= 1
        assert tries > 0, "Wrong password!"
    return True


def register(user, session=None):
    '''
    this bit registers the new user
    '''
    print("Creating new user...")

    print("Give me a password for this user")
    password = None
    while True:
        try:
            user.password = input_password()
            break
        except AssertionError as e:
            print(e)
    user.save(session)
    return True


def chknolog():
    try:
        with open(FILES["NOLOGIN"]) as a:
            s = a.read()
        print(s)
    except:
        return

    import sys
    sys.exit(0)
