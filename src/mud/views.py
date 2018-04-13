from config import CONFIG
from d2lib import printfile
from getpass import getpass
from server import stats

import humanize


def cls():
    print("=-" * 40)
    print("\n" * 24)


def start(show=True):
    '''
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    '''
    cls()
    print("\n" * 4)
    if not show:
        return

    # splash()

    time = stats()
    created = time.get('created')
    elapsed = time.get('elapsed')
    print(created, elapsed)

    if created is None:
        created = "<unknown>"
    else:
        created = created.strftime("%x %X")

    if elapsed is None:
        elapsed = "AberMUD has yet to ever start!!!"
    else:
        elapsed = "Game time elapsed: {}".format(
            humanize.naturaltime(elapsed)
        )

    cls()
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
