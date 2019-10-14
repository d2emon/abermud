"""
Two Phase Game System
"""
import sys
from ..errors import PlayerIsDead, LockError, OutputBufferError, SysLogError, UserDataError, WorldError
from ..bprintf import pbfr
from ..key import global_state as key_state
from ..support import syslog
from ..tk import talker
from .signals import set_alarm, global_state as signals_state


global_state = {
    'interrupt': 0,
    #
    'in_fight': None,
    # Helpers
    'pbfr': pbfr,
}


__dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


def initialize_state(state, username):
    state = {
        **state,
        **key_state,
        **signals_state,
        **global_state,
        'globme': "The {}".format(username) if username == 'Phantom' else username,
    }
    print("Entering Game ....")
    print("Hello {}".format(state['globme']))
    syslog(state, "GAME ENTRY: {}[{}".format(state['globme'], state['user_id']))
    return state


def finalize_state(state):
    return {
        **state['pbfr'](state),
        'pr_due': 0,  # So we dont get a prompt after the exit
    }


def main(state, username):
    try:
        state = initialize_state(state, username)
        talker(state['globme'])
    except (PlayerIsDead, LockError, OutputBufferError, SysLogError, UserDataError, WorldError) as e:
        finalize_state(state)
        print("\n{}\n\n{}\n\n{}".format(__dashes, e, __dashes))
        sys.exit(0)
    except Exception:
        state['onError'](state)
