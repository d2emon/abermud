from .errors import PlayerIsDead, PlayerLoose
from .opensys import close_world, open_world
from .support import pname
from .sys_log import logger


def bloodrcv(state, array, isme):
    try:
        #
        logger.debug("%s slain by %s", state['name'], pname(array[0]))
        #
        raise PlayerLoose("Oh dear... you seem to be slightly dead")
    except PlayerLoose as e:
        close_world(state)

        delpers(state['name'])

        state = open_world(state)
        sendsys(
            state['name'],
            state['name'],
            -10000,
            state['curch'],
            "[p]{}[/p] has just died.\n".format(state['name']),
        )
        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[ [p]{}[/p] has been slain by [p]{}[/p] ]\n".format(state['name'], pname(array[0])),
        )
        raise PlayerIsDead(e)
