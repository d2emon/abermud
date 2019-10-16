from datetime import datetime
from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import pname
from .sys_log import logger


def sendsys(state, __to, __from, codeword, channel, text):
    return send2(
        state,
        {
            'channel': channel,
            'code': codeword,
            'to': __to,
            'from': __from,
            'text': text,
        },
    )


def doaction(state, n):
    state = open_world(state)
    #
    state = state['rte'](state)
    state = open_world(state)
    #
    close_world(state)
    #
    raise PlayerIsDead("Goodbye")
    #


def dodirn(state, n):
    state = set_channel(state, newch)


def gamrcv(state, is_me, message):
    channel = message['channel']
    code = message['code']
    name_to = message['to']
    name_from = message['from']
    text = message['text']

    if code == -20000 and fpbns(name_to) == state['fighting']:
        state['in_fight'] = 0
        state['fighting'] = -1
    if code < -10099:
        new1rcv(is_me, channel, name_to, name_from, code, text)
    elif code == -401 and is_me:
        state.update({'snoopd', fpbns(name_from)})
    elif code == -599 and is_me:
        state.update({
            'my_lev': text[0],
            'my_sco': text[1],
            'my_str': text[2],
        })
        state = calibme(state)
    elif code == -666:
        state['bprintf'](state, "Something Very Evil Has Just Happened...\n")
        raise PlayerIsDead("Bye Bye Cruel World....")
    elif code == -400 and is_me:
        state.update({'snoopd', -1})
    elif code == -750 and is_me:
        if fpbns(name_from) != -1:
            raise PlayerIsDead("***HALT")

        close_world(state)
        raise SystemExit("***HALT")
    elif code == -9900:
        setpvis(text[0], text[1])
    elif code == -10000 and not is_me and state['curch'] == channel:
        return state['bprintf'](state, text)
    elif code == -10001:
        if not is_me:
            return state['bprintf'](state, "[c]A massive lightning bolt strikes [/c][D]{}[/D][c]\n[/c]".format(name_to))
        if state['my_lev'] > 10:
            return state['bprintf'](state, "[p]{}[/p] cast a lightning bolt at you\n".format(name_from))
        # You are in the ....
        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[ [p]{}[/p] has just been zapped by [p]{}[/p] and terminated ]\n".format(state['name'], name_to),
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
        state['bprintf'](state, "You have been utterly destroyed by {}\n".format(name_from))
        raise PlayerIsDead("Bye Bye.... Slain By Lightning")
    elif code == -10002 and not is_me:
        if state['curch'] == channel or state['my_lev'] > 9:
            return state['bprintf'](state, "[P]{}[/P][d] shouts '{}'\n[/d]".format(name_from, text))
        return state['bprintf'](state, "[d]A voice shouts '{}'\n[/d]".format(text))
    elif code == -10003 and not is_me and state['curch'] == channel:
        return state['bprintf'](state, "[P]{}[/P][d] says '{}'\n[/d]".format(name_from, text))
    elif code == -10004 and is_me:
        return state['bprintf'](state, "[P]{}[/P][d] tells you '{}'\n[/d]".format(name_from, text))
    elif code == -10010:
        if not is_me:
            return state['bprintf'](state, "{} has been kicked off\n".format(name_to))
        raise PlayerIsDead("You have been kicked off")
    elif code == -10011 and is_me:
        return state['bprintf'](state, text)
    elif code == -10020 and is_me:
        state['ades'] = channel
        if state['my_lev'] < 10:
            summon_message = "You drop everything you have as you are summoned by [p]{}[/p]\n".format(name_from)
            state['tdes'] = 1
        else:
            summon_message = "[p]{}[/p] tried to summon you\n".format(name_from)
        return state['bprintf'](state, summon_message)
    elif code == -10021 and is_me and state['curch'] == channel:
        state.update({
            'rdes': 1,
            'vdes': text[0],
        })
        return bloodrcv(state, text, is_me)
    elif code == -10030:
        wthrrcv(channel)
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
    broad("Reset in progress....\nReset Completed....\n")


def lightning(state):
    #
    broad("[d]You hear an ominous clap of thunder in the distance\n[/d]")
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


def dosummcom(state):
    state = set_channel(state, loc)


def tsscom(state):
    #
    close_world(state)
    #
    keysetback()
    keysetup()


def rmeditcom(state):
    #
    close_world(state)
    #
    state = open_world(state)
    #
    raise PlayerIsDead("You have been kicked off")
    #
    return state['rte'](state)


def u_system(state):
    #
    close_world(state)
    #
    state = open_world(state)
    #
    raise PlayerIsDead("You have been kicked off")
    #
    state = state['rte'](state)
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
    broad(x[1:])
    broad(y)

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
