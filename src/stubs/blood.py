from .errors import PlayerIsDead
from .support import pname, syslog


def bloodrcv(state, array, isme):
    #
    syslog(state, "{} slain by {}".format(state['globme'], pname(array[0])))
    #
    raise PlayerIsDead("Oh dear... you seem to be slightly dead\n")
    #
