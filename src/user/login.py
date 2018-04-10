from config import CONFIG
from d2log import mud_logger as logger
from mud.utils import cls
# from user.models import User
from user.models import User
from getpass import getpass


TRIES = 3


def input_username(username, prompt="By what name shall I call you?\n*\t"):
    if not username:
        username = input(prompt)[:15]

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


def input_password(prompt='Password: '):
    return getpass(prompt)


def login(username=None):
    '''
    Does all the login stuff
    The whole login system is called from this
    '''
    # Check if banned first
    b = User.chkbnid(User.host())
    # cuserid(NULL));
    logger.debug("BANNED %d", b)

    if username:
        username = username.lower()

    user = User.by_username(username)
    if user:
        authenticate(user)
        return user

    # Get the user name
    user = None
    while not user:
        user = input_username(username)
        username = ''

    if user.id:
        # Password checking
        authenticate(user)
    else:
        register(user)
    cls()
    return user


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


def chknolog():
    try:
        with open(CONFIG["NOLOGIN"]) as a:
            s = a.read()
        print(s)
    except:
        return

    import sys
    sys.exit(0)


def search():
    import db
    engine, session = db.connect()
    users = session.query(User).all()
    for u in users:
        print("{}:\t{}".format(u.id, u.username))
    return input("\nUser Name: ")


def show(username):
    user = User.by_username(username)
    if user is None:
        print("\nNo user registered in that name\n\n")
    else:
        print("\n\nUser Data For {}\n".format(user.username))
        print("Name: {}\nPassword: {}\n".format(user.username, user.password))
    return user


def edit_field(title, value):
    new_value = input("{}(Currently {}): ".format(title, value))

    if not new_value:
        new_value = value
    return new_value


def change_password(user):
    try:
        data = input_password("\nOld Password\n*\t")
        assert data == user.password, "Incorrect Password"
    except AssertionError as e:
        print(e)
        return

    while True:
        try:
            password = input_password("\nNew Password\n*\t")
            verify = input_password("\nVerify Password\n*\t")
            assert verify == password, "Passwords doesn't match"
            user.password = password
        except AssertionError as e:
            print(e)
            continue
        break
    user.save()
    print("Changed")
    return
