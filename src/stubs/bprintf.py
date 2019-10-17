from .errors import OutputBufferError  # PlayerLoose
from .opensys import close_world
from .sys_log import logger
from .support import Player


# State
global_state = {
    'is_clean': True,
    'sysbuf': '',
}


# Mutations
def set_clean(state, is_clean):
    state['is_clean'] = is_clean
    return state


# Actions
def __lock_alarm(state):
    return {
        **state,
        '__ignore': True,
    }


def __unlock_alarm(state):
    if state['timer_active']:
        state['time'] = 2
    return {
        **state,
        '__ignore': False,
    }


def bprintf(state, *args):
    #
    logger.debug("Bprintf Short Buffer overflow")
    raise OutputBufferError("Internal Error in BPRINTF")
    #


def dcprnt(__str, __file):
    #
    raise OutputBufferError("Internal $ control sequence error")
    #


def tocontinue(state, __str, ct, x, mx):
    #
    logger.debug("Bprintf Short Buffer overflow")
    #
    raise OutputBufferError("Buffer OverRun in IO_TOcontinue")
    #


def seeplayer(state, player_id):
    player = Player(state, player_id)
    if player.player_id == -1:
        return True
    if player.player_id == state['mynum']:
        return True
    if plev(state['mynum']) < pvis(player.player_id):
        return False
    if state['ail_blind']:
        return False
    if player.location == state['curch'] and isdark(state['curch']):
        return False

    setname(player.player_id)
    return True


def make_buffer(state):
    try:
        state['sysbuf'] = ''
        return state
    except Exception:
        raise OutputBufferError("Out Of Memory")


def pbfr(state):
    state = __lock_alarm(state)
    close_world(state)
    if state['sysbuf']:
        state = set_clean(state, False)

    if state['sysbuf'] and state['pr_qcr']:
        putchar("\n")
        state['pr_qcr'] = False

    if state['log_fl']:
        state['iskb'] = False
        dcprnt(state['sysbuf'], state['log_fl'])

    if state['snoopd'] != -1:
        snoopd = Player(state, state['snoopd'])
        try:
            fln = opensnoop(snoopd.name, 'a')
            state['iskb'] = False
            dcprnt(state['sysbuf'], fln)
            fln.unlock().disconnect()
        except ServiceError:
            pass

    state['iskb'] = True
    dcprnt(state['sysbuf'], None)

    state['sysbuf'] = ''

    if state['snoopt'] != -1:
        viewsnoop()

    state = __unlock_alarm(state)
    return state


def quprnt(state, x):
    #
    logger.debug("Buffer overflow on user %s", state['name'])
    raise OutputBufferError("PANIC - Buffer overflow")


def opensnoop(user, per):
    #
    return z.connect(per).lock()


def snoopcom(state):
    if state['my_lev'] < 10:
        return state['bprintf'](state, "Ho hum, the weather is nice isn't it\n")

    if state['snoopt'] != -1:
        state = state['bprintf'](state, "Stopped snooping on {}\n".format(state['sntn']))
        state['snoopt'] = -1
        sendsys(
            state,
            state['sntn'],
            state['globme'],
            -400,
            0,
            "",
        )

    if brkword() == -1:
        return state

    target = Player(state, fpbn(state['wordbuf']))
    if target.player_id == -1:
        return state['bprintf'](state, "Who is that?\n")
    if state['my_lev'] < 10000 and plev(target.player_id) >= 10 or ptstbit(target.player_id, 6):
        state['snoopt'] = -1
        return state['bprintf'](state, "Your magical vision is obscured\n")

    state.update({
        'sntn': target.name,
        'snoopt': target.player_id,
    })
    state = state['bprintf'](state, "Started to snoop on {}\n".format(target.name))
    sendsys(
        state,
        state['sntn'],
        state['globme'],
        -401,
        0,
        "",
    )

    fx = opensnoop(state['name'], 'w')
    fx.append(' ')
    fx.unlock().disconnect()


def viewsnoop():
    fx.unlock().disconnect()


def setname(state, player_id):
    player = Player(state, player_id)
    if player.player_id > 15 and player.player_id != fpbns('riatha') and player.player_id != fpbns('shazareth'):
        state['wd_it'] = player.name
        return state
    if psex(player.player_id):
        state['wd_her'] = player.name
    else
        state['wd_him'] = player.name
    state['wd_them'] = player.name
    return state
