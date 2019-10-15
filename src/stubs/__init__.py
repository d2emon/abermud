from .gamego import global_state as main_state
from .key import global_state as key_state
from .tk import global_state as talker_state


state = {
    **key_state,
    **talker_state,
    **main_state,
}
