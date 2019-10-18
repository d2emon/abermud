import sys
from ..errors import PlayerIsDead
from ..key import key_reprint
from ..opensys import close_world, open_world


# State
global_state = {
    '__ignore': True,
    '__time': None,
    'interrupt': False,
    'timer_active': False,
}


# Mutations
def set_alarm(state, alarm):
    state.update({
        '__ignore': not alarm,
        '__time': alarm and 2,
        'timer_active': alarm,
    })
    return state


def set_interrupt(state, interrupt):
    state['interrupt'] = interrupt
    return state


# Events
def __ignore(state):
    return state


def __on_time(state):
    if not state['timer_active'] or state['__ignore']:
        return

    state = set_alarm(state, False)
    state = open_world(state)

    state = set_interrupt(state, True)
    state = state['process_messages'](state, state['mynum'], state['cms'])
    state = set_interrupt(state, False)

    on_timing()

    close_world(state)
    state = key_reprint(state)
    return set_alarm(state, True)


def __on_error(state):
    set_alarm(state, False)
    # raise PlayerIsDead()
    sys.exit(255)


def __on_quit(state):
    print("^C")

    if state['in_fight']:
        return state

    set_alarm(state, False)
    raise PlayerIsDead("Byeeeeeeeeee  ...........")


def __on_loose(state):
    state = set_alarm(state, False)
    state['i_setup'] = False

    state = open_world(state)
    dumpitems()
    if state['me'].is_visible(10000):
        state = sendsys(
            state,
            state['name'],
            state['name'],
            -10113,
            "{} has departed from AberMUDII\n".format(state['name']),
        )
    state['me'].destroy()
    close_world(state)

    if not state['zapped']:
        saveme()
    chksnp()
    return state


events = {
    'onClose': __on_error,
    'onQuit': __on_quit,
    'onKill': __on_quit,
    'onStop': __ignore,
    'onError': __ignore,
    'onTime': __on_time,
    'onLoose': __on_loose,
}
