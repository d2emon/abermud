from config import CONFIG
from d2lib import printfile
from getpass import getpass
from .utils import cls
from server import Server


def start(show=True, server=None):
    '''
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    '''
    cls()
    print("\n" * 4)
    if not show:
        return

    if not server:
        server = Server()

    if server:
        created, started = server.mudStats()
    print(created, started)

    print("""
                     A B E R  M U D

              By Alan Cox, Richard Acott Jim Finnis

    This AberMUD was created: {created}
    {elapsed}
    """.format(
        created = created,
        elapsed = elapsed,
    ))



def motd(show=True):
    '''
    List the message of the day
    '''
    if not show:
        return

    print('MOTD')
    cls()
    printfile(CONFIG.get('MOTD'))
    getpass("")
    print("\n\n")
    # return showMotd()
