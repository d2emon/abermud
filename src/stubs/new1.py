from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .sys_log import logger


def ohereandget(state):
    #
    state = open_world(state)
    #


def pushcom():
    #
    broad("[d]You hear a thud and a squelch in the distance.\n[/d]")
    #
    broad("[d]Church bells ring out around you\n[/d]")
    #
    raise PlayerIsDead("             S   P    L      A         T           !")
    #
    state = set_channel(state, -140)


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
    sendsys(
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "{} has just died\n".format(state['name']),
    )
    sendsys(
        state['name'],
        state['name'],
        -10113,
        state['curch'],
        "[ {} has just died ]\n".format(state['name']),
    )
    raise PlayerIsDead("Oh dear you just died")
    #


def teletrap(state):
    state = set_channel(state, newch)