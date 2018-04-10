from .cli import cls, splash, inputUser, loadUser, newUser
from .errors import ArgsError


def parseArgs(user=dict(), **kwargs):
    if len(kwargs) <= 0:
        return user.get('username')
    if len(kwargs) and len(kwargs) != 2:
        raise ArgsError("Must recieve only 2 args")
    username = kwargs.get('n')
    if username is None:
        raise ArgsError("Name is not set")
    # qnmrq = 1
    # # ttyt = 0
    return username


def showSplash(username):
    """
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    """
    cls()
    print("\n" * 4)
    if username:
        return
    splash()


def login(username):
    username, user = inputUser(username)
    cls()
    print(username, user)
    if user is None:
        return newUser(username)
    else:
        return loadUser(username)


def showMotd():
    print('MOTD')
    # return showMotd()


def talker(user):
    print(user)
    # return talker(user) // Run system


def main(args=dict(), **kwargs):
    '''
    The initial routine
    '''
    username = parseArgs(args, **kwargs)
    print("GMAIN2.PY MAIN()", args, kwargs, username)
    showSplash(username)
    user = login(username)
    showMotd()
    talker(user)
    print('Bye Bye!')
