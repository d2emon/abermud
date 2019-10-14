"""
Two Phase Game System
"""
state = {
    'argv_p': '',
    'privs': [],
    'sig_active': 0,
    'interrupt': 0,
}


def main(argc, argv):
    raise NotImplementedError()


def crapup(__str):
    raise NotImplementedError()


def listfl(name):
    raise NotImplementedError()


def getkbd(s, l):
    raise NotImplementedError()


def sig_alon():
    raise NotImplementedError()


def unblock_alarm():
    raise NotImplementedError()


def block_alarm():
    raise NotImplementedError()


def sig_aloff():
    raise NotImplementedError()


def sig_occur():
    raise NotImplementedError()


def sig_init():
    raise NotImplementedError()


def sig_oops():
    raise NotImplementedError()


def sig_ctrlc():
    raise NotImplementedError()


def set_progname(n, text):
    raise NotImplementedError()
