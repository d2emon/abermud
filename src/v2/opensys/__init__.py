from ..gamego.error import MudError


def fcloselock(service):
    raise NotImplementedError()


def get_numobs():
    raise NotImplementedError()


def get_objinfo():
    raise NotImplementedError()


def get_ublock():
    raise NotImplementedError()


def openlock(service, create=False, write=False):
    raise NotImplementedError()


def set_objinfo(value):
    raise NotImplementedError()


def set_ublock(value):
    raise NotImplementedError()


class WorldError(MudError):
    pass


class World:
    active = None

    def __init__(self):
        try:
            self.active = openlock('/usr/tmp/-iy7AM', create=True)
        except WorldError:
            raise WorldError("Cannot find World file")

    @classmethod
    def __read(cls, offset, count, size):
        raise NotImplementedError()

    @classmethod
    def __write(cls, data, offset, count, size):
        raise NotImplementedError()

    @classmethod
    def load(cls):
        world = cls.active
        if world is not None:
            return world

        world = cls()
        set_objinfo(world.__read(400, get_numobs(), 4))
        set_ublock(world.__read(350, 48, 16))
        return world

    @classmethod
    def save(cls):
        world = cls.active
        if world is None:
            return

        world.write(get_objinfo(), 400, get_numobs(), 4)
        world.write(get_ublock(), 350, 48, 16)
        fcloselock(world)
        world.active = None
