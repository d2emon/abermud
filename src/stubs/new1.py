from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .sys_log import logger


def ohereandget(state):
    #
    state = open_world(state)
    #


def pushcom():
    #
    raise PlayerIsDead("             S   P    L      A         T           !")
    #


def gropecom():
    #
    raise PlayerIsDead("Bye....... LINE TERMINATED - MORALITY REASONS")
    #


def vicbase(state):
    #
    state = open_world(state)
    #


def wounded(state, n):
    #
    close_world(state)
    logger.debug("%s slain magically", state['name'])
    #
    state = open_world(state)
    #
    raise PlayerIsDead("Oh dear you just died")
    #
