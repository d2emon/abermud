from .errors import PlayerIsDead


def on_timing():
    raise NotImplementedError()


def onlook():
    raise NotImplementedError()


def chkfight(x):
    raise NotImplementedError()


def consid_move(x):
    raise NotImplementedError()


def crashcom():
    raise NotImplementedError()


def singcom():
    raise NotImplementedError()


def spraycom():
    raise NotImplementedError()


# More new stuff


def dircom():
    raise NotImplementedError()


def sys_reset():
    #
    RESET_N.connect('ruf').lock()
    #
    raise NotImplementedError()


def dorune():
    raise NotImplementedError()


def pepdrop():
    raise NotImplementedError()
    raise PlayerIsDead("Whoops.....   Frying tonight")


def dragget():
    raise NotImplementedError()


def helpchkr():
    raise NotImplementedError()
