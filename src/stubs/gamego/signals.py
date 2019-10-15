import sys
from ..errors import PlayerIsDead
from ..key import key_reprint
from ..opensys import close_world, open_world
# from ..tk.lock import loseme


def __ignore(state):
    return state


def __on_time(state):
    if not state['timer_active'] or state['__ignore']:
        return

    state = set_alarm(state, False)
    state = open_world(state)

    state['interrupt'] = True
    state = state['rte'](state)
    state['interrupt'] = False

    on_timing()

    close_world(state)
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
    'timer_active': False,
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
        'timer_active': alarm,
        '__time': alarm and 2,
        '__ignore': not alarm,
    }
