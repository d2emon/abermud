from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import Item
from .sys_log import logger


def ohereandget(state):
    #
    state = open_world(state)
    #


def wavecom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    elif item.item_id == 136:
        bridge = Item(state, 151)
        if state(bridge.item_id) == 1 or bridge.location == state['curch']:
            setstate(150, 0)
            return state['bprintf'](state, "The drawbridge is lowered!\n")
    elif item.item_id == 158:
        teletrap(-114)
        return state['bprintf'](state, "You are teleported!\n")
    return state['bprintf'](state, "Nothing happens\n")


def putcom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state

    if brkword() == -1:
        return state['bprintf'](state, "where?\n")

    if state['wordbuf'] in ('on', 'in') and brkword() == -1:
        return state['bprintf'](state, "What?\n")

    location = Item(state, fobna(state['wordbuf']))
    if location.item_id == -1:
        return state['bprintf'](state, "There isn't one of those here.\n")
    elif location.item_id == 10:
        if item.item_id < 4 or item.item_id > 6:
            return state['bprintf'](state, "You can't do that\n")
        if state(location.item_id) != 2:
            return state['bprintf'](state, "There is already a candle in it!\n")
        return state['bprintf'](state, "The candle fixes firmly into the candlestick\n")
        state['my_sco'] += 50
        destroy(item.item_id)
        osetbyte(location.item_id, 1, item.item_id)
        osetbit(location.item_id, 9)
        osetbit(location.item_id, 10)
        if otstbit(item.item_id, 13):
            osetbit(location.item_id, 13)
            setstate(location.item_id, 0)
        else:
            setstate(location.item_id, 1)
            oclearbit(location.item_id, 13)
        return state
    elif location.item_id == 137:
        if state(location.item_id) == 0:
            item.located_at = -162
            return state['bprintf'](state, "ok\n")
        destroy(item.item_id)
        state = state['bprintf'](state, "It dissappears with a fizzle into the slime\n")
        if item.item_id == 108:
            state = state['bprintf'](state, "There isn't one of those here.\n")
            setstate(location.item_id, 0)
        return state
    elif location.item_id == 193:
        return state['bprintf'](state, "You can't do that, the chute leads up from here!\n")
    elif location.item_id == 192:
        if item.item_id == 32:
            return state['bprintf'](state, "You can't let go of it!\n")
        state = state['bprintf'](state, "It vanishes down the chute....\n")
        chute = Item(state, 193)
        sendsys(
            state,
            None,
            None,
            -10000,
            chute.location,
            "The {} comes out of the chute!\n".format(oname(item.item_id)),
        )
        item.located_at = chute.location
        return state
    elif location.item_id == 23:
        if item.item_id == 19 and state(21) == 1:
            state = state['bprintf'](state, "The door clicks open!\n")
            setstate(20, 0)
            return state
        return state['bprintf'](state, "Nothing happens\n")
    elif location.item_id == item.item_id:
        return state['bprintf'](state, "What do you think this is, the goon show?\n")

    if otstbit(location.item_id, 14) == 0:
        return state['bprintf'](state, "You can't do that\n")
    if state(location.item_id) != 0:
        return state['bprintf'](state, "That's not open\n")
    if obflannel(litem.item_id) != 0:
        return state['bprintf'](state, "You can't take that!\n")
    if dragget():
        return state
    if item.item_id == 32:
        return state['bprintf'](state, "You can't let go of it!\n")
    item.contained_in = location.item_id
    state = state['bprintf'](state, "Ok.\n")
    sendsys(
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "[D]{}[/D][c] puts the {} in the {}.\n[c]".format(state['name'], oname(item.item_id), oname(location.item_id)),
    )
    if otstbit(item.item_id, 12):
        setstate(item.item_id, 0)
    if state['curch'] == -1081:
        setstate(20, 1)
        state = state['bprintf'](state, "The door clicks shut....\n")
    return state


def pushcom(state):
    if brkword() == -1:
        return state['bprintf'](state, "Push what ?\n")

    item = Item(state, fobna(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "That is not here\n")
    elif item.item_id == 126:
        state = state['bprintf'](state, "The tripwire moves and a huge stone crashes down from above!\n")
        broad(world, "[d]You hear a thud and a squelch in the distance.\n[/d]")
        raise PlayerIsDead("             S   P    L      A         T           !")
    elif item.item_id == 162:
        state = state['bprintf'](state, "A trapdoor opens at your feet and you plumment downwards!\n")
        return change_channel(state, -140)
    elif item.item_id == 130:
        if state(132) == 1:
            setstate(132, 0)
            return state['bprintf'](state, "A secret panel opens in the east wall!\n")
        else:
            return state['bprintf'](state, "Nothing happens\n")
    elif item.item_id == 131:
        if state(134) == 1:
            setstate(134, 0)
            state = state['bprintf'](state, "Uncovering a hole behind it.\n")
        return state
    elif item.item_id == 138:
        if state(137) == 1:
            setstate(137, 0)
            return state['bprintf'](state, "You hear a gurgling noise and then silence.\n")
        else:
            return state['bprintf'](state, "Ok...\n")
    elif item.item_id in (146, 147):
        setstate(146, 1 - state(146))
        return state['bprintf'](state, "Ok...\n")
    elif item.item_id == 30:
        setstate(28, 1 - state(28))
        if state(28):
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 28).location,
                "[c]The portcullis falls\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 29).location,
                "[c]The portcullis falls\n[/c]",
            )
        else:
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 28).location,
                "[c]The portcullis rises\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 29).location,
                "[c]The portcullis rises\n[/c]",
            )
        return state
    elif item.item_id == 149:
        setstate(150, 1 - state(150))
        if state(150):
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 150).location,
                "[c]The drawbridge rises\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 151).location,
                "[c]The drawbridge rises\n[/c]",
            )
        else:
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 150).location,
                "[c]The drawbridge is lowered\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 151).location,
                "[c]The drawbridge is lowered\n[/c]",
            )
        return state
    elif item.item_id == 24:
        if state(26) == 1:
            setstate(26, 0)
            return state['bprintf'](state, "A secret door slides quietly open in the south wall!!!\n")
        else:
            return state['bprintf'](state, "It moves but nothing seems to happen\n")
    elif item.item_id == 49:
        return broad(world, "[d]Church bells ring out around you\n[/d]")
    elif item.item_id == 104:
        return state['bprintf'](state, "You can't shift it alone, maybe you need help\n")

    if otstbit(item.item_id, 4):
        setstate(item.item_id, 0)
        oplong(item.item_id)
        return state
    elif otstbit(item.item_id, 5):
        setstate(item.item_id, 1 - state(item.item_id))
        oplong(item.item_id)
        return state
    else:
        return state['bprintf'](state, "Nothing happens\n")


def gropecom():
    #
    raise PlayerIsDead("Bye....... LINE TERMINATED - MORALITY REASONS")
    #


def vicbase(state):
    #
    state = open_world(state)
    #


def wounded(state, n):
    #
    close_world(state)
    logger.debug("%s slain magically", state['name'])
    #
    state = open_world(state)
    #
    sendsys(
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "{} has just died\n".format(state['name']),
    )
    sendsys(
        state['name'],
        state['name'],
        -10113,
        state['curch'],
        "[ {} has just died ]\n".format(state['name']),
    )
    raise PlayerIsDead("Oh dear you just died")
    #


def iswornby(item, player):
    if not iscarrby(item, player):
        return False
    return item.carry_flag == Item.WORN_BY


def teletrap(state):
    state = change_channel(state, newch)


def on_flee_event(state):
    for item_id in range(state['numobs']):
        item = Item(state, item_id)
        if iscarrby(item.item_id, state['mynum']) and not iswornby(item.item_id, state['mynum']):
            item.located_at = ploc(state['mynum'])
