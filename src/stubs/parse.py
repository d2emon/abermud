from .errors import PlayerIsDead
from .support import syslog, pname


def doaction(n):
    #
    raise PlayerIsDead("Goodbye")
    #


def gamrcv(blok):
    #
    raise PlayerIsDead("Bye Bye Cruel World....")
    #
    raise PlayerIsDead("Bye Bye.... Slain By Lightning")
    #
    raise PlayerIsDead("You have been kicked off")
    #


def rescom():
    b = RESET_DATA.connect('r').lock()


def lightning(state):
    #
    syslog(state, "{} zapped {}".format(state['globme'], pname(vic)))
    #


def calibme(state):
    #
    syslog(state, "{} to level {}".format(state['globme'], b))
    #


def exorcom(state):
    #
    syslog(state, "{} exorcised {}".format(state['globme'], pname(x)))
    #


def tsscom():
    keysetback()
    keysetup()


def rmeditcom():
    #
    raise PlayerIsDead("You have been kicked off")
    #


def u_system():
    #
    raise PlayerIsDead("You have been kicked off")
    #


def becom():
    #
    keysetback()
    #


def bugcom(state):
    #
    syslog(state, "Bug by {} : {}".format(state['globme'], x))


def typocom(state):
    #
    syslog(state, "Typo by {} : {}".format(y, x))
