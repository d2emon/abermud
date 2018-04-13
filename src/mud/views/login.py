from d2log import mud_logger as logger
from .utils import cls, input_username, input_password
from models.user.models import User


TRIES = 3


def is_banned():
    '''
    Check if banned first
    '''
    b = User.chkbnid(User.host())
    # cuserid(NULL));
    logger.debug("BANNED %d", b)


def authenticate(user):
    '''
    Main login code
    '''
    tries = TRIES
    while tries:
        try:
            prompt = "This user already exists, what is the password? "
            return user.check_password(input_password(prompt))
        except AssertionError as e:
            print(e)
            tries -= 1
        assert tries > 0, "Wrong password!"
    return True


def register(user):
    '''
    this bit registers the new user
    '''
    print("Creating new user...")

    password = None
    while True:
        try:
            prompt = "Give me a password for this user "
            user.password = input_password(prompt)
            break
        except AssertionError as e:
            print(e)
    user.save()
    return True


def login(username=None):
    '''
    Does all the login stuff
    The whole login system is called from this
    '''
    is_banned()

    user = User.by_username(username)
    if user:
        authenticate(user)
        return user

    # Get the user name
    while not user:
        user, username = input_username(username)

    if user.id:
        # Password checking
        authenticate(user)
    else:
        register(user)
    cls()
    return user
