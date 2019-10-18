from .support import Item, Player


def aobjsat(state, location, mode):
    found = False
    cols = 0
    for item_id in range(state['NOBS']):
        item = Item(state, item_id)
        if iscarrby(state, item, location) and mode == 1 or iscontin(state, item, location) and mode == 3:
            found = True
            cols += 1 + len(item.name)
            if state['debug_mode']:
                cols += 5
            if isdest(item.item_id):
                cols += 2
            if iswornby(item, location):
                cols += len("<worn> ")
            if cols > 79:
                cols = 0
                state = state['bprintf'](state, "\n")
            if isdest(item.item_id):
                state = state['bprintf'](state, "(")
            state = state['bprintf'](state, item.name)
            if state['debug_mode']:
                state = state['bprintf'](state, "{{}}".format(item_id))
            if iswornby(item, location):
                state = state['bprintf'](state, "<worn> ")
            if isdest(item.item_id):
                state = state['bprintf'](state, ")")
            state = state['bprintf'](state, " ")
            cols += 1
    if not found:
        state = state['bprintf'](state, "Nothing")
    return state['bprintf'](state, "\n")


def iscontin(state, o1, o2):
    item1 = Item(state, o1)
    item2 = Item(state, o2)
    if item1.contained_in != item2.item_id:
        return False
    if state['my_lev'] < 10 and isdest(item1.item_id):
        return False
    return True


def fobnsys(state, name, control, args):
    name = name.lower()
    if name == 'red':
        brkword()
        return 4
    if name == 'blue':
        brkword()
        return 5
    if name == 'green':
        brkword()
        return 6

    for item_id in range(state['NOBS']):
        item = Item(state, item_id)
        if item.name.lower() != name:
            continue
        state['wd_it'] = name
        if control == 0:
            return item.item_id
        elif control == 1:
            if item.item_id == 112 and iscarrby(Item(state, 113), state['mynum']):
                return 113
            if item.item_id == 112 and iscarrby(Item(state, 114), state['mynum']):
                return 114
            if isavl(item.item_id):
                return item.item_id
        elif control == 2:
            if iscarrby(item, state['mynum']):
                return item.item_id
        elif control == 3:
            if iscarrby(item, args):
                return item.item_id
        elif control == 4:
            if ishere(item):
                return item.item_id
        elif control == 5:
            if iscontin(item, args):
                return item.item_id
        else:
            return item.item_id
    return -1


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
        "[D]{}[/D][c] takes the {}\n[/c]".format(state['name'], item.name),
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


def lojal2(state, flannel):
    for item_id in range(state['NOBS']):
        item = Item(state, item_id)
        if ishere(item.item_id) and oflannel(item.item_id) == flannel:
            if state(item.item_id) > 3:
                continue
            if len(item.description):
                if isdest(item.item_id):
                    state = state['bprintf'](state, "--")
                oplong(item.item_id)
                state['wd_it'] = item.name
    return state


def dumpstuff(state, n, loc):
    for item_id in range(state['NOBS']):
        item = Item(state, item_id)
        if iscarrby(state, item.item_id, n):
            item.located_at = loc
    return state


def whocom(state):
    if state['my_lev'] > 9:
        state = state['bprintf'](state, "Players\n")
        max_player_id = 48
    else:
        max_player_id = 16

    for player_id in range(max_player_id):
        player = Player(state, player_id)
        if player_id == 16:
            state = state['bprintf'](state, "----------\nMobiles\n")
        if player.is_alive:
            state = dispuser(state, player.player_id)

    return state['bprintf'](state, "\n")


def dispuser(state, player_id):
    player = Player(state, player_id)
    if player.strength < 0:
        return
    if not player.is_visible(state['my_lev']):
        return
    if not player.is_visible(0):
        state = state['bprintf'](state, "(")
    state = state['bprintf'](state, "{} ".format(player.name))
    disl4(player.level, player.sex)
    if not player.is_visible(0):
        state = state['bprintf'](state, "(")
    if ppos(player.player_id):
        state = state['bprintf'](state, " [Absent From Reality]")
    return state['bprintf'](state, "\n")


def fpbns(state, name):
    for player_id in range(48):
        player = Player(state, player_id)
        if not player.is_alive:
            continue

        player_name = player.name.lower()
        names = [player_name]
        if player_name[:4] == "the ":
            names.append(player_name[4:])
        if name.lower() in names:
            return player
        pass
    return None


def lispeople(state):
    for player_id in range(48):
        player = Player(state, player_id)
        if player.player_id == state['mynum']:
            continue
        if player.is_alive and player.location == state['curch'] and seeplayer(state, player.player_id):
            state = state['bprintf'](state, "{} ".format(player.name))
            if state['debug_mode']:
                state = state['bprintf'](state, "{{}}".format(player.player_id))
            disl4(player.level, player.sex)
            if player.sex == Player.female:
                state['wd_her'] = player.name
            else:
                state['wd_him'] = player.name
            state = state['bprintf'](state, " is here carrying\n")
            lobjsat(player.player_id)
    return state


def oplong(state, item_id):
    item = Item(state, item_id)
    if state['debug_mode']:
        return state['bprintf'](state, "{{}} {}\n".format(item.item_id, item.description))
    if len(item.description):
        return state['bprintf'](state, "{}\n".format(item.description))
    return state
