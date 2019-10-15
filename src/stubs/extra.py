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


def wherecom(state):
    #
    close_world(state)
    #
