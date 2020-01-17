from ..gamego.error import MudError


class WorldError(MudError):
    pass


class Service:
    NAME = None

    def __init__(self, read=True, write=False, create=False, append=False):
        if not create:
            raise WorldError()

        self.name = self.NAME
        self.__read = read
        self.__write = write
        self.__create = create
        self.__append = append
        self.__active = True

    def disconnect(self):
        self.name = None
        self.__active = False

    @classmethod
    def lock(cls, **kwargs):
        try:
            return cls(**kwargs)
        except WorldError:
            # ENOSPC        PANIC exit device full
            # EHOSTUNREACH  PANIC exit access failure, NFS gone for a snooze
            raise WorldError()

    def unlock(self):
        self.disconnect()

    @property
    def active(self):
        return self.__active

    @property
    def data(self):
        raise NotImplementedError()

    def read(self, record_id, count=None, size=None):
        if not self.active or not self.__read:
            raise WorldError()

        return self.data.get(record_id)

    def write(self, record_id, value, count=None, size=None):
        if not self.active or not self.__write:
            raise WorldError()

        self.data[record_id] = value


class World(Service):
    NAME = '/usr/tmp/-iy7AM'
    __ITEMS = 400
    __PLAYERS = 350
    __ITEMS_COUNT = 194
    __PLAYERS_COUNT = 48

    __world = None
    __data = {
        __PLAYERS: [{} for _ in range(__PLAYERS_COUNT)],
        __ITEMS: [{} for _ in range(__ITEMS_COUNT)],
        'players_count': __PLAYERS_COUNT,
        'items_count': __ITEMS_COUNT,
        'players_size': 16,
        'items_size': 4,
    }
    __items = [None for _ in range(__ITEMS_COUNT)]
    __players = [None for _ in range(__PLAYERS_COUNT)]

    @property
    def data(self):
        return self.__data

    @classmethod
    def __connect(cls):
        try:
            return cls.lock(read=True, create=True, write=True)
        except WorldError:
            raise WorldError("Cannot find World file")

    @classmethod
    def read_meta(cls):
        return cls.__world.read(0)

    @classmethod
    def read_event(cls, event_id):
        return cls.__world.read(event_id)

    @classmethod
    def read_players(cls):
        return cls.__world.read(350)

    @classmethod
    def read_items(cls):
        return cls.__world.read(400)

    @classmethod
    def write_meta(cls, meta):
        cls.__world.write(meta, 0)

    @classmethod
    def write_event(cls, event_id, event):
        cls.__world.write(event, event_id)

    @classmethod
    def write_players(cls, players):
        cls.__world.write(cls.__players, 350)

    @classmethod
    def write_items(cls, items):
        cls.__world.write(cls.__items, 400)

    @classmethod
    def load(cls):
        if cls.__world is not None:
            return cls.__world

        cls.__world = cls.__connect()
        cls.__items = cls.__world.read(cls.__ITEMS)
        cls.__players = cls.__world.read(cls.__PLAYERS)
        return cls.__world

    @classmethod
    def save(cls):
        if cls.__world is None:
            return

        cls.__world.write(cls.__ITEMS, cls.__items)
        cls.__world.write(cls.__PLAYERS, cls.__players)
        cls.__world.unlock()
        cls.__world = None
