from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import Item, Player
from .sys_log import logger


def ohereandget(state):
    #
    state = open_world(state)
    #


def opencom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    elif item.item_id == 21:
        if state(item.item_id) == 1:
            return state['bprintf'](state, "It is\n")
        else:
            return state['bprintf'](state, "It seems to be magically closed\n")
    elif item.item_id == 1:
        if state(item.item_id) != 0:
            return state['bprintf'](state, "It is!\n")
        else:
            item.item_id.state = 1
            return state['bprintf'](state, "The Umbrella Opens\n")
    elif item.item_id == 20:
        return state['bprintf'](state, "You can't shift the door from this side!!!!\n")
    else:
        if not item.can_open:
            return state['bprintf'](state, "You can't open that\n")
        if state(item.item_id) == 0:
            return state['bprintf'](state, "It already is\n")
        if state(item.item_id) == 2:
            return state['bprintf'](state, "It's locked!\n")
        item.state = 0
        return state['bprintf'](state, "Ok\n")


def closecom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    elif item.item_id == 1:
        if state(item.item_id) == 0:
            return state['bprintf'](state, "It is closed, silly!\n")
        else:
            item.state = 0
            return state['bprintf'](state, "Ok\n")
    else:
        if not item.can_open:
            return state['bprintf'](state, "You can't close that\n")
        if state(item.item_id) != 0:
            return state['bprintf'](state, "It is open already\n")
        if state(item.item_id) == 2:
            return state['bprintf'](state, "It's locked!\n")
        item.state = 1
        return state['bprintf'](state, "Ok\n")


def lockcom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    elif not Item.find(state, lambda i: i.is_key):
        return state['bprintf'](state, "You haven't got a key\n")
    else:
        if not item.can_lock:
            return state['bprintf'](state, "You can't lock that!\n")
        if state(item.item_id) == 2:
            return state['bprintf'](state, "It's already locked\n")
        item.state = 2
        return state['bprintf'](state, "Ok\n")


def unlockcom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    elif not Item.find(state, lambda i: i.is_key):
        return state['bprintf'](state, "You have no keys\n")
    else:
        if not item.can_lock:
            return state['bprintf'](state, "You can't unlock that\n")
        if state(item.item_id) != 2:
            return state['bprintf'](state, "It's not locked!\n")
        item.state = 1
        return state['bprintf'](state, "Ok\n")


def wavecom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    elif item.item_id == 136:
        bridge = Item(state, 151)
        if state(bridge.item_id) == 1 or bridge.location == state['curch']:
            setstate(150, 0)
            return state['bprintf'](state, "The drawbridge is lowered!\n")
    elif item.item_id == 158:
        teletrap(-114)
        return state['bprintf'](state, "You are teleported!\n")
    return state['bprintf'](state, "Nothing happens\n")


def putcom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state

    if brkword() == -1:
        return state['bprintf'](state, "where?\n")

    if state['wordbuf'] in ('on', 'in') and brkword() == -1:
        return state['bprintf'](state, "What?\n")

    location = Item(state, fobna(state['wordbuf']))
    if location.item_id == -1:
        return state['bprintf'](state, "There isn't one of those here.\n")
    elif location.item_id == 10:
        if item.item_id < 4 or item.item_id > 6:
            return state['bprintf'](state, "You can't do that\n")
        if state(location.item_id) != 2:
            return state['bprintf'](state, "There is already a candle in it!\n")
        return state['bprintf'](state, "The candle fixes firmly into the candlestick\n")
        state['my_sco'] += 50
        item.destroy()
        location.bytes[1] = item.item_id
        location.can_light = True
        location.can_extinguish = True
        location.is_lit = item.is_lit
        if location.is_lit:
            location.state = 0
        else:
            location.state = 1
        return state
    elif location.item_id == 137:
        if state(location.item_id) == 0:
            item.located_at = -162
            return state['bprintf'](state, "ok\n")
        item.destroy()
        state = state['bprintf'](state, "It dissappears with a fizzle into the slime\n")
        if item.item_id == 108:
            state = state['bprintf'](state, "There isn't one of those here.\n")
            location.state = 0
        return state
    elif location.item_id == 193:
        return state['bprintf'](state, "You can't do that, the chute leads up from here!\n")
    elif location.item_id == 192:
        if item.item_id == 32:
            return state['bprintf'](state, "You can't let go of it!\n")
        state = state['bprintf'](state, "It vanishes down the chute....\n")
        chute = Item(state, 193)
        sendsys(
            state,
            None,
            None,
            -10000,
            chute.location,
            "The {} comes out of the chute!\n".format(item.name),
        )
        item.located_at = chute.location
        return state
    elif location.item_id == 23:
        if item.item_id == 19 and state(21) == 1:
            state = state['bprintf'](state, "The door clicks open!\n")
            Item(state, 20).state = 0
            return state
        return state['bprintf'](state, "Nothing happens\n")
    elif location.item_id == item.item_id:
        return state['bprintf'](state, "What do you think this is, the goon show?\n")

    if not location.is_container:
        return state['bprintf'](state, "You can't do that\n")
    if location.state != 0:
        return state['bprintf'](state, "That's not open\n")
    if not item.is_movable:
        return state['bprintf'](state, "You can't take that!\n")
    if dragget():
        return state
    if item.item_id == 32:
        return state['bprintf'](state, "You can't let go of it!\n")
    item.contained_in = location.item_id
    state = state['bprintf'](state, "Ok.\n")
    sendsys(
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "[D]{}[/D][c] puts the {} in the {}.\n[c]".format(state['name'], item.name, location.name),
    )
    if item.turn_on_put:
        item.state = 0
    if state['curch'] == -1081:
        Item(state, 20).state = 1
        state = state['bprintf'](state, "The door clicks shut....\n")
    return state


def lightcom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    if not Item.find(state, lambda i: i.is_lit):
        return state['bprintf'](state, "You have nothing to light things from\n")
    # By item_id
    # Default
    if not item.can_light:
        return state['bprintf'](state, "You can't light that!\n")
    if state(item.item_id):
        return state['bprintf'](state, "It is lit\n")
    item.state = 0
    item.is_lit = True
    return state['bprintf'](state, "Ok\n")


def extinguishcom(state):
    item = Item(state, ohereandget(state))
    if item.item_id == -1:
        return state
    # By item_id
    # Default
    if not item.is_lit:
        return state['bprintf'](state, "That isn't lit\n")
    if not item.can_extinguish:
        return state['bprintf'](state, "You can't extinguish that!\n")
    item.state = 1
    item.is_lit = False
    return state['bprintf'](state, "Ok\n")


def pushcom(state):
    if brkword() == -1:
        return state['bprintf'](state, "Push what ?\n")

    item = Item(state, fobna(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "That is not here\n")
    elif item.item_id == 126:
        state = state['bprintf'](state, "The tripwire moves and a huge stone crashes down from above!\n")
        broad(world, "[d]You hear a thud and a squelch in the distance.\n[/d]")
        raise PlayerIsDead("             S   P    L      A         T           !")
    elif item.item_id == 162:
        state = state['bprintf'](state, "A trapdoor opens at your feet and you plumment downwards!\n")
        return change_channel(state, -140)
    elif item.item_id == 130:
        panel = Item(state, 132)
        if panel.state == 1:
            panel.state = 0
            return state['bprintf'](state, "A secret panel opens in the east wall!\n")
        else:
            return state['bprintf'](state, "Nothing happens\n")
    elif item.item_id == 131:
        hole = Item(state, 134)
        if hole.state == 1:
            hole.state = 0
            state = state['bprintf'](state, "Uncovering a hole behind it.\n")
        return state
    elif item.item_id == 138:
        connected = Item(state, 137)
        if connected.state == 1:
            connected.state = 0
            return state['bprintf'](state, "You hear a gurgling noise and then silence.\n")
        else:
            return state['bprintf'](state, "Ok...\n")
    elif item.item_id in (146, 147):
        connected = Item(state, 146)
        connected.state = 1 - connected.state
        return state['bprintf'](state, "Ok...\n")
    elif item.item_id == 30:
        connected = Item(state, 28)
        connected.state = 1 - connected.state
        if connected.state:
            sendsys(
                state,
                None,
                None,
                -10000,
                connected.location,
                "[c]The portcullis falls\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 29).location,
                "[c]The portcullis falls\n[/c]",
            )
        else:
            sendsys(
                state,
                None,
                None,
                -10000,
                connected.location,
                "[c]The portcullis rises\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 29).location,
                "[c]The portcullis rises\n[/c]",
            )
        return state
    elif item.item_id == 149:
        connected = Item(state, 150)
        connected.state = 1 - connected.state
        if connected.state:
            sendsys(
                state,
                None,
                None,
                -10000,
                connected.location,
                "[c]The drawbridge rises\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 151).location,
                "[c]The drawbridge rises\n[/c]",
            )
        else:
            sendsys(
                state,
                None,
                None,
                -10000,
                connected.location,
                "[c]The drawbridge is lowered\n[/c]",
            )
            sendsys(
                state,
                None,
                None,
                -10000,
                Item(state, 151).location,
                "[c]The drawbridge is lowered\n[/c]",
            )
        return state
    elif item.item_id == 24:
        connected = Item(state, 26)
        if connected.state == 1:
            connected.state = 0
            return state['bprintf'](state, "A secret door slides quietly open in the south wall!!!\n")
        else:
            return state['bprintf'](state, "It moves but nothing seems to happen\n")
    elif item.item_id == 49:
        return broad(world, "[d]Church bells ring out around you\n[/d]")
    elif item.item_id == 104:
        if state['me'].helper is None:
            return state['bprintf'](state, "You can't shift it alone, maybe you need help\n")

    if item.is_turnable:
        item.state = 0
        oplong(item.item_id)
        return state
    elif item.is_switchable:
        item.state = 1 - item.state
        oplong(item.item_id)
        return state
    else:
        return state['bprintf'](state, "Nothing happens\n")


def cripplecom(state):
    target = Player(state, victim())
    if target.player_id == -1:
        return state
    return sendsys(
        state,
        target.name,
        state['name'],
        -10101,
        state['curch'],
        "",
    )


def curecom(state):
    target = Player(state, vichfb())
    if target.player_id == -1:
        return state
    return sendsys(
        state,
        target.name,
        state['name'],
        -10100,
        state['curch'],
        "",
    )


def dumbcom(state):
    target = Player(state, victim())
    if target.player_id == -1:
        return state
    return sendsys(
        state,
        target.name,
        state['name'],
        -10102,
        state['curch'],
        "",
    )


def forcecom(state):
    target = Player(state, victim())
    if target.player_id == -1:
        return state
    return sendsys(
        state,
        target.name,
        state['name'],
        -10103,
        state['curch'],
        getreinput(),
    )


def missilecom(state):
    target = Player(state, vichfb())
    if target.player_id == -1:
        return state
    damage = 2 * state['my_lev']
    state = sendsys(
        state,
        target.name,
        state['name'],
        -10106,
        state['curch'],
        damage,
    )
    if target.strength < damage:
        state = state['bprintf'](state, "Your last spell did the trick\n")
        state['my_sco'] += target.kill()
        state.update({
            'in_fight': 0,
            'fighting': -1,
        })
    if target.player_id > 15:
        state = woundmn(state, target.player_id, damage)
    return state


def changecom(state):
    if brkword() == -1:
        return state['bprintf'](state, "change what (Sex ?) ?\n")
    if state['wordbuf'] != 'sex':
        return state['bprintf'](state, "I don't know how to change that\n")

    target = Player(state, victim())
    if target.player_id == -1:
        return state
    state = sendsys(
        state,
        target.name,
        state['name'],
        -10107,
        state['curch'],
        "",
    )
    if target.player_id >= 16:
        target.sex = Player.male if target.sex == Player.female else Player.female
    return state


def fireballcom(state):
    target = Player(state, vichfb())
    if target.player_id == -1:
        return state
    if target.player_id == state['mynum']:
        return state['bprintf'](state, "Seems rather dangerous to me....\n")

    multiplier = 6 if target.player_id == fpbns('yeti') else 2
    damage = multiplier * state['my_lev']
    if target.strength < damage:
        state = state['bprintf'](state, "Your last spell did the trick\n")
        state['my_sco'] += target.kill()
        state.update({
            'in_fight': 0,
            'fighting': -1,
        })

    state = sendsys(
        state,
        target.name,
        state['name'],
        -10109,
        state['curch'],
        damage,
    )

    if target.player_id > 15:
        state = woundmn(state, target.player_id, damage)
    return state


def shockcom(state):
    target = Player(state, vichfb())
    if target.player_id == -1:
        return state
    if target.player_id == state['mynum']:
        return state['bprintf'](state, "You are supposed to be killing other people not yourself\n")

    damage = 2 * state['my_lev']
    if target.strength < damage:
        state = state['bprintf'](state, "Your last spell did the trick\n")
        state['my_sco'] += target.kill()
        state.update({
            'in_fight': 0,
            'fighting': -1,
        })

    state = sendsys(
        state,
        target.name,
        state['name'],
        -10110,
        state['curch'],
        damage,
    )

    if target.player_id > 15:
        state = woundmn(state, target.player_id, damage)
    return state


def starecom(state):
    target = Player(state, vichere())
    if target.player_id == -1:
        return state
    if target.player_id == state['mynum']:
        return state['bprintf'](state, "That is pretty neat if you can do it!\n")

    sillytp(target.player_id, "stares deep into your eyes\n")
    return state['bprintf'](state, "You stare at [p]{}[/p]\n")


def gropecom():
    #
    raise PlayerIsDead("Bye....... LINE TERMINATED - MORALITY REASONS")
    #


def vicbase(state, x):
    #
    state = open_world(state)
    #


def vichere(state, player_id):
    player = Player(state, vicbase(state, player_id))
    if player.player_id == -1:
        return player.player_id
    if player.location != state['curch']:
        state = state['bprintf'](state, "They are not here\n")
        return -1
    return player.player_id


def vichfb(state, player_id):
    player = Player(state, vicfb(state, player_id))
    if player.player_id == -1:
        return -1
    if player.location != state['curch']:
        state = state['bprintf'](state, "They are not here\n")
        return -1
    return player.player_id


def sillytp(state, player_id, message):
    if message[:4] == "star":
        text = "[s name=\"{}\"]{} {}\n[/s]".format(state['name'], state['name'], message)
    else:
        text = "[p]{}[/p] {}\n".format(state['name'], message)

    player = Player(state, player_id)
    return sendsys(
        state,
        player.name,
        state['name'],
        -10111,
        state['curch'],
        text,
    )


def tscale(state):
    players = (Player(state, player_id) for player_id in range(16))
    count = len(list(filter(lambda player: player.is_alive, players)))
    if count == 1:
        return 2
    elif count == 2:
        return 3
    elif count == 3:
        return 3
    elif count == 4:
        return 4
    elif count == 5:
        return 4
    elif count == 6:
        return 5
    elif count == 7:
        return 6
    return 7


def wounded(state, n):
    #
    close_world(state)
    logger.debug("%s slain magically", state['name'])
    #
    state = open_world(state)
    #
    sendsys(
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "{} has just died\n".format(state['name']),
    )
    sendsys(
        state['name'],
        state['name'],
        -10113,
        state['curch'],
        "[ {} has just died ]\n".format(state['name']),
    )
    raise PlayerIsDead("Oh dear you just died")
    #


def woundmn(state, mobile_id, damage):
    mobile = Player(state, mobile_id)

    mobile.strength -= damage
    if mobile.strength >= 0:
        return mhitplayer(state, mobile.player_id, state['mynum'])

    dumpstuff(mobile.player_id, mobile.location)
    sendsys(
        state,
        None,
        None,
        -10000,
        mobile.location,
        "{} has just died\n".format(mobile.name),
    )
    sendsys(
        state,
        state['name'],
        state['name'],
        -10113,
        mobile.location,
        "[ {} has just died ]\n".format(mobile.name),
    )
    mobile.destroy()
    return state


def mhitplayer(state, mobile_id, player_id):
    mobile = Player(state, mobile_id)
    if mobile.location != state['curch']:
        return state
    if mobile.player_id < 0 or mobile.player_id > 47:
        return state

    a = randperc()
    b = 3 * (15 - state['my_lev']) + 20
    if iswornby(Item(state, 89), state['mynum']) or iswornby(Item(state, 113), state['mynum']) or iswornby(Item(state, 114), state['mynum']):
        b -= 10

    if a < b:
        return sendsys(
            state,
            state['name'],
            mobile.name,
            -10021,
            mobile.location,
            [
                mobile.player_id,
                randperc() % damof(mobile.player_id),
                -1,
            ],
        )
    else:
        return sendsys(
            state,
            state['name'],
            mobile.name,
            -10021,
            mobile.location,
            [
                mobile.player_id,
                -1,
                -1,
            ],
        )


def resetplayers(state):
    for player_id in range(16, 35):
        player = Player(state, player_id)
        data = pinit[player_id - 16]

        player.name = data.name
        player.location = data.location
        player.strength = data.strength
        player.sex = data.sex
        player.weapon = None
        player.visibility = 0
        player.level = data.level

    for player_id in range(35, 48):
        player = Player(state, player_id)
        player.destroy()


def iswornby(item, player):
    if not iscarrby(item, player):
        return False
    return item.carry_flag == Item.WORN_BY


def canwear(state, item_id):
    item = Item(state, item_id)
    return item.can_wear


def deafcom(state):
    target = Player(state, victim())
    if target.player_id == -1:
        return state
    return sendsys(
        state,
        target.name,
        state['name'],
        -10120,
        state['curch'],
        "",
    )


def blindcom(state):
    target = Player(state, victim())
    if target.player_id == -1:
        return state
    return sendsys(
        state,
        target.name,
        state['name'],
        -10105,
        state['curch'],
        "",
    )


def teletrap(state):
    state = change_channel(state, newch)


def on_flee_event(state):
    for item_id in range(state['numobs']):
        item = Item(state, item_id)
        if iscarrby(item, state['mynum']) and not iswornby(item, state['mynum']):
            item.located_at = state['me'].location
