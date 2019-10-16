from .errors import PlayerIsDead, PlayerLoose
from .opensys import close_world, open_world


def helpcom(state):
    #
    close_world(state)
    #


def levcom(state):
    #
    close_world(state)
    #


def examcom(state):
    state = set_channel(state, -114)


def statplyr(state):
    #
    close_world(state)
    #


def incom(state):
    #
    close_world(state)
    #
    state = open_world(state)
    #
    state = open_world(state)
    #


def jumpcom():
    #
    raise PlayerLoose("I suppose you could be scraped up - with a spatula")
    #
    return set_channel(state, b)


def wherecom(state):
    #
    close_world(state)
    #
