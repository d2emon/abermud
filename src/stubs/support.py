"""
Some more basic functions

Note

state(obj)
setstate(obj,val)
destroy(obj)

are elsewhere
"""


def ocarrf(ob):
    raise NotImplementedError()


def setocarrf(ob, v):
    raise NotImplementedError()


def oloc(ob):
    raise NotImplementedError()


def setoloc(ob, v):
    raise NotImplementedError()


def ploc(chr):
    raise NotImplementedError()


def pname(chr):
    raise NotImplementedError()


def plev(chr):
    raise NotImplementedError()


def setplev(ob, v):
    raise NotImplementedError()


def pchan(chr):
    raise NotImplementedError()


def pstr(chr):
    raise NotImplementedError()


def setpstr(ob, v):
    raise NotImplementedError()


def pvis(chr):
    raise NotImplementedError()


def setpvis(ob, v):
    raise NotImplementedError()


def psex(chr):
    raise NotImplementedError()


def setpsex(ob, v):
    raise NotImplementedError()


def setpsexall(ob, v):
    raise NotImplementedError()


def psexall(chr):
    raise NotImplementedError()


def oname(ob):
    raise NotImplementedError()


def olongt(st):
    raise NotImplementedError()


def omaxstate(ob):
    raise NotImplementedError()


def obflannel(ob):
    raise NotImplementedError()


def oflannel(ob):
    raise NotImplementedError()


def obaseval(ob):
    raise NotImplementedError()


def isdest(ob):
    raise NotImplementedError()


def isavl(ob):
    raise NotImplementedError()


def ospare(ob):
    raise NotImplementedError()


def ppos(chr):
    raise NotImplementedError()


def setppos(chr, v):
    raise NotImplementedError()


def setploc(chr, n):
    raise NotImplementedError()


def pwpn(chr):
    raise NotImplementedError()


def setpwpn(chr, v):
    raise NotImplementedError()


def ocreate(ob):
    raise NotImplementedError()


def osetbit(ob, x):
    raise NotImplementedError()


def oclearbit(ob, x):
    raise NotImplementedError()


def oclrbit(ob, x):
    raise NotImplementedError()


def otstbit(ob, x):
    raise NotImplementedError()


def osetbyte(ob, x, y):
    raise NotImplementedError()


def obyte(o, x):
    raise NotImplementedError()


def ohany(mask):
    raise NotImplementedError()


def phelping(x, y):
    raise NotImplementedError()


def setphelping(x, y):
    raise NotImplementedError()


def ptothlp(pl):
    raise NotImplementedError()


def psetflg(ch, x):
    raise NotImplementedError()


def pclrflg(ch, x):
    raise NotImplementedError()


"""
Pflags

0 sex
1 May not be exorcised ok
2 May change pflags ok
3 May use rmedit ok
4 May use debugmode ok
5 May use patch 
6 May be snooped upon
"""


def ptstbit(ch, x):
    raise NotImplementedError()


def ptstflg(ch, x):
    raise NotImplementedError()
