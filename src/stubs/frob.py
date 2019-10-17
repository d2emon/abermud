from .opensys import open_world


def frobnicate(state):
    if state['my_lev'] < 10000:
        return state['bprintf'](state, "No way buster.\n")
    if brkword() == -1:
        return state['bprintf'](state, "Frobnicate who ?\n")
    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id > 15 and state['my_lev'] != 10033:
        return state['bprintf'](state, "Can't frob mobiles old bean.\n")
    if player.level > 9999 and state['my_lev'] != 10033:
        return state['bprintf'](state, "You can't frobnicate {}!!!!\n".format(player.name))

    keysetback()

    state = state['bprintf'](state, "New Level: ")
    state = state['pbfr'](state)
    bf1 = input()[:6]

    state = state['bprintf'](state, "New Score: ")
    state = state['pbfr'](state)
    bf2 = input()[:8]

    state = state['bprintf'](state, "New Strength: ")
    state = state['pbfr'](state)
    bf3 = input()[:8]

    keysetup()

    state = open_world(state)
    state = sendsys(
        state,
        player.name,
        player.name,
        -599,
        0,
        [
            bf1,
            bf2,
            bf3,
        ]
    )
    return state['bprintf'](state, "Ok....\n")
