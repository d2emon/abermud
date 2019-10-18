from .errors import PlayerIsDead, PlayerLoose
from .opensys import close_world, open_world
from .support import Item, Player


def helpcom(state):
    if brkword() != -1:
        player = Player(state, fpbn(state['wordbuf']))
        if player.player_id == -1:
            return state['bprintf'](state, "Help who?\n")
        if player.location != state['curch']:
            return state['bprintf'](state, "They are not here\n")
        if player.player_id == state['mynum']:
            return state['bprintf'](state, "You can't help yourself.\n")

        if phelping(state['mynum']) != -1:
            sendsys(
                state,
                player.name,
                player.name,
                -10011,
                state['curch'],
                "[c]{}[/c] has stopped helping you\n".format(state['name']),
            )
            helping = Player(state, phelping(state['mynum']))
            state = state['bprintf'](state, "Stopped helping {}\n". format(helping.name))

        setphelping(state['mynum'], player.player_id)
        sendsys(
            state,
            player.name,
            player.name,
            -10011,
            state['curch'],
            "[c]{}[/c] has offered to help you\n".format(state['name']),
        )
        return state['bprintf'](state, "OK...\n")

    close_world(state)
    state = state['bprintf'](state, "[f]{}[/f]".format(HELP1))
    if state['my_lev'] > 9:
        state = state['bprintf'](state, "Hit <Return> For More....\n")
        state = state['pbfr'](state)
        while getchar() != "\n":
            pass
        state = state['bprintf'](state, "[f]{}[/f]".format(HELP2))
    state = state['bprintf'](state, "\n")
    if state['my_lev'] > 9999:
        state = state['bprintf'](state, "Hit <Return> For More....\n")
        state = state['pbfr'](state)
        while getchar() != "\n":
            pass
        state = state['bprintf'](state, "[f]{}[/f]".format(HELP3))
    state = state['bprintf'](state, "\n")
    return state


def levcom(state):
    #
    close_world(state)
    #


def valuecom(state):
    if brkword() == -1:
        return state['bprintf'](state, "Value what ?\n")
    item = Item(state, fobna(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "There isn't one of those here.\n")
    return state['bprintf'](state, "{} : {} points\n".format(item.name, item.value))


def stacom(state):
    if brkword() == -1:
        return state['bprintf'](state, "STATS what?\n")

    if state['my_lev'] < 10:
        return state['bprintf'](state, "Sorry, this is a wizard command buster...\n")

    item = Item(state, fobn(state['wordbuf']))
    if item.item_id == -1:
        return statplyr(state)

    state = state['bprintf'](state, "\nItem        :{}".format(item.name))
    if item.carry_flag == Item.CONTAINED_IN:
        container = Item(state, item.location)
        state = state['bprintf'](state, "\nContained in:{}".format(container.name))
    elif item.carry_flag == Item.LOCATED_AT:
        state = state['bprintf'](state, "\nPosition    :")
        showname(item.location)
    else:
        player = Player(state, item.location)
        state = state['bprintf'](state, "\nHeld By     :{}".format(player.name))
    state = state['bprintf'](state, "\nState       :{}".format(state(item.item_id)))
    state = state['bprintf'](state, "\nCarr_Flag   :{}".format(item.carry_flag))
    state = state['bprintf'](state, "\nSpare       :{}".format(item.is_destroyed))
    state = state['bprintf'](state, "\nMax State   :{}".format(item.max_state))
    state = state['bprintf'](state, "\nBase Value  :{}".format(item.base_value))
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
        scroll.create()
        scroll.carried_by = state['mynum']

        return state
    elif item.item_id == 145:
        item.destroy()
        state = change_channel(state, -114)
        state = state['bprintf'](state, "As you read the scroll you are teleported!\n")
        return state
    elif item.item_id == 101 and obyte(item.item_id, 0) == 0:
        osetbyte(item.item_id, 0, 1)
        key = Item(state, 107)
        key.create()
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
    elif item.item_id == 8 and state(7) != 0 and iscarrby(3 + state(7), state['mynum']) and Item(state, 3 + state(7)).is_lit:
        state = state['bprintf'](state, "Everything shimmers and then solidifies into a different view!\n")
        item.destroy()
        teletrap(-1074)
        return state
    elif item.item_id == 85 and not obyte(83, 0):
        state = state['bprintf'](state, "Aha. under the bed you find a loaf and a rabbit pie\n")
        Item(state, 83).create()
        Item(state, 84).create()
        oclrbyte(83, 0, 1)
        return state
    elif item.item_id == 91 and not obyte(90, 0):
        Item(state, 90).create()
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
    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id == -1:
        return state['bprintf'](state, "Whats that?\n")
    state = state['bprintf'](state, "Name      : {}\n".format(player.name))
    state = state['bprintf'](state, "Level     : {}\n".format(player.level))
    state = state['bprintf'](state, "Strength  : {}\n".format(player.strength))
    state = state['bprintf'](state, "Sex       : {}\n".format(player.sex))
    state = state['bprintf'](state, "Location  : ")
    showname(player.location)
    return state


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
        if item.name == state['wordbuf']:
            rnd = 1
            if state['my_lev'] > 9999:
                state = state['bprintf'](state, "[{}]".format(item.item_id))
            state = state['bprintf'](state, "{} - ".format(item.name))
            if state['my_lev'] < 10 and item.is_destroyed:
                state = state['bprintf'](state, "Nowhere\n")
            else:
                desrm(item.location, item.carry_flag)

    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id != -1:
        rnd += 1
        state = state['bprintf'](state, "{} - ".format(player.name))
        desrm(player.location, 0)

    if rnd:
        return state

    return state['bprintf'](state, "I dont know what that is\n")


def desrm(state, location, carry_flag):
    if state['my_lev'] < 10 and carry_flag == Item.LOCATED_AT and location > -5:
        return state['bprintf'](state, "Somewhere.....\n")
    if carry_flag == Item.CONTAINED_IN:
        return state['bprintf'](state, "In the {}\n".format(Item(state, location).name))
    if carry_flag != Item.LOCATED_AT:
        player = Player(state, location)
        return state['bprintf'](state, "Carried by [c]{}[/c]\n".format(player.name))

    try:
        unit = openroom(location, 'r')
        for b in range(7):
            x = getstr(unit)
        state = state['bprintf'](state, getstr(unit))
        if state['my_lev'] > 9:
            state = state['bprintf'](state, " | ")
            showname(location)
        else:
            state = state['bprintf'](state, "\n")
        unit.disconnect()
    except ServiceError:
        return state['bprintf'](state, "Out in the void\n")
