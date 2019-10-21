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


def cancarry(state, player_id):
    player = Player(state, player_id)
    if player.level > 9:
        return True
    if player.level < 0:
        return True
    items = (Item(state, item_id) for item_id in range(state['numobs']))
    items = filter(lambda i: iscarrby(i, player) and not i.is_destroyed, items)
    if len(list(items)) < player.level + 5:
        return True
    return False


def setcom(state):
    def setmobile(new_state):
        player = Player(new_state, fpbn(new_state['wordbuf']))
        if player.player_id == -1:
            return state['bprintf'](state, "Set what ?\n")
        if player.player_id < 16:
            return state['bprintf'](state, "Mobiles only\n")
        if brkword() == -1:
            return state['bprintf'](state, "To what value ?\n")
        player.strength = int(state['wordbuf'])
        return new_state

    def bitset(new_state, item):
        if brkword() == -1:
            return state['bprintf'](state, "Which bit ?\n")
        b = int(state['wordbuf'])
        if brkword() == -1:
            return state['bprintf'](state, "The bit is {}\n".format('TRUE' if item.flags[b] else 'FALSE'))
        c = int(state['wordbuf'])
        if c < 0 or c > 1 or b < 0 or b > 15:
            return state['bprintf'](state, "Number out of range\n")
        item.flags[b] = (c == 1)
        return new_state

    def byteset(new_state, item):
        if brkword() == -1:
            return state['bprintf'](state, "Which byte ?\n")
        b = int(state['wordbuf'])
        if brkword() == -1:
            return state['bprintf'](state, "Current Value is : {}\n".format(item.bytes[b]))
        c = int(state['wordbuf'])
        if c < 0 or c > 255 or b < 0 or b > 1:
            return state['bprintf'](state, "Number out of range\n")
        item.bytes[b] = c
        return new_state

    if brkword() == -1:
        return state['bprintf'](state, "set what\n")
    if state['my_lev'] < 10:
        return state['bprintf'](state, "Sorry, wizards only\n")
    item = Item(state, state['wordbuf'])
    if item.item_id == -1:
        return setmobile(state)
    if brkword() == -1:
        return state['bprintf'](state, "Set to what value?\n")
    if state['wordbuf'] == 'bit':
        return bitset(state, item)
    if state['wordbuf'] == 'byte':
        return byteset(state, item)
    b = int(state['wordbuf'])
    if b > item.max_state:
        return state['bprintf'](state, "Sorry max state for that is {}\n".format(item.max_state))
    if b < 0:
        return state['bprintf'](state, "States start at 0\n")
    setstate(item, b)
    return state


def isdark(state):
    def idk(new_state):
        for item_id in new_state['numobs']:
            item = Item(new_state, item_id)
            if item_id != 32 and otstbit(item.item_id, 13):
                continue
            if ishere(item.item_id):
                return False
            if not item.owned_by:
                continue
            owner = Player(state, item.owned_by)
            if owner.location != state['curch']:
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


def setpflags(state):
    if not state['me'].can_change_flags:
        return state['bprintf'](state, "You can't do that\n")
    if brkword() == -1:
        return state['bprintf'](state, "Whose PFlags?\n")
    target = Player(state, fpbns(state['wordbuf']))
    if target.player_id == -1:
        return state['bprintf'](state, "Who is that?\n")
    if brkword() == -1:
        return state['bprintf'](state, "Flag number?\n")
    flag_id = int(state['wordbuf'])
    if brkword() == -1:
        return state['bprintf'](state, "Value is {}\n".format('TRUE' if target.flags[flag_id] else 'FALSE'))
    value = int(state['wordbuf'])
    if value < 0 or value > 1 or flag_id < 0 or flag_id > 31:
        return state['bprintf'](state, "Out of range\n")
    target.flags[flag_id] = value
    return state
