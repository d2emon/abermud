from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import pname
from .sys_log import logger


def bloodrcv(state, array, isme):
    #
    logger.debug("%s slain by %s", state['name'], pname(array[0]))
    #
    close_world(state)
    #
    state = open_world(state)
    #
    raise PlayerIsDead("Oh dear... you seem to be slightly dead\n")
    #
