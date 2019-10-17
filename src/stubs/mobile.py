from .errors import PlayerIsDead
from .support import Item, Player


def on_timing():
    raise NotImplementedError()


def onlook():
    raise NotImplementedError()


def chkfight(state, player_id):
    if player_id < 0:
        return state

    player = Player(state, player_id)
    consid_move(player.player_id)
    if not player.is_alive:
        return state
    if player.location != state['curch']:
        return state
    if pvis(state['mynum']):
        return state
    if randperc() > 40:
        return state
    if player.player_id == fpbns('yeti') and ohany(1 << 13):
        return state
    return mhitplayer(state, player.player_id, state['mynum'])


def consid_move(x):
    raise NotImplementedError()


def crashcom():
    raise NotImplementedError()


def singcom():
    raise NotImplementedError()


def spraycom():
    raise NotImplementedError()


# More new stuff


def dircom(state):
    if state['my_lev'] < 10:
        return state['bprintf'](state, "That's a wiz command\n")

    for item_id in range(state['numobs']):
        item = Item(state, item_id)
        c, b = findzone(item.location)
        d = "{}{}".format(b, c)
        if item.carry_flag == Item.CONTAINED_IN:
            d = "IN ITEM"
        elif item.carry_flag:
            d = "CARRIED"
        state = state['bprintf'](state, "{}{}".format(oname(item.item_id), d))
        if item_id % 3 == 2:
            state = state['bprintf'](state, "\n")
        if item_id % 18 == 17:
            state = state['pbfr'](state)
    return state['bprintf'](state, "\n")


def sys_reset():
    #
    RESET_N.connect('ruf').lock()
    #
    raise NotImplementedError()


def dorune(state):
    if state['in_fight']:
        return state
    for player_id in range(32):
        player = Player(state, player_id)
        if player.player_id == state['mynum']:
            continue
        if not player.is_alive:
            continue
        if plev(player.player_id) > 9:
            continue
        if player.location == state['curch']:
            if randperc() < 9 * state['my_lev']:
                return state
            if fpbns(player.name) == -1:
                return state
            state = state['bprintf'](state, "The runesword twists in your hands lashing out savagely\n")
            return hitplayer(state, player.player_id, 32)


def pepdrop(state):
    sendsys(
        state,
        None,
        None,
        -10000,
        state['curch'],
        "You start sneezing ATISCCHHOOOOOO!!!!\n",
    )
    dragon = Player(state, 32)
    if not dragon.is_alive or dragon.location != state['curch']:
        return state

    # Ok dragon and pepper time
    item = Item(state, 89)
    if iscarrby(item, state['mynum']) and item.carry_flag == Item.WORN_BY:
        # Fried dragon
        dragon.destroy()  # No dragon
        state['my_sco'] += 100
        calibme()
        return state

    # Whoops!
    state = state['bprintf'](state, "The dragon sneezes forth a massive ball of flame.....\n")
    state = state['bprintf'](state, "Unfortunately you seem to have been fried\n")
    raise PlayerIsDead("Whoops.....   Frying tonight")


def dragget(state):
    if state['my_lev'] > 9:
        return False
    dragon = Player(state, fpbns('dragon'))
    if dragon.player_id == -1:
        return False
    if dragon.location != state['curch']:
        return False
    return True


def helpchkr(state):
    player = Player(statw, phelping(state['mynum']))
    if not state['i_setup']:
        return state
    if not player.is_alive or ploc(player.player_id) != state['curch']:
        state = state['bprintf'](state, "You can no longer help [c]{}[/c]\n".format(player.name))
        setphelping(state['mynum'], -1)
    return state
