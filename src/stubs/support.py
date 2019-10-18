"""
Some more basic functions

Note

state(obj)
setstate(obj,val)
destroy(obj)

are elsewhere
"""


class Item:
    LOCATED_AT = 0
    CARRIED_BY = 1
    WORN_BY = 2
    CONTAINED_IN = 3

    def __init__(self, state, item_id):
        self.__state = state
        self.item_id = item_id

    @property
    def __items(self):
        return self.__state['objects']

    @property
    def __item_vars(self):
        return self.__state['objinfo']

    @property
    def name(self):
        return self.__items[self.item_id].name

    @property
    def description(self):
        return self.state_description(state(self.item_id))

    @property
    def max_state(self):
        return self.__items[self.item_id].max_state

    @property
    def is_movable(self):
        return not self.__items[self.item_id].is_fixed

    @property
    def location(self):
        return self.__item_vars[4 * self.item_id]

    @property
    def located_at(self):
        return self.location if self.carry_flag == self.LOCATED_AT else None

    @located_at.setter
    def located_at(self, value):
        self.__item_vars[4 * self.item_id] = value
        self.__item_vars[4 * self.item_id + 3] = self.LOCATED_AT

    @property
    def carried_by(self):
        return self.location if self.carry_flag == self.CARRIED_BY else None

    @carried_by.setter
    def carried_by(self, value):
        self.__item_vars[4 * self.item_id] = value
        self.__item_vars[4 * self.item_id + 3] = self.CARRIED_BY

    @property
    def contained_in(self):
        return self.location if self.carry_flag == self.CONTAINED_IN else None

    @contained_in.setter
    def contained_in(self, value):
        self.__item_vars[4 * self.item_id] = value
        self.__item_vars[4 * self.item_id + 3] = self.CONTAINED_IN

    @property
    def owned_by(self):
        return self.location if self.carry_flag in (self.CARRIED_BY, self.WORN_BY) else None

    @property
    def carry_flag(self):
        return self.__item_vars[4 * self.item_id + 3]

    # @carry_flag.setter
    # def carry_flag(self, value):
    #     self.__items[4 * self.item_id + 3] = value

    def state_description(self, state):
        return self.__items[self.item_id].description[state]



class Player:
    male = 'MALE'
    female = 'FEMALE'

    def __init__(self, state, player_id):
        self.state = state
        self.player_id = player_id

    @property
    def __players(self):
        return self.state['objinfo']

    @property
    def name(self):
        return self.__players[16 * self.player_id]

    @name.setter
    def name(self, value):
        self.__players[16 * self.player_id] = value

    @property
    def location(self):
        return self.__players[16 * self.player_id + 4]

    @location.setter
    def location(self, value):
        self.__players[16 * self.player_id + 4] = value

    @property
    def strength(self):
        return self.__players[16 * self.player_id + 7]

    @strength.setter
    def strength(self, value):
        self.__players[16 * self.player_id + 7] = value

    @property
    def visibility(self):
        return self.__players[16 * self.player_id + 8]

    @visibility.setter
    def visibility(self, value):
        self.__players[16 * self.player_id + 8] = value

    @property
    def flags(self):
        return self.__players[16 * self.player_id + 9]

    @flags.setter
    def flags(self, value):
        self.__players[16 * self.player_id + 9] = value

    @property
    def sex(self):
        return self.male if self.flags[0] else self.female

    @sex.setter
    def sex(self, value):
        self.flags[0] = value == self.male

    @property
    def level(self):
        return self.__players[16 * self.player_id + 10]

    @level.setter
    def level(self, value):
        self.__players[16 * self.player_id + 10] = value

    @property
    def is_alive(self):
        return len(self.name) > 0

    @property
    def value(self):
        if self.player_id < 16:
            return self.level ** 2 * 100
        return 10 * damof(self.player_id)

    def is_visible(self, level):
        return level >= self.visibility

    def set_flags(self, flags):
        self.__players[16 * self.player_id + 9] = flags

    def destroy(self):
        self.name = ''

    def kill(self):
        if self.strength < 0:
            return 0
        self.strength = -1
        return self.value


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


def pwpn(chr):
    raise NotImplementedError()


def setpwpn(chr, v):
    raise NotImplementedError()


def ocreate(ob):
    raise NotImplementedError()


def osetbit(ob, x):
    raise NotImplementedError()item_id)


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


def ptothlp(state, pl):
    who = Player(state, pl)
    for player_id in range(state['maxu']):
        player = Player(state, player_id)
        if player.location != who.location:
            continue
        if phelping(player.player_id) != who.player_id:
            continue
        return player.player_id
    return -1


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
