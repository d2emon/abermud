from datetime import datetime
from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import pname
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
    state = process_messages(state, state['mynum'], state['cms'])
    state = open_world(state)
    #
    close_world(state)
    #
    raise PlayerIsDead("Goodbye")
    #


def dodirn(state, n):
    state = change_channel(state, newch)


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
        setpvis(message.text[0], message.text[1])
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
        setpvis(state['mynum'], 0)

    if state['me_cal']:
        state['me_cal'] = False
        state = calibme(state)

    if state['tdes']:
        dosumm(state['ades'])

    if state['in_fight']:
        """
        if(ploc(fighting)!=curch)
          {
          fighting= -1;
          in_fight=0;
          }
        if(!strlen(pname(fighting)))
          {
          fighting= -1;
          in_fight=0;
          }
        if(in_fight)
          {
          if(interrupt)
             {
             in_fight=0;
             hitplayer(fighting,wpnheld);
             }
          }
        """
        pass
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
    #
    broad(world, "[d]You hear an ominous clap of thunder in the distance\n[/d]")
    #
    logger.debug("%s zapped %s", state['name'], pname(vic))
    #


def calibme(state):
    #
    logger.debug("%s to level %s", state['name'], b)
    #


def exorcom(state):
    #
    logger.debug("%s exorcised %s", state['name'], pname(x))
    #


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
    if state['my_lev'] < 10 and ploc(player.player_id) != state['curch']:
        return state['bprintf'](state, "But they aren't here\n")
    if item.carry_flag == Item.WORN_BY:
        return state['bprintf'](state, "They are wearing that\n")
    if pwpn(player.player_id) == item.item_id:
        return state['bprintf'](state, "They have that firmly to hand .. for KILLING people with\n")
    if not cancarry(state['mynum']):
        return state['bprintf'](state, "You can't carry any more\n")

    f = randperc()
    e = 10 + state['my_lev'] - plev(player.player_id)
    e *= 5
    if f < e:
        if f & 1:
            sendsys(
                state,
                pname(player.player_id),
                state['name'],
                -10011,
                state['curch'],
                "[p]{}[/p] steals the {} from you !\n".format(state['name'], oname(item.item_id)),
            )
            if player.player_id > 15:
                woundmn(player.player_id, 0)

        setoloc(item.item_id, state['mynum'], 0)
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


def emptycom(state):
    #
    state = open_world(state)
    #
