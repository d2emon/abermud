from .support import Item, Player


def sumcom(state):
    def willwork(new_state, to_summon):
        new_state = new_state['bprintf'](new_state, "You cast the summoning......\n")
        if to_summon.player_id < 16:
            return sendsys(
                new_state,
                to_summon.name,
                state['name'],
                -10020,
                state['curch'],
                '',
            )
        if to_summon.player_id == 17 or to_summon.player_id == 23:
            return new_state
        dumpstuff(to_summon.player_id, to_summon.location)
        new_state = sendsys(
            new_state,
            None,
            None,
            -10000,
            state['curch'],
            "[s name =\"{}\"]{} has arrived\n[/s]".format(to_summon.name, to_summon.name),
        )
        to_summon.location = state['curch']
        return new_state

    def sumob(new_state, to_summon):
        if new_state['my_lev'] < 10:
            return new_state['bprintf'](new_state, "You can only summon people\n")
        """
    bprintf("The %s flies into your hand ,was ",oname(a));
    desrm(oloc(a),ocarrf(a));
    setoloc(a,mynum,1);
        
        :param new_state: 
        :return: 
        """
        x = to_summon.location
        if to_summon.owned_by:
            x = Player(state, to_summon.owned_by).location
        sendsys(
            new_state['name'],
            new_state['name'],
            -10000,
            x,
            "[p]{}[/p] has summoned the {}\n".format(new_state['name'], oname(to_summon.item_id)),
        )
        new_state = new_state['bprintf'](new_state, "The {} flies into your hand  was ".format(oname(to_summon.item_id)))
        desrm(to_summon.location, to_summon.carry_flag)
        item.carried_by = state['mynum']
        return new_state

    if brkword() == -1:
        return state['bprintf'](state, "Summon who?\n")

    item = Item(state, fobn(state['wordbuf']))
    if item.item_id != -1:
        return sumob(state, item)

    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id == -1:
        return state['bprintf'](state, "I dont know who that is\n")

    if state['my_str'] < 10:
        return state['bprintf'](state, "You are too weak\n")

    if state['my_lev'] < 10:
        state['my_str'] -= 2

    c = state['my_lev'] * 2
    if state['my_lev'] > 9:
        c = 101
    if iscarrby(111, state['mynum']):
        c += state['my_lev']
    if iscarrby(121, state['mynum']):
        c += state['my_lev']
    if iscarrby(163, state['mynum']):
        c += state['my_lev']

    d = randperc()

    if state['my_lev'] > 9:
        return willwork(state, player)
    if iswornby(90, player.player_id) or c < d:
        return state['bprintf'](state, "The spell fails....\n")
    if player.player_id == fpbn("wraith") or iscarrby(32, player.player_id) or iscarrby(159, player.player_id) or iscarrby(174, player.player_id):
        return state['bprintf'](state, "Something stops your summoning from succeeding\n")
    if player.player_id == state['mynum']:
        return state['bprintf'](state, "Seems a waste of effort to me....\n")
    if -1076 >= state['curch'] >= -1082:
        return state['bprintf'](state, "Something about this place makes you fumble the magic\n")

    return willwork(state, player)


def goloccom(state):
    state = change_channel(state, a)


def viscom(state):
    if state['my_lev'] < 10:
        return state['bprintf'](state, "You can't just do that sort of thing at will you know.\n")
    if state['me'].is_visible(0):
        return state['bprintf'](state, "You already are visible\n")
    state['me'].visible = 0
    state = sendsys(
        state,
        None,
        None,
        -9900,
        0,
        [
            state['mynum'],
            state['me'].visible,
        ]
    )
    state = state['bprintf'](state, "Ok\n")
    return sillycom(state, "[s name=\"{}\"]{} suddenely appears in a puff of smoke\n[/s]")


def inviscom(state):
    if state['my_lev'] < 10:
        return state['bprintf'](state, "You can't just turn invisible like that!\n")
    level = 10000 if state['my_lev'] > 9999 else 10
    if state['my_lev'] == 10033 and brkword() != -1:
        level = int(state['wordbuf'])
    if state['me'].is_visible(level):
        return state['bprintf'](state, "You are already invisible\n")
    state['me'].visible = level
    state = sendsys(
        state,
        None,
        None,
        -9900,
        0,
        [
            state['mynum'],
            state['me'].visible,
        ]
    )
    state = state['bprintf'](state, "Ok\n")
    return sillycom(state, "[c]{} vanishes!\n[/s]")


def ressurcom(state):
    if state['my_lev'] < 10:
        return state['bprintf'](state, "Huh?\n")

    if brkword() == -1:
        return state['bprintf'](state, "Yes but what?\n")

    item = Item(state, fobn(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "You can only ressurect objects\n")
    if ospare(item.item_id) != -1:
        return state['bprintf'](state, "That already exists\n")
    ocreate(item.item_id)
    item.located_at = state['curch']
    sendsys(
        state,
        None,
        None,
        -10000,
        state['curch'],
        "The {} suddenly appears\n".format(oname(item.item_id)),
    )
    return state
