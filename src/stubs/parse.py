from datetime import datetime
from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import Item, Player, pname
from .sys_log import logger
from .tk.back import set_message_id, process_messages
from .tk.message import Message


def sendsys(world, receiver, sender, codeword, channel, text):
    message = Message(
        channel,
        codeword,
        receiver,
        sender,
        text,
    )
    world.send_message(message)
    return world.state


def doaction(state, n):
    state = open_world(state)
    #
    if n == 8:
        if state['is_force']:
            return state['bprintf'](state, "You can't be forced to do that\n")
        state = process_messages(state, state['mynum'], state['cms'])
        state = open_world(state)
        if state['in_fight']:
            return state['bprintf'](state, "Not in the middle of a fight!\n")
        state = state['bprintf'](state, "Ok")
        state = sendsys(
            state,
            state['name'],
            state['name'],
            -10000,
            state['curch'],
            "{} has left the game\n".format(state['name']),
        )
        state = sendsys(
            state,
            state['name'],
            state['name'],
            -10113,
            0,
            "[ Quitting Game : {} ]\n".format(state['name']),
        )
        dumpitems()
        state['me'].kill()
        state['me'].destroy()
        close_world(state)
        state.update({
            'curmode': 0,
            'curch': 0
        })
        saveme()
        raise PlayerIsDead("Goodbye")


def dodirn(state, n):
    if state['in_fight'] > 0:
        state = state['bprintf'](state, "You can't just stroll out of a fight!\n")
        state = state['bprintf'](state, "If you wish to leave a fight, you must FLEE in a direction\n")
        return state

    golem = Player(state, 25)
    if iscarrby(32, state['mynum']) and golem.location == state['curch'] and golem.is_alive:
        return state['bprintf'](state, "[c]The Golem[/c] bars the doorway!\n")

    if chkcrip():
        return state

    n -= 2
    newch = ex_dat[n]

    if 999 < newch < 2000:
        door = Item(state, newch - 1000)
        droff = Item(state, door.item_id ^ 1)  # other door side
        if state(door.item_id) != 0:
            if door.name != 'door' or isdark() or len(door.description) == 0:
                return state['bprintf'](state, "You can't go that way\n")
            else:
                return state['bprintf'](state, "The door is not open\n")
        newch = droff.location

    if newch == -139:
        if not iswornby(113, state['mynum']) and  not iswornby(114, state['mynum']) and  not iswornby(89, state['mynum']):
            return state['bprintf'](state, "The intense heat drives you back\n")

        state = state['bprintf'](state, "The shield protects you from the worst of the lava stream's heat\n")

    if n == 2:
        figure = Player(state, fpbns('figure'))
        if figure.player_id != state['mynum'] and figure.player_id != -1 and figure.location == state['curch'] and not iswornby(101, state['mynum']) and not iswornby(102, state['mynum']) and not iswornby(103, state['mynum']):
            state = state['bprintf'](state, "[p]The Figure[/p] holds you back\n")
            state = state['bprintf'](state, "[p]The Figure[/p] says 'Only true sorcerors may pass'\n")
            return state

    if newch >= 0:
        return state['bprintf'](state, "You can't go that way\n")

    sendsys(
        state,
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "[s name=\"{}\"]{} has gone {} {}.[/s]".format(state['me'].name, state['name'], exittxt[n], state['out_ms']),
    )
    state = change_channel(state, newch)
    sendsys(
        state,
        state['name'],
        state['name'],
        -10000,
        state['curch'],
        "[s name=\"{}\"]{} {}\n[/s]".format(state['name'], state['name'], state['in_ms']),
    )
    return state


def gamrcv(state, message):
    if state['debug_mode']:
        state = state['bprintf'](state, "\n<{}>".format(message.code))

    is_me = message.is_me(state['name'].lower())
    is_here = message.channel == state['curch']

    if message.code >= -3:
        return state['bprintf'](state, message.text)
    elif message.code == -20000 and fpbns(message.receiver) == state['fighting']:
        state['in_fight'] = 0
        state['fighting'] = -1
    elif message.code < -10099:
        return new1rcv(state, is_me, message.channel, message.receiver, message.sender, message.code, message.text)
    elif message.code == -401 and is_me:
        state.update({'snoopd', fpbns(message.sender)})
    elif message.code == -599 and is_me:
        state.update({
            'my_lev': message.text[0],
            'my_sco': message.text[1],
            'my_str': message.text[2],
        })
        state = calibme(state)
    elif message.code == -666:
        state['bprintf'](state, "Something Very Evil Has Just Happened...\n")
        raise PlayerIsDead("Bye Bye Cruel World....")
    elif message.code == -400 and is_me:
        state.update({'snoopd', -1})
    elif message.code == -750 and is_me:
        if fpbns(message.sender) != -1:
            raise PlayerIsDead("***HALT")

        close_world(state)
        raise SystemExit("***HALT")
    elif message.code == -9900:
        Player(state, message.text[0]).visibility = message.text[1]
    elif message.code == -10000 and not is_me and is_here:
        return state['bprintf'](state, message.text)
    elif message.code == -10001:
        if not is_me:
            return state['bprintf'](state, "[c]A massive lightning bolt strikes [/c][D]{}[/D][c]\n[/c]".format(message.receiver))
        if state['my_lev'] > 10:
            return state['bprintf'](state, "[p]{}[/p] cast a lightning bolt at you\n".format(message.sender))
        # You are in the ....
        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[ [p]{}[/p] has just been zapped by [p]{}[/p] and terminated ]\n".format(state['name'], message.sender),
        )
        state = state['bprintf'](
            state,
            "A massive lightning bolt arcs down out of the sky to strike you between\n"
            "the eyes\n",
        )
        state['zapped'] = True
        delpers(state['name'])
        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[s name=\"{}\"]{} has just died.\n[/s]".format(state['name'], state['name']),
        )
        state['bprintf'](state, "You have been utterly destroyed by {}\n".format(message.sender))
        raise PlayerIsDead("Bye Bye.... Slain By Lightning")
    elif message.code == -10002 and not is_me:
        if is_here or state['my_lev'] > 9:
            return state['bprintf'](state, "[P]{}[/P][d] shouts '{}'\n[/d]".format(message.sender, message.text))
        return state['bprintf'](state, "[d]A voice shouts '{}'\n[/d]".format(message.text))
    elif message.code == -10003 and not is_me and is_here:
        return state['bprintf'](state, "[P]{}[/P][d] says '{}'\n[/d]".format(message.sender, message.text))
    elif message.code == -10004 and is_me:
        return state['bprintf'](state, "[P]{}[/P][d] tells you '{}'\n[/d]".format(message.sender, message.text))
    elif message.code == -10010:
        if not is_me:
            return state['bprintf'](state, "{} has been kicked off\n".format(message.receiver))
        raise PlayerIsDead("You have been kicked off")
    elif message.code == -10011 and is_me:
        return state['bprintf'](state, message.text)
    elif message.code == -10020 and is_me:
        state['ades'] = message.channel
        if state['my_lev'] < 10:
            summon_message = "You drop everything you have as you are summoned by [p]{}[/p]\n".format(message.sender)
            state['tdes'] = 1
        else:
            summon_message = "[p]{}[/p] tried to summon you\n".format(message.sender)
        return state['bprintf'](state, summon_message)
    elif message.code == -10021 and is_me and is_here:
        state.update({
            'rdes': 1,
            'vdes': message.text[0],
        })
        return bloodrcv(state, message.text, is_me)
    elif message.code == -10030:
        wthrrcv(message.channel)
    return state


def eorte(state):
    time = datetime.utcnow()
    if time - state['last_io_interrupt'] > 2:
        state['interrupt'] = True
    if state['interrupt']:
        state['last_io_interrupt'] = time

    if state['me_ivct']:
        state['me_ivct'] -= 1
    if state['me_ivct'] <= 1:
        state['me'].visibility = 0

    if state['me_cal']:
        state['me_cal'] = False
        state = calibme(state)

    if state['tdes']:
        dosumm(state['ades'])

    if state['in_fight']:
        enemy = Player(state, state['fighting'])
        if enemy.location != state['curch']:
            state.update({
                'fighting': -1,
                'in_fight': 0,
            })
        if not enemy.is_alive:
            state.update({
                'fighting': -1,
                'in_fight': 0,
            })
        if state['in_fight'] and state['interrupt']:
            state.update({'in_fight': 0})
            hitplayer(enemy.player_id, state['wpnheld'])
    if iswornby(18, state['mynum']) or randperc() < 10:
        state['my_str'] += 1
        if state['i_setup']:
            state = calibme(state)

    forchk()

    if state['me_drunk'] > 0:
        state['me_drunk'] -= 1
        if not state['ail_dumb']:
            gamecom('hiccup')

    state['interrupt'] = False
    return state


def rescom():
    b = RESET_DATA.connect('r').lock()
    b.unlock().disconnect()
    broad(world, "Reset in progress....\nReset Completed....\n")


def lightning(state):
    if state['my_lev'] < 10:
        return state['bprintf'](state, "Your spell fails.....\n")
    if brkword() == -1:
        return state['bprintf'](state, "But who do you wish to blast into pieces....\n")

    enemy = Player(state, fpbn(state['wordbuf']))
    if enemy.player_id == -1:
        return state['bprintf'](state, "There is no one on with that name\n")
    sendsys(
        state,
        enemy.name,
        state['globme'],
        -10001,
        enemy.location,
        "",
    )
    logger.debug("%s zapped %s", state['name'], enemy.name)
    if enemy.player_id > 15:
        state = woundmn(state, enemy.player_id, 10000)
    return broad(world, "[d]You hear an ominous clap of thunder in the distance\n[/d]")


def eatcom(state):
    if brkword() == -1:
        return state['bprintf'](state, "What\n")

    if state['curch'] == -609 and state['wordbuf'] == 'water':
        state['wordbuf'] = 'spring'
    if state['wordbuf'] == 'from':
        brkword()

    item = Item(state, fobna(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "There isn't one of those here\n")
    elif item.item_id == 11:
        state = state['bprintf'](state, "You feel funny, and then pass out\n")
        state = state['bprintf'](state, "You wake up elsewhere....\n")
        return teletrap(-1076)
    elif item.item_id == 75:
        return state['bprintf'](state, "very refreshing\n")
    elif item.item_id == 175:
        if state['my_lev'] < 3:
            state['my_sco'] += 40
            state = calibme(state)
            return state['bprintf'](state, "You feel a wave of energy sweeping through you.\n")
        else:
            if state['my_str'] < 40:
                state['my_sco'] += 2
            state = calibme(state)
            return state['bprintf'](state, "Faintly magical by the taste.\n")
    else:
        if item.is_edible:
            item.destroy()
            state['my_str'] += 12
            state = calibme(state)
            return state['bprintf'](state, "Ok....\n")
        else:
            return state['bprintf'](state, "Thats sure not the latest in health food....\n")


def calibme(state):
    if not state['i_setup']:
        return state
    b = levelof(state['my_sco'])
    if b != state['my_lev']:
        state['my_lev'] = b
        state = state['bprintf']("You are now {} ".format(state['name']))
        logger.debug("%s to level %s", state['name'], b)
        disle3(b, state['my_sex'][0])
        sendsys(
            state,
            state['name'],
            state['name'],
            -10113,
            state['me'].location,
            "[p]{}[/p] is now level {}\n".format(state['name'], state['my_lev']),
        )
        if b == 10:
            state = state['bprintf']("[f]{}[/f]".format(GWIZ))
    state['me'].level = state['my_lev']
    if state['my_str'] > 30 + 10 * state['my_lev']:
        state['my_str'] = 30 + 10 * state['my_lev']
    state['me'].strength = state['my_str']
    state['me'].sex = state['my_sex'][0]
    state['me'].weapon = Item(state, state['wpnheld'])
    return state


def playcom(state):
    if brkword() == -1:
        return state['bprintf'](state, "Play what ?\n")
    item = Item(state, fobna(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "That isn't here\n")
    if not item.is_available(state['me']):
        return state['bprintf'](state, "That isn't here\n")
    return state


def tellcom(state):
    if chkdumb():
        return state
    if brkword() == -1:
        return state['bprintf']("Tell who?\n")
    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id == -1:
        return state['bprintf']("No one with that name is playing\n")
    return sendsys(
        state,
        player.name,
        state['name'],
        -10004,
        state['curch'],
        getreinput(),
    )


def exorcom(state):
    if state['my_lev'] < 10:
        return state['bprintf'](state, "No chance....\n")
    if brkword() == -1:
        return state['bprintf'](state, "Exorcise who?\n")

    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id == -1:
        return state['bprintf'](state, "They aren't playing\n")
    if ptstflg(player.player_id, 1):
        return state['bprintf'](state, "You can't exorcise them, they dont want to be exorcised\n")

    logger.debug("%s exorcised %s", state['name'], player.name)
    dumpstuff(player.player_id, player.location)
    sendsys(
        state,
        player.name,
        state['name'],
        -10010,
        state['curch'],
        '',
    )
    player.destroy()
    return state


def dogive(state, ob, pl):
    item = Item(state, ob)
    player = Player(state, pl)

    if state['my_lev'] < 10 and player.location != state['curch']:
        return state['bprintf'](state, "They are not here\n")
    if not iscarrby(item.item_id, state['mynum']):
        state = state['bprintf'](state, "You are not carrying that\n")
    if not cancarry(pl):
        return state['bprintf'](state, "They can't carry that\n")
    if state['my_lev'] < 10 and item.item_id == 32:
        return state['bprintf'](state, "It doesn't wish to be given away.....\n")

    item.carried_by = pl
    sendsys(
        state,
        player.name,
        state['name'],
        -10011,
        state['curch'],
        "[p]{}[/p] gives you the {}\n".format(state['name'], item.name)
    )


def stealcom(state):
    if brkword() == -1:
        return state['bprintf'](state, "Steal what from who?\n")
    x = state['wordbuf']
    if brkword() == -1:
        return state['bprintf'](state, "From who?\n")
    if state['wordbuf'] == 'from' and brkword() == -1:
        return state['bprintf'](state, "From who?\n")
    player = Player(state, fpbn(state['wordbuf']))
    if player.player_id == -1:
        return state['bprintf'](state, "Who is that?\n")
    item = Item(state, fobncb(x, player.player_id))
    if item.item_id == -1:
        return state['bprintf'](state, "They are not carrying that\n")
    if state['my_lev'] < 10 and player.location != state['curch']:
        return state['bprintf'](state, "But they aren't here\n")
    if item.carry_flag == Item.WORN_BY:
        return state['bprintf'](state, "They are wearing that\n")
    if player.weapon.item_id == item.item_id:
        return state['bprintf'](state, "They have that firmly to hand .. for KILLING people with\n")
    if not cancarry(state['mynum']):
        return state['bprintf'](state, "You can't carry any more\n")

    f = randperc()
    e = (10 + state['my_lev'] - player.level) * 5
    if f < e:
        if f & 1:
            sendsys(
                state,
                player.name,
                state['name'],
                -10011,
                state['curch'],
                "[p]{}[/p] steals the {} from you !\n".format(state['name'], item.name),
            )
            if player.player_id > 15:
                woundmn(player.player_id, 0)

        item.carried_by = state['mynum']
        return state
    else:
        return state['bprintf'](state, "Your attempt fails\n")


def dosumm(state):
    state = change_channel(state, loc)


def tsscom(state):
    #
    close_world(state)
    #
    keysetback()
    keysetup()


def rmeditcom(state):
    state = set_message_id(state, state['mynum'], -2)
    #
    close_world(state)
    #
    state = open_world(state)
    #
    raise PlayerIsDead("You have been kicked off")
    #
    return process_messages(state, state['mynum'], state['cms'])


def u_system(state):
    state = set_message_id(state, state['mynum'], -2)
    #
    close_world(state)
    #
    state = open_world(state)
    #
    raise PlayerIsDead("You have been kicked off")
    #
    state = process_messages(state, state['mynum'], state['cms'])
    state = open_world(state)
    #


def updcom(state):
    try:
        pass
    except PlayerIsDead as e:
        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[ {} has updated ]\n".format(state['name']),
        )
        close_world(state)

    try:
        execl(EXE, "   --{----- ABERMUD -----}--   ", state['name'])
    except FileNotFoundError:
        state['bprintf'](state, "Eeek! someones pinched the executable!\n")


def becom(state):
    try:
        #
        keysetback()
    except PlayerIsDead:
        close_world(state)

    try:
        execl(EXE2, "   --}----- ABERMUD ------   ", x)
    except FileNotFoundError:
        state['bprintf'](state, "Eek! someone's just run off with mud!!!!\n")


def rawcom():
    broad(world, x[1:])
    broad(world, y)


def bugcom(state):
    #
    logger.debug("Bug by %s : %s", state['name'], x)


def typocom(state):
    #
    logger.debug("Typo by %s : %s", y, x)


def look_cmd(state):
    if brkword() == -1:
        brhold = state['brmode']
        state['brmode'] = 0
        lookin(state, state['curch'])
        state['brmode'] = brhold
        return state
    if state['wordbuf'] == 'at':
        return examcom(state)
    if state['wordbuf'] != 'in' and state['wordbuf'] != 'into':
        return state
    if brkword() == -1:
        return state['bprintf'](state, "In what ?\n")
    item = Item(state, fobna(state['wordbuf']))
    if item.item_id == -1:
        return state['bprintf'](state, "What ?\n")
    if not item.is_container:
        return state['bprintf'](state, "That isn't a container\n")
    if item.can_open and item.state != 0:
        return state['bprintf'](state, "It's closed!\n")

    state = state['bprintf'](state, "The {} contains:\n".format(item.name))
    aobjsat(item.item_id, 3)


def digcom(state):
    item = Item(state, 186)
    if item.location == state['curch'] and item.is_destroyed:
        item.create()
        return state['bprintf'](state, "You uncover a stone slab!\n")
    if state['curch'] not in [-172, -192]:
        return state['bprintf'](state, "You find nothing.\n")
    if state(176) == 0:
        return state['bprintf'](state, "You widen the hole, but with little effect.\n")
    setstate(176, 0)
    return state['bprintf'](state, "You rapidly dig through to another passage.\n")


def emptycom(state):
    container = Item(state, ohereandget())
    if container.item_id == -1:
        return state
    for item_id in state['numobs']:
        item = Item(state, item_id)
        if iscontin(item.item_id, container.item_id):
            item.carried_by = state['mynum']
            state = state['bprintf'](state, "You empty the {} from the {}\n".format(item.name, container.name))
            gamecom("drop {}".format(item.name))
            state = state['pbdf'](state)
            state = open_world(state)
    return state
