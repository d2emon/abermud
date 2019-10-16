from .errors import PlayerIsDead, PlayerLoose
from .opensys import close_world, open_world
from .support import Item


def helpcom(state):
    #
    close_world(state)
    #


def levcom(state):
    #
    close_world(state)
    #


def stacom(state):
    if brkword() == -1:
        return state['bprintf'](state, "STATS what?\n")

    if state['my_lev'] < 10:
        return state['bprintf'](state, "Sorry, this is a wizard command buster...\n")

    item = Item(state, fobn(state['wordbuf']))
    if item.item_id == -1:
        return statplyr(state)

    state = state['bprintf'](state, "\nItem        :{}".format(oname(item.item_id)))
    if item.carry_flag == Item.CONTAINED_IN:
        state = state['bprintf'](state, "\nContained in:{}".format(oname(item.location)))
    elif item.carry_flag == Item.LOCATED_AT:
        state = state['bprintf'](state, "\nPosition    :")
        showname(item.location)
    else:
        state = state['bprintf'](state, "\nHeld By     :{}".format(pname(item.location)))
    state = state['bprintf'](state, "\nState       :{}".format(state(item.item_id)))
    state = state['bprintf'](state, "\nCarr_Flag   :{}".format(item.carry_flag))
    state = state['bprintf'](state, "\nSpare       :{}".format(ospare(item.item_id)))
    state = state['bprintf'](state, "\nMax State   :{}".format(omaxstate(item.item_id)))
    state = state['bprintf'](state, "\nBase Value  :{}".format(obaseval(item.item_id)))
    state = state['bprintf'](state, "\n")
    return state


def examcom(state):
    if brkword() == -1:
        return state['bprintf'](state, "Examine what?\n")

    item = Item(state, fobna(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "You see nothing special at all\n")
    elif item.item_id == 144 and obyte(item.item_id, 0) == 0:
        osetbyte(item.item_id, 0, 1)
        state = state['bprintf'](state, "You take a scroll from the tube.\n")
        scroll = Item(state, 145)
        ocreate(scroll.item_id)
        scroll.carried_by = state['mynum']
        return state
    elif item.item_id == 145:
        destroy(item.item_id)
        state = change_channel(state, -114)
        state = state['bprintf'](state, "As you read the scroll you are teleported!\n")
        return state
    elif item.item_id == 101 and obyte(item.item_id, 0) == 0:
        osetbyte(item.item_id, 0, 1)
        key = Item(state, 107)
        oclrbit(key, 0)
        key.carried_by = state['mynum']
        state = state['bprintf'](state, "You take a key from one pocket\n")
        return state
    elif item.item_id == 7:
        setstate(item.item_id, randperc() % 3 + 1)
        if state(item.item_id) == 1:
            state = state['bprintf'](state, "It glows red")
        if state(item.item_id) == 2:
            state = state['bprintf'](state, "It glows blue")
        if state(item.item_id) == 3:
            state = state['bprintf'](state, "It glows green")
        state = state['bprintf'](state, "\n")
        return state
    elif item.item_id == 8 and state(7) != 0 and iscarrby(3 + state(7), state['mynum']) and otstbit(3 + state(7), 13):
        state = state['bprintf'](state, "Everything shimmers and then solidifies into a different view!\n")
        destroy(item.item_id)
        teletrap(-1074)
        return state
    elif item.item_id == 85 and not obyte(83, 0):
        state = state['bprintf'](state, "Aha. under the bed you find a loaf and a rabbit pie\n")
        ocreate(83)
        ocreate(84)
        oclrbyte(83, 0, 1)
        return state
    elif item.item_id == 91 and not obyte(90, 0):
        ocreate(90)
        state = state['bprintf'](state, "You pull an amulet from the bedding\n")
        oclrbyte(90, 0, 1)
        return state

    try:
        r = Service("{}{}".format(EXAMINES, item.item_id))
        r.connect('r')
        for x in r.contents:
            state = state['bprintf'](state, "{}\n".format(x))
        r.disconnect()
        return state
    except ServiceError:
        return state['bprintf'](state, "You see nothing special.\n")


def statplyr(state):
    #
    close_world(state)
    #


def incom(state):
    #
    close_world(state)
    #
    state = open_world(state)
    #
    state = open_world(state)
    #


def jumpcom():
    #
    raise PlayerLoose("I suppose you could be scraped up - with a spatula")
    #
    return change_channel(state, b)


def wherecom(state):
    if state['my_str'] < 10:
        return state['bprintf'](state, "You are too weak\n")

    if state['my_lev'] < 10:
        state['my_str'] -= 2

    rnd = randperc()
    cha = 10 * state['my_lev']
    if iscarrby(111, state['mynum']) or iscarrby(121, state['mynum']) or iscarrby(163, state['mynum']):
        cha = 100

    close_world(state)

    if rnd > cha:
        return state['bprintf'](state, "Your spell fails...\n")

    if brkword() == -1:
        return state['bprintf'](state, "What is that?\n")

    rnd = 0
    for cha in range(state['numobs']):
        item = Item(state, cha)
        if oname(item.item_id) == state['wordbuf']:
            rnd = 1
            if state['my_lev'] > 9999:
                state = state['bprintf'](state, "[{}]".format(item.item_id))
            state = state['bprintf'](state, "{} - ".format(oname(item.item_id)))
            if state['my_lev'] < 10 and ospare(item.item_id) == -1:
                state = state['bprintf'](state, "Nowhere\n")
            else:
                desrm(item.location, item.carry_flag)

    item = Item(state, fpbn(state['wordbuf']))
    if item.item_id != -1:
        rnd += 1
        state = state['bprintf'](state, "{} - ".format(pname(item.item_id)))
        desrm(ploc(item.item_id), 0)

    if rnd:
        return state

    return state['bprintf'](state, "I dont know what that is\n")