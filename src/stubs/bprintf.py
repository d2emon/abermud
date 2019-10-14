from .errors import OutputBufferError
from .support import syslog


def __lock_alarm(state):
    return {
        **state,
        '__ignore': True,
    }


def __unlock_alarm(state):
    if state['sig_active']:
        state['time'] = 2
    return {
        **state,
        '__ignore': False,
    }


def bprintf(state, *args):
    #
    syslog(state, "Bprintf Short Buffer overflow")
    raise OutputBufferError("Internal Error in BPRINTF")
    #


def dcprnt(__str, __file):
    #
    raise OutputBufferError("Internal $ control sequence error")
    #


def tocontinue(state, __str, ct, x, mx):
    #
    syslog(state, "Bprintf Short Buffer overflow")
    #
    raise OutputBufferError("Buffer OverRun in IO_TOcontinue")
    #


def makebfr():
    #
    raise OutputBufferError("Out Of Memory")
    #


def pbfr(state):
    __lock_alarm(state)
    #
    __unlock_alarm(state)
    return state


def quprnt(state, x):
    #
    syslog(state, "Buffer overflow on user {}".format(state['globme']))
    raise OutputBufferError("PANIC - Buffer overflow")
    #

def opensnoop(user, per):
    #
    return z.connect(per).lock()
