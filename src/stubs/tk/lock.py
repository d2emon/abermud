from ..gamego.signals import set_alarm


def loseme(state, name=None):
    state = open_world(state)
    close_world(state)
    set_alarm(state, False)
    raise NotImplementedError()
