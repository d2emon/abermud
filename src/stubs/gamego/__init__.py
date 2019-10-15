"""
Two Phase Game System
"""
import sys
from ..errors import PlayerIsDead, LockError, OutputBufferError, SysLogError, UserDataError, WorldError
from ..bprintf import bprintf, pbfr
from ..sys_log import logger
from ..tk import rte
from ..tk.talker import talker, next_turn
from .signals import set_alarm, global_state as signals_state


# State
global_state = {
    **signals_state,
    'interrupt': 0,
    #
    'in_fight': None,
    # Helpers
    'rte': rte,
    'bprintf': bprintf,
    'pbfr': pbfr,
}


# Mutations
def set_name(state, name):
    state['name'] = "The {}".format(name) if name == 'Phantom' else name
    return state


__dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


def initialize_state(state, username):
    state = set_name(state, username)
    print("Entering Game ....")
    print("Hello {}".format(state['name']))
    logger.debug("GAME ENTRY: %s[%s]", state['name'], state['user_id'])
    return state


def finalize_state(state):
    return {
        **state['pbfr'](state),
        'pr_due': 0,  # So we dont get a prompt after the exit
    }


def main(state, username):
    try:
        state = initialize_state(state, username)
        state = talker(state)
        while True:
            state = next_turn(state)
    except (PlayerIsDead, LockError, OutputBufferError, SysLogError, UserDataError, WorldError) as e:
        finalize_state(state)
        print("\n{}\n\n{}\n\n{}".format(__dashes, e, __dashes))
        sys.exit(0)
    except Exception:
        state['onError'](state)
