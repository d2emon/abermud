"""
AberMUD II   C

This game systems, its code scenario and design
are (C) 1987/88  Alan Cox,Jim Finnis,Richard Acott

This file holds the basic communications routines
"""
from ..errors import PlayerIsDead, WorldError
from ..bprintf import makebfr
from ..gamego.signals import set_alarm
from ..key import key_input


global_state = {
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


def __vcpy(dest, offd, source, offs, __len):
    raise NotImplementedError()


def __mstoout(block, name):
    raise NotImplementedError()


def __sendmsg(state, name):
    state['program'] = "-csh"
    state['program'] = "   --}----- ABERMUD -----{--     Playing as {}".format(name)

    state = set_alarm(state, True)
    state = key_input(state, prmpt, 80)
    state = set_alarm(state, False)

    raise NotImplementedError()


def __send2(block):
    raise WorldError("AberMUD: FILE_ACCESS : Access failed")
    raise NotImplementedError()


def __readmsg(channel, block, num):
    raise NotImplementedError()


def rte(name):
    raise WorldError("AberMUD: FILE_ACCESS : Access failed")
    raise NotImplementedError()


def __findstart(unit):
    raise NotImplementedError()


def __findend(unit):
    raise NotImplementedError()


def talker(state, name):
    makebfr()
    state = {
        **state,
        'cms': -1,
        'globme': name,
    }
    __putmeon(name)
    if openworld() is None:
        raise WorldError("Sorry AberMUD is currently unavailable")
    if state['mynum'] >= state['maxu']:
        raise Exception("Sorry AberMUD is full at the moment")
    state['globme'] = name
    rte(name)
    closeworld()
    state['cms'] = -1
    __special('.g', name)
    state['i_setup'] = True
    """
    while(1)
       {
       pbfr();
       sendmsg(name);
       if(rd_qd) rte(name);
       rd_qd=0;
       closeworld();
       pbfr();
       }
    """
    return state


def __cleanup(inpbk):
    raise NotImplementedError()


def __special(string, name):
    raise NotImplementedError()


def broad(mesg):
    raise NotImplementedError()


def __tbroad(message):
    raise NotImplementedError()


def __sysctrl(block, luser):
    raise NotImplementedError()


def split(block, nam1, nam2, work, luser):
    raise NotImplementedError()


def trapch(chan):
    raise NotImplementedError()


def __putmeon(name):
    raise WorldError("You are already on the system - you may only be on once at a time")
    raise NotImplementedError()


def update(name):
    raise NotImplementedError()


def __revise(cutoff):
    raise NotImplementedError()


def lookin(room):
    raise PlayerIsDead("bye bye.....")
    raise NotImplementedError()


def __loodrv(room):
    raise NotImplementedError()


def __userwrap(state):
    #
    syslog(state, "System Wrapup exorcised {}".format(state['globme']))
    #
    raise NotImplementedError()


def fcloselock(file):
    raise NotImplementedError()
