from ..gamego.error import MudError


class WorldError(MudError):
    pass


class Service:
    def __init__(self, name, read=True, write=False, create=False):
        if not create:
            raise WorldError()

        self.name = name
        self.__read = read
        self.__write = write
        self.__create = create
        self.__active = True

    def disconnect(self):
        self.name = None
        self.__active = False

    @classmethod
    def lock(cls, name, **kwargs):
        try:
            return Service(name, **kwargs)
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
    __filename = '/usr/tmp/-iy7AM'
    __world = None
    __data = {
        350: [{} for _ in range(48)],
        400: [{} for _ in range(194)],
        'players_count': 48,
        'items_count': 194,
        'players_size': 16,
        'items_size': 4,
    }
    __items = [None for _ in range(194)]
    __players = [None for _ in range(48)]

    @property
    def data(self):
        return self.__data

    @classmethod
    def __connect(cls):
        try:
            return cls.lock(cls.__filename, create=True)
        except WorldError:
            raise WorldError("Cannot find World file")

    @classmethod
    def load(cls):
        if cls.__world is not None:
            return cls.__world

        cls.__world = cls.__connect()
        cls.__items = cls.__world.read(400)
        cls.__players = cls.__world.read(350)
        return cls.__world

    @classmethod
    def save(cls):
        if cls.__world is None:
            return

        cls.__world.write(cls.__items, 400)
        cls.__world.write(cls.__players, 350)
        cls.__world.unlock()
        cls.__world = None
