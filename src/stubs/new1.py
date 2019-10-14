from .errors import PlayerIsDead
from .support import syslog


def pushcom():
    #
    raise PlayerIsDead("             S   P    L      A         T           !")
    #


def gropecom():
    #
    raise PlayerIsDead("Bye....... LINE TERMINATED - MORALITY REASONS")
    #


def wounded(state, n):
    #
    syslog(state, "{} slain magically".format(state['globme']))
    #
    raise PlayerIsDead("Oh dear you just died")
    #
