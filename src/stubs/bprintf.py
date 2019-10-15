from .errors import OutputBufferError
from .opensys import close_world
from .sys_log import logger


def __lock_alarm(state):
    return {
        **state,
        '__ignore': True,
    }


def __unlock_alarm(state):
    if state['timer_active']:
        state['time'] = 2
    return {
        **state,
        '__ignore': False,
    }


def bprintf(state, *args):
    #
    logger.debug("Bprintf Short Buffer overflow")
    raise OutputBufferError("Internal Error in BPRINTF")
    #


def dcprnt(__str, __file):
    #
    raise OutputBufferError("Internal $ control sequence error")
    #


def tocontinue(state, __str, ct, x, mx):
    #
    logger.debug("Bprintf Short Buffer overflow")
    #
    raise OutputBufferError("Buffer OverRun in IO_TOcontinue")
    #


def make_buffer(state):
    try:
        state['sysbuf'] = ''
        return state
    except Exception:
        raise OutputBufferError("Out Of Memory")


def pbfr(state):
    state = __lock_alarm(state)
    close_world(state)
    #
    state = __unlock_alarm(state)
    return state


def quprnt(state, x):
    #
    logger.debug("Buffer overflow on user %s", state['name'])
    raise OutputBufferError("PANIC - Buffer overflow")
    #

def opensnoop(user, per):
    #
    return z.connect(per).lock()
