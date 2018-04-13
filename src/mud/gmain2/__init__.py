from d2log import mud_logger as logger

from .cli import inputUser, loadUser, newUser
from mud.errors import ArgsError
from mud.utils import uid
from mud.views import cls, start, motd
# from ..talker import talker
from models.user.login import login  # , authenticate


def login_vars(username=None):
    user = login(username)
    if username is not None:
        user.ttyt = 0
    return user


def login1(username):
    username, user = inputUser(username)
    cls()
    print(username, user)
    if user is None:
        return newUser(username)
    else:
        return loadUser(username)


def talker(user):
    # Log entry
    logger.info("Game entry by %s : UID %s", user.username, uid())

    # Run system
    # talker(user)
    print(user)
    # return talker(user) // Run system


def main(username=None, args=dict(), **kwargs):
    '''
    The initial routine
    '''
    print("GMAIN2.PY MAIN()", args, kwargs, username)
    show = username is None
    start(show)

    user = login_vars(username)
    # user = login(username)

    motd(show)
    talker(user)
