from datetime import datetime
from .errors import PlayerIsDead
from .opensys import close_world, open_world
from .support import pname
from .sys_log import logger


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


def gamrcv(state, message):
    name = state['name'].lower()
    is_me, name1, name2, text = split(message, name)
    location = message[0]
    code = message[1]
    if code == -20000 and fpbns(name1) == state['fighting']:
        state['in_fight'] = 0
        state['fighting'] = -1
    if code < -10099:
        new1rcv(is_me, location, name1, name2, code, text)
    elif code == -401 and is_me:
        state.update({'snoopd', fpbns(name2)})
    elif code == -599 and is_me:
        state.update({
            'my_lev': text[0],
            'my_sco': text[1],
            'my_str': text[2],
        })
        state = calibme(state)
    elif code == -666:
        state['bprintf'](state, "Something Very Evil Has Just Happened...\n")
        loseme()
        raise PlayerIsDead("Bye Bye Cruel World....")
    elif code == -400 and is_me:
        state.update({'snoopd', -1})
    elif code == -750 and is_me:
        if fpbns(name2) != -1:
            loseme()
        close_world(state)
        raise SystemExit("***HALT")
    elif code == -9900:
        setpvis(text[0], text[1])
    elif code == -10000 and not is_me and state['curch'] == location:
        return state['bprintf'](state, text)
    elif code == -10001:
        if not is_me:
            return state['bprintf'](state, "[c]A massive lightning bolt strikes [/c][D]{}[/D][c]\n[/c]".format(name1))
        if state['my_lev'] > 10:
            return state['bprintf'](state, "[p]{}[/p] cast a lightning bolt at you\n".format(name2))
        # You are in the ....
        sendsys(
            state['name'],
            state['name'],
            -10113,
            state['curch'],
            "[ [p]{}[/p] has just been zapped by [p]{}[/p] and terminated ]\n".format(state['name'], name2),
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
        loseme()
        state['bprintf'](state, "You have been utterly destroyed by {}\n".format(name2))
        raise PlayerIsDead("Bye Bye.... Slain By Lightning")
    elif code == -10002 and not is_me:
        if state['curch'] == location or state['my_lev'] > 9:
            return state['bprintf'](state, "[P]{}[/P][d] shouts '{}'\n[/d]".format(name2, text))
        return state['bprintf'](state, "[d]A voice shouts '{}'\n[/d]".format(text))
    elif code == -10003 and not is_me and state['curch'] == location:
        return state['bprintf'](state, "[P]{}[/P][d] says '{}'\n[/d]".format(name2, text))
    elif code == -10004 and is_me:
        return state['bprintf'](state, "[P]{}[/P][d] tells you '{}'\n[/d]".format(name2, text))
    elif code == -10010:
        if not is_me:
            return state['bprintf'](state, "{} has been kicked off\n".format(name1))
        loseme()
        raise PlayerIsDead("You have been kicked off")
    elif code == -10011 and is_me:
        return state['bprintf'](state, text)
    elif code == -10020 and is_me:
        state['ades'] = location
        if state['my_lev'] < 10:
            summon_message = "You drop everything you have as you are summoned by [p]{}[/p]\n".format(name2)
            state['tdes'] = 1
        else:
            summon_message = "[p]{}[/p] tried to summon you\n".format(name2)
        return state['bprintf'](state, summon_message)
    elif code == -10021 and is_me and state['curch'] == location:
        state.update({
            'rdes': 1,
            'vdes': text[0],
        })
        return bloodrcv(state, text, is_me)
    elif code == -10030:
        wthrrcv(location)
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


def lightning(state):
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
    #
    close_world(state)
    #


def becom():
    #
    keysetback()
    #
    close_world(state)
    #


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
