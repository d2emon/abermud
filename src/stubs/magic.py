from .support import Item


def sumcom(state):
    def willwork(new_state, to_summon):
        new_state = new_state['bprintf'](new_state, "You cast the summoning......\n")
        if to_summon.player_id < 16:
            return sendsys(
                new_state,
                pname(to_summon.player_id),
                state['name'],
                -10020,
                state['curch'],
                '',
            )
        if to_summon.player_id == 17 or to_summon.player_id == 23:
            return new_state
        dumpstuff(to_summon.player_id, ploc(to_summon.player_id))
        new_state = sendsys(
            new_state,
            None,
            None,
            -10000,
            state['curch'],
            "[s name =\"{}\"]{} has arrived\n[/s]".format(pname(to_summon.player_id), pname(to_summon.player_id)),
        )
        setploc(to_summon.player_id, state['curch'])
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
        if to_summon.carry_flag != Item.LOCATED_AT:
            x = ploc(x)
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

    player = fpbn(state['wordbuf'])
    if player == -1:
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
