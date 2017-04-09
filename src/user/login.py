from d2lib import cuserid
from mud.utils import cls
from user.models import User


def input_username(username):
    if not username:
        username = input("By what name shall I call you?\n*\t")[:15]

    # Check name
    user = User(username)
    if not user.get_username(username):
        return False, None

    user = User.by_username(username)
    if user is not None:
        return True, user

    # If he/she doesnt exist
    answer = input("Did I get the name right {}? ".format(username)).lower()
    # print("\n")
    if answer[0] == 'y':
        user = User(username=username)
    return False, user


def login(username=None, session=None):
    '''
    The whole login system is called from this
    '''
    # Check if banned first
    b = User.chkbnid(cuserid())
    # cuserid(NULL));
    print("BANNED", b)

    user = User()
    logged = None
    print("LOGIN({})".format(username))
    while not logged:
        # Get the user name
        exists, logged = input_username(username)
        print("USER", user, exists, logged)

    user = logged
    # Password checking
    print("LOGGED USER", user)
    if user and user.id:
        user.authenticate(session)
    else:
        User.register(username, session)
    cls()
