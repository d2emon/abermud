"""
AberMUD II   C

This game systems, its code scenario and design
are (C) 1987/88  Alan Cox,Jim Finnis,Richard Acott

This file holds the basic communications routines
"""
state = {
    'i_setup': 0,
    'oddcat': 0,
    'talkfl': 0,

    'cms': -1,
    'curch': 0,
    'globme': '',
    'curmode': 0,
    'meall': 0,

    'gurum': 0,
    'convflg': 0,

    'fl_com': None,

    'rd_qd': 0,

    'dsdb': 0,
    'moni': 0,

    'bound': 0,
    'tmpimu': 0,
    'echoback': 'e',
    'tmpwiz': '.',

    'mynum': 0,

    'lasup': 0,

    'iamon': 0,
}

"""
Data format for mud packets

Sector 0
[64 words]
0   Current first message pointer
1   Control Word
Sectors 1-n  in pairs ie [128 words]

[channel][controlword][text data]

[controlword]
0 = Text
-1 = general request
"""


def vcpy(dest, offd, source, offs, __len):
    raise NotImplementedError()


def mstoout(block, name):
    raise NotImplementedError()


def sendmsg(name):
    raise NotImplementedError()


def send2(block):
    raise NotImplementedError()


def readmsg(channel, block, num):
    raise NotImplementedError()


def rte(name):
    raise NotImplementedError()


def openlock(file, perm):
    raise NotImplementedError()


def findstart(unit):
    raise NotImplementedError()


def findend(unit):
    raise NotImplementedError()


def talker(name):
    raise NotImplementedError()


def cleanup(inpbk):
    raise NotImplementedError()


def special(string, name):
    raise NotImplementedError()


def broad(mesg):
    raise NotImplementedError()


def tbroad(message):
    raise NotImplementedError()


def sysctrl(block, luser):
    raise NotImplementedError()


def split(block, nam1, nam2, work, luser):
    raise NotImplementedError()


def trapch(chan):
    raise NotImplementedError()


def putmeon(name):
    raise NotImplementedError()


def loseme(name):
    raise NotImplementedError()


def update(name):
    raise NotImplementedError()


def revise(cutoff):
    raise NotImplementedError()


def lookin(room):
    raise NotImplementedError()


def loodrv(room):
    raise NotImplementedError()


def userwrap():
    raise NotImplementedError()


def fcloselock(file):
    raise NotImplementedError()
