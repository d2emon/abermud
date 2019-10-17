from .errors import PlayerIsDead, PlayerLoose
from .opensys import close_world, open_world
from .support import Item, Player, pname
from .sys_log import logger


def hitplayer(state, victim_id, weapon_id):
    victim = Player(state, victim_id)
    weapon = Item(state, weapon_id)

    if not victim.is_alive:
        return state

    # Chance to hit stuff
    if not iscarrby(weapon, state['mynum']) and weapon.item_id != -1:
        state = state['bprintf'](state, "You belatedly realise you dont have the {},\nand are forced to use your hands instead..\n".format(oname(weapon.item_id)))
        if state['wpnheld'] == weapon.item_id:
            weapon = None

    state['wpnheld'] = weapon.item_id if weapon else -1
    if weapon and weapon.item_id == 32 and iscarrby(Item(state, 16), victim):
        return state['bprintf'](state, "The runesword flashes back away from its target, growling in anger!\n")
    if dambyitem(weapon.item_id if weapon else -1) < 0:
        state['wpnheld'] = -1
        return state['bprintf'](state, "Thats no good as a weapon\n")
    if state["in_fight"]:
        return state['bprintf'](state, "You are already fighting!\n")

    state.update({
        'in_fight': 300,
        'fighting': victim.player_id,
    })

    res = randperc()
    cth = 40 + 3 * state['my_lev']
    if iswornby(Item(state, 89), victim) or iswornby(Item(state, 113), victim) or iswornby(Item(state, 114), victim):
        cth -= 10
    if cth < 0:
        cth = 0
    if cth > res:
        state = state['bprintf'](state, "You hit [p]{}[/p] ".format(victim.name))
        if weapon:
            state = state['bprintf'](state, "with the {}".format(oname(weapon.item_id)))
        state = state['bprintf'](state, "\n")

        damage = randperc() % dambyitem(weapon.item_id if weapon else -1)
        if victim.strength < damage:
            state = state['bprintf'](state, "Your last blow did the trick\n")
            state['my_sco'] += victim.kill()
            state.update({
                'in_fight': 0,
                'fighting': -1,
            })
        if victim.player_id < 16:
            state = sendsys(
                state,
                victim.name,
                state['name'],
                -10021,
                state['curch'],
                [
                    state['mynum'],
                    damage,
                    weapon.item_id if weapon else -1,
                ],
            )
        else:
            state = woundmn(state, victim.player_id, damage)
        state['my_sco'] += damage * 2
        return calibme(state)

    state = state['bprintf'](state, "You missed [p]{}[/p]\n".format(victim.name))
    if victim.player_id < 16:
        return sendsys(
            state,
            victim.name,
            state['name'],
            -10021,
            state['curch'],
            [
                state['mynum'],
                -1,
                weapon.item_id if weapon else -1,
            ],
        )
    else:
        return woundmn(state, victim.player_id, 0)


def killcom(state):
    def xwisc(victim):
        weapon = Item(state, state['wpnheld'])
        if brkword() != -1:
            if state['wordbuf'] == 'with':
                if brkword() == -1:
                    return state['bprintf'](state, "with what ?\n")
            else:
                return xwisc(victim)

            weapon = Item(state, fobnc(state['wordbuf']))
            if weapon.item_id == -1:
                return state['bprintf'](state, "with what ?\n")

        return hitplayer(victim.item_id, weapon.item_id)

    if brkword() == -1:
        return state['bprintf'](state, "Kill who\n")
    if state['wordbuf'] == "door":
        return state['bprintf'](state, "Who do you think you are, Moog?\n")

    item = Item(state, fobna(state['wordbuf']))
    if item.item_id != -1:
        return breakitem(state, item.item_id)

    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id != -1:
        return state['bprintf'](state, "You can't do that\n")
    if player.player_id == state['mynum']:
        return state['bprintf'](state, "Come on, it will look better tomorrow...\n")
    if player.location != state['curch']:
        return state['bprintf'](state, "They aren't here\n")
    return xwisc(player)


def bloodrcv(state, data, is_me):
    if not is_me:
        return state

    enemy_id, damage, weapon_id = data
    if enemy_id < 0:
        return state

    enemy = Player(state, enemy_id)
    weapon = Item(state, weapon_id)
    if not enemy.is_alive:
        return state

    state.update({
        'in_fight': 300,
        'fighting': enemy.player_id,
    })

    if damage == -1:
        state = state['bprintf'](state, "[p]{}[/p] attacks you".format(enemy.name))
        if weapon.item_id != -1:
            state = state['bprintf'](state, "with the {}".format(oname(weapon.item_id)))
        return state['bprintf'](state, "\n")

    state = state['bprintf'](state, "You are wounded by [p]{}[/p]".format(enemy.name))
    if weapon.item_id != -1:
        state = state['bprintf'](state, "with the {}".format(oname(weapon.item_id)))
    state = state['bprintf'](state, "\n")

    if state['my_lev'] >= 10:
        return state

    try:
        state['my_str'] -= damage

        if enemy.player_id == 16:
            state = state['bprintf'](state, "You feel weaker, as the wraiths icy touch seems to drain your very life force\n")

            state['my_sco'] -= 100 * damage
            if state['my_sco'] < 0:
                state['my_str'] = -1

        state['me_cal'] = True

        if state['my_str'] < 0:
            raise PlayerLoose("Oh dear... you seem to be slightly dead")
    except PlayerLoose as e:
        logger.debug("%s slain by %s", state['name'], enemy.name)
        dumpitems()
        close_world(state)

        delpers(state['name'])

        state = open_world(state)
        sendsys(
            state,
            state['name'],
            state['name'],
            -10000,
            state['curch'],
            "[p]{}[/p] has just died.\n".format(state['name']),
        )
        sendsys(
            state,
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[ [p]{}[/p] has been slain by [p]{}[/p] ]\n".format(state['name'], enemy.name),
        )
        raise PlayerIsDead(e)
