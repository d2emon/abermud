"""
 The next part of the universe...
"""

"""
Weather Routines

Current weather defined by state of object 47

states are

0   Sunny
1   Rain
2   Stormy
3   Snowing
"""
state = {
    'hasfarted': 0,
}


def setwthr(n):
    raise NotImplementedError()


def suncom():
    raise NotImplementedError()


def raincom():
    raise NotImplementedError()


def stormcom():
    raise NotImplementedError()


def snowcom():
    raise NotImplementedError()


def blizzardcom():
    raise NotImplementedError()


def adjwthr(n):
    raise NotImplementedError()


def longwthr():
    raise NotImplementedError()


def wthrrcv(__type):
    raise NotImplementedError()


def showwthr():
    raise NotImplementedError()


def outdoors():
    raise NotImplementedError()


# Silly Section


def sillycom(txt):
    raise NotImplementedError()


def laughcom():
    raise NotImplementedError()


def purrcom():
    raise NotImplementedError()


def crycom():
    raise NotImplementedError()


def sulkcom():
    raise NotImplementedError()


def burpcom():
    raise NotImplementedError()


def hiccupcom():
    raise NotImplementedError()


def fartcom():
    raise NotImplementedError()


def grincom():
    raise NotImplementedError()


def smilecom():
    raise NotImplementedError()


def winkcom():
    raise NotImplementedError()


def sniggercom():
    raise NotImplementedError()


def posecom(state):
    broad(world, "[c]A massive ball of fire explodes high up in the sky\n[/c]")
    raise NotImplementedError()


def emotecom():
    raise NotImplementedError()


def praycom():
    raise NotImplementedError()


def yawncom():
    raise NotImplementedError()


def groancom():
    raise NotImplementedError()


def moancom():
    raise NotImplementedError()


def cancarry(plyr):
    raise NotImplementedError()


def setcom():
    raise NotImplementedError()


def isdark(state):
    def idk(new_state):
        for item_id in new_state['numobs']:
            item = Item(new_state, item_id)
            if item_id != 32 and otstbit(item.item_id, 13):
                continue
            if ishere(item.item_id):
                return False
            if item.carry_flag in (Item.CONTAINED_IN, Item.WORN_BY):
                continue
            if ploc(oloc(item.item_id)) != state['curch']:
                continue
            return False
        return True

    if state['my_lev'] > 9:
        return False
    if state['curch'] == -1100 or state['curch'] == -1101:
        return False
    if -1113 >= state['curch'] >= -1123:
        return idk(state)
    if state['curch'] < -399 or state['curch'] > -300:
        return False
    return idk(state)


def modifwthr(n):
    raise NotImplementedError()


def setpflags():
    raise NotImplementedError()
