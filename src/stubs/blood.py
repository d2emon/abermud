from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import pname, syslog


def bloodrcv(state, array, isme):
    #
    syslog(state, "{} slain by {}".format(state['name'], pname(array[0])))
    #
    close_world(state)
    #
    state = open_world(state)
    #
    raise PlayerIsDead("Oh dear... you seem to be slightly dead\n")
    #
