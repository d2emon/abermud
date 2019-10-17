from .support import Item, Player


def iscontin(state, o1, o2):
    item1 = Item(state, o1)
    item2 = Item(state, o2)
    if item1.contained_in != item2.item_id:
        return False
    if state['my_lev'] < 10 and isdest(item1.item_id):
        return False
    return True


def getobj(state):
    if brkword() == -1:
        return state['bprintf'](state, "Get what?\n")

    item = Item(state, fobnh(state['wordbuf']))
    location = Item(state, -1)
    # Hold
    i = state['stp']
    bf = state['wordbuf']
    if brkword() != -1 and state['wordbuf'] in ['from', 'out']:
        if brkword() == -1:
            return state['bprintf'](state, "From what?\n")
        location = Item(state, fobna(state['wordbuf']))
        if location.item_id == -1:
            return state['bprintf'](state, "You can't take things from that - it's not here\n")
        item = Item(state, fobnin(bf, location.item_id))
    state['stp'] = i

    if item.item_id == -1:
        return state['bprintf'](state, "That is not here.\n")

    if item.item_id == 112 and location.item_id == -1:
        if isdest(113):
            item = Item(state, 113)
        elif isdest(114):
            item = Item(state, 114)

        if item.item_id in (113, 114):
            oclrbit(item.item_id, 0)
        else:
            state = state['bprintf'](state, "The shields are all to firmly secured to the walls\n")

    if obflannel(item.item_id):
        return state['bprintf'](state, "You can't take that!\n")
    if dragget():
        return state
    if not cancarry(state['mynum']):
        return state['bprintf'](state, "You can't carry any more\n")
    if item.item_id == 32 and state(item.item_id) == 1 and ptothlp(state['mynum']) == -1:
        return state['bprintf'](state, "Its too well embedded to shift alone.\n")

    item.carried_by = state['mynum']
    state = state['bprintf'](state, "Ok...\n")
    sendsys(
        state,
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "[D]{}[/D][c] takes the {}\n[/c]".format(state['name'], oname(item.item_id)),
    )
    if otstbit(item.item_id, 12):
        setstate(item.item_id, 0)
    if state['curch'] == -1081:
        setstate(20, 1)
        state = state['bprintf'](state, "The door clicks shut....\n")
    return state


def ishere(state, item_id):
    item = Item(state, item_id)
    if state['my_lev'] < 10 and isdest(item.item_id):
        return False
    if item.carried_by != state['curch']:
        return False
    return True


def iscarrby(state, item_id, player_id):
    item = Item(state, item_id)
    if state['my_lev'] < 10 and isdest(item.item_id):
        return False
    if item.owned_by != player_id:
        return False
    return True


def dropitem(state):
    if brkword() == -1:
        return state['bprintf'](state, "Drop what?\n")

    item = Item(state, fobnc(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "You are not carrying that.\n")

    if state['my_lev'] < 10 and item.item_id == 32:
        return state['bprintf'](state, "You can't let go of it!\n")

    item.located_at = state['curch']
    state = state['bprintf'](state, "OK..\n")
    sendsys(
        state,
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "[D]{}[/D][c] drops the {}\n\n[/c]".format(state['name'], state['wordbuf']),
    )

    if state['curch'] not in (-183, -5):
        return state
    state = state['bprintf'](state, "It disappears down into the bottomless pit.....\n")
    sendsys(
        state,
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "The {} disappears into the bottomless pit.\n".format(state['wordbuf']),
    )
    state['my_sco'] += tscale() * obaseval(item.item_id) / 5
    calibme()
    item.located_at = -6
    return state


def dumpstuff(state, n, loc):
    for item_id in range(state['NOBS']):
        item = Item(state, item_id)
        if iscarrby(state, item.item_id, n):
            item.located_at = loc
    return state


def lispeople(state):
    for player_id in range(48):
        player = Player(state, player_id)
        if player.player_id == state['mynum']:
            continue
        if len(pname(player.player_id)) and player.location == state['curch'] and seeplayer(state, player.player_id):
            state = state['bprintf'](state, "{} ".format(pname(player.player_id)))
            if state['debug_mode']:
                state = state['bprintf'](state, "{{}}".format(player.player_id))
            disl4(plev(player.player_id), psex(player.player_id))
            if psex(player.player_id):
                state['wd_her'] = pname(player.player_id)
            else:
                state['wd_him'] = pname(player.player_id)
            state = state['bprintf'](state, " is here carrying\n")
            lobjsat(player.player_id)
    return state
