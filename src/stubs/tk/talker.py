from ..errors import WorldError
from ..bprintf import make_buffer
from ..opensys import close_world, open_world
from . import set_channel


def __putmeon(state):
    if fpbn(state['name']) != -1:
        raise WorldError("You are already on the system - you may only be on once at a time")

    player_id = next((player_id for player_id in range(state['maxu']) if not len(pname(player_id))), None)
    if player_id is None:
        raise Exception("Sorry AberMUD is full at the moment")

    state['mynum'] = player_id
    setpname(player_id, state['name'])
    setploc(player_id, state['curch'])
    setppos(player_id, -1)
    setplev(player_id, 1)
    setpvis(player_id, 0)
    setpstr(player_id, -1)
    setpwpn(player_id, -1)
    setpsex(player_id, 0)
    return state


def __special(state, string):
    if string and string[0] != ".":
        return state

    code = string[1]
    if code == 'q':
        pass
    elif code == 'g':
        state.update({
            'curmode': 1,
            'curch': -5
        })
        initme()
        state = open_world(state)

        setpstr(state['mynum'], state['my_str'])
        setplev(state['mynum'], state['my_lev'])
        setpvis(state['mynum'], 0 if state['my_lev'] < 10000 else 10000)
        setpwpn(state['mynum'], -1)
        setpsexall(state['mynum'], state['my_sex'])
        setphelping(state['mynum'], -1)

        state = set_channel(state, -5 if randperc() > 50 else -183)

        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[s name=\"{}\"]{}  has entered the game\n[/s]".format(state['name'], state['name']),
        )

        state = state['rte'](state)

        sendsys(
            state['name'],
            state['name'],
            -10000,
            state['curch'],
            "[s name=\"{}\"][ {}  has entered the game ]\n[/s]".format(state['name'], state['name']),
        )
    else:
        print("\nUnknown . option")
    return state


def __listen(state):
    state = state['pbfr'](state)

    if state['convflg'] == 0:
        prompt = ">"
    elif state['convflg'] == 1:
        prompt = "\""
    elif state['convflg'] == 2:
        prompt = "*"
    else:
        prompt = "?"

    if pvis(state['mynum']):
        prompt = "({})".format(prompt)
    if state['debug_mode']:
        prompt = "#" + prompt
    if state['my_lev'] > 9:
        prompt = "----" + prompt

    state = state['pbfr'](state)

    if pvis(state['mynum']) > 9999:
        state['program'] = "-csh"
    elif pvis(state['mynum']) == 0:
        state['program'] = "   --}----- ABERMUD -----{--     Playing as {}".format(state['name'])

    state = set_alarm(state, True)
    state = key_input(state, prompt, 80)
    state = set_alarm(state, False)

    work = state['key_buff']
    state['sysbuf'] = "[l]{}\n[/l]".format(work)

    state = open_world(state)
    state = state['rte'](state)
    close_world(state)

    if state['convflg'] and work == "**":
        state['convflg'] = 0
        return __listen(state)

    if work == "*":
        if state['convflg'] == 1:
            work = "say {}".format(work)
        elif state['convflg'] == 2:
            work = "tss {}".format(work)

    if state['curmode'] == 1:
        state = gamecom(state, work)
    else:
        state = __special(state, work)

    if state['fighting'] > -1:
        if not pname(state['fighting']) or ploc(state['fighting']) != state['curch']:
            state.update({
                'in_fight': 0,
                'fighting': -1,
            })
    if state['in_fight']:
        state['in_fight'] -= 1

    return state


def talker(state):
    state = make_buffer(state)

    try:
        state = open_world(state)
        state = __putmeon(state)
        state['cms'] = -1
        state = state['rte'](state)
        close_world(state)
    except WorldError:
        raise WorldError("Sorry AberMUD is currently unavailable")

    state['cms'] = -1
    __special(state, '.g')
    state['i_setup'] = True
    return state


def next_turn(state):
    state = state['pbfr'](state)
    __listen(state)
    if state['rd_qd']:
        state = state['rte'](state)
    state['rd_qd'] = False
    close_world(state)
    state = state['pbfr'](state)
    return state
