from ..gamego.signals import set_alarm


def loseme(state, name=None):
    set_alarm(state, False)
    raise NotImplementedError()
