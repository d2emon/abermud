import sys
from ..errors import PlayerIsDead
from ..key import key_reprint
from ..opensys import openworld
# from ..tk import rte
# from ..tk.lock import loseme


def __ignore(state):
    return state


def __on_time(state):
    if not sig_active or state['__ignore']:
        return

    set_alarm(state, False)
    openworld()

    state['interrupt'] = True
    rte(state['globme'])
    state['interrupt'] = False

    on_timing()

    closeworld()
    state = key_reprint(state)
    return set_alarm(state, True)


def __on_error(state):
    set_alarm(state, False)
    loseme(state)
    sys.exit(255)


def __on_quit(state):
    print("^C")

    if state['in_fight']:
        return state

    set_alarm(state, False)

    raise PlayerIsDead("Byeeeeeeeeee  ...........")


global_state = {
    '__ignore': True,
    '__time': None,
    'sig_active': False,
    # Events
    'onClose': __on_error,
    'onQuit': __on_quit,
    'onKill': __on_quit,
    'onStop': __ignore,
    'onError': __ignore,
    'onTime': __on_time,
}


def set_alarm(state, alarm):
    return {
        **state,
        'sig_active': alarm,
        '__time': alarm and 2,
        '__ignore': not alarm,
    }
