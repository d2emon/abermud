from .errors import PlayerIsDead, PlayerLoose
from .opensys import close_world, open_world
from .support import Item, Player, pname
from .sys_log import logger


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


def bloodrcv(state, array, isme):
    try:
        #
        logger.debug("%s slain by %s", state['name'], pname(array[0]))
        #
        raise PlayerLoose("Oh dear... you seem to be slightly dead")
    except PlayerLoose as e:
        close_world(state)

        delpers(state['name'])

        state = open_world(state)
        sendsys(
            state['name'],
            state['name'],
            -10000,
            state['curch'],
            "[p]{}[/p] has just died.\n".format(state['name']),
        )
        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[ [p]{}[/p] has been slain by [p]{}[/p] ]\n".format(state['name'], pname(array[0])),
        )
        raise PlayerIsDead(e)
