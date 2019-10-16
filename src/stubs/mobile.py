from .errors import PlayerIsDead
from .support import Item


def on_timing():
    raise NotImplementedError()


def onlook():
    raise NotImplementedError()


def chkfight(x):
    raise NotImplementedError()


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


def dorune():
    raise NotImplementedError()


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
    if not len(pname(dragon.item_id)) or ploc(dragon.item_id) != state['curch']:
        return state

    # Ok dragon and pepper time
    item = Item(state, 89)
    if iscarrby(item, state['mynum']) and item.carry_flag == Item.WORN_BY:
        # Fried dragon
        setpname(dragon.item_id, '')  # No dragon
        state['my_sco'] += 100
        calibme()
        return state

    # Whoops!
    state = state['bprintf'](state, "The dragon sneezes forth a massive ball of flame.....\n")
    state = state['bprintf'](state, "Unfortunately you seem to have been fried\n")
    raise PlayerIsDead("Whoops.....   Frying tonight")


def dragget():
    raise NotImplementedError()


def helpchkr():
    raise NotImplementedError()
