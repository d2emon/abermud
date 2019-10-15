"""
AberMUD II   C

This game systems, its code scenario and design
are (C) 1987/88  Alan Cox,Jim Finnis,Richard Acott

This file holds the basic communications routines
"""
from ..errors import PlayerIsDead, WorldError
from ..gamego.signals import set_alarm
from ..key import key_input
from ..opensys import close_world, open_world
from ..parse import eorte, gamrcv
from ..support import syslog


global_state = {
    '__first_message': 0,
    '__last_message': 0,
    '__messages': [],

    'i_setup': 0,

    'cms': -1,
    'curch': 0,
    'name': '',
    'curmode': 0,
    'meall': 0,

    'gurum': 0,
    'convflg': 0,

    'rd_qd': 0,

    'dsdb': 0,
    'moni': 0,

    'bound': 0,
    'tmpimu': 0,
    'echoback': 'e',
    'tmpwiz': '.',

    'mynum': 0,
}

__last_update = 0

"""
Data format for mud packets

Sector 0
[64 words]
0   Current first message pointer
1   Control Word
Sectors 1-n  in pairs ie [128 words]

[channel][controlword][text data]

[controlword]
0 = Text
-1 = general request
"""


def __vcpy(dest, offd, source, offs, __len):
    raise NotImplementedError()


def __process_message(state, message):
    code = message[1]
    text = message[2]
    if state['debug_mode']:
        state = state['bprintf'](state, "\n<{}>".format(code))
    if code < -3:
        return gamrcv(state, message)
    return state['bprintf'](state, text)


def __read_messages(state, first_message, last_message):
    for message_id in range(first_message, last_message + 1):
        yield state['__messages'][message_id - state['__first_message']]


def __send2(state, block):
    raise WorldError("AberMUD: FILE_ACCESS : Access failed")
    state = open_world(state)
    raise NotImplementedError()


def rte(state):
    try:
        state = open_world(state)
    except WorldError:
        raise WorldError("AberMUD: FILE_ACCESS : Access failed")

    last_message_id = state['__last_message']
    first_message_id = state['cms'] if state['cms'] != -1 else last_message_id
    for message in __read_messages(state, first_message_id, last_message_id):
        state = __process_message(state, message)
    state['cms'] = last_message_id

    state = update(state)
    return {
        **eorte(state),
        'rdes': 0,
        'tdes': 0,
        'vdes': 0,
    }


def __cleanup(state, inpbk):
    state = open_world(state)

    raise NotImplementedError()


def broad(mesg):
    raise NotImplementedError()


def __tbroad(message):
    raise NotImplementedError()


def split(block, nam1, nam2, work, luser):
    raise NotImplementedError()


def trapch(state, chan):
    state = open_world(state)

    raise NotImplementedError()


def update(state):
    global __last_update

    messages = state['cms'] - __last_update
    if abs(messages) < 10:
        return state

    __last_update = state['cms']
    state = open_world(state)
    setppos(state['mynum'], state['cms'])
    return state


def __revise(state, cutoff):
    state = open_world(state)

    raise NotImplementedError()


def lookin(state, room):
    close_world(state)
    state = open_world(state)
    state = open_world(state)
    raise PlayerIsDead("bye bye.....")
    raise NotImplementedError()


def __loodrv(room):
    raise NotImplementedError()


def __userwrap(state):
    #
    syslog(state, "System Wrapup exorcised {}".format(state['name']))
    #
    raise NotImplementedError()


def fcloselock(file):
    raise NotImplementedError()
