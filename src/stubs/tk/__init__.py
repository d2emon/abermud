"""
AberMUD II   C

This game systems, its code scenario and design
are (C) 1987/88  Alan Cox,Jim Finnis,Richard Acott

This file holds the basic communications routines
"""
from ..errors import PlayerIsDead, WorldError
from ..opensys import close_world, open_world, add_message, cleanup
from ..parse import eorte, gamrcv
from ..sys_log import logger


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


def __parse_message(message, receiver):
    name_to = message['to'].lower()
    names = [name_to]
    if name_to[:4] == "the ":
        names.append(name_to[4:])
    is_me = any(name for name in names if name == receiver)
    return is_me, message


def __process_message(state, data):
    receiver = state['name'].lower()
    is_me, message = __parse_message(data, receiver)
    if state['debug_mode']:
        state = state['bprintf'](state, "\n<{}>".format(message['code']))
    if message['code'] < -3:
        return gamrcv(state, is_me, message)
    return state['bprintf'](state, message['text'])


def __read_messages(state, first_message, last_message):
    for message_id in range(first_message, last_message + 1):
        yield state['__messages'][message_id - state['__first_message']]


def __revise(state, cutoff):
    state = open_world(state)
    player_ids = (i for i in range(16) if pname(i) and ppos(i) < cutoff / 2 and ppos(i) != -2)
    for player_id in player_ids:
        state = broad(state, "{} has been timed out\n".format(pname(player_id)))
        dumpstuff(player_id, ploc(player_id))
        setpname(player_id, '')
    return state


def send2(state, message):
    try:
        state = open_world(state)
        state = add_message(state, message)
        if state['__last_message'] - state['__first_message'] >= 199:
            state = cleanup(state)
            state = __revise(state, state['__last_message'])
            longwthr()
        return state
    except WorldError:
        raise PlayerIsDead("AberMUD: FILE_ACCESS : Access failed")


def broad(state, text):
    state['rd_qd'] = True
    return send2(
        state,
        {
            'channel': None,
            'code': -1,
            'to': None,
            'from': None,
            'text': text,
        },
    )


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


def set_channel(state, channel):
    state = open_world(state)
    setploc(state['mynum'], channel)
    return lookin(state, channel)


def update(state):
    global __last_update

    messages = state['cms'] - __last_update
    if abs(messages) < 10:
        return state

    __last_update = state['cms']
    state = open_world(state)
    setppos(state['mynum'], state['cms'])
    return state


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
    logger.debug("System Wrapup exorcised %s", state['name'])
    #
    raise NotImplementedError()


def fcloselock(file):
    raise NotImplementedError()
