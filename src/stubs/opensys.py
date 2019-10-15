from .errors import ServiceError, WorldError
from .files import Service


class WorldService(Service):
    def __init__(self):
        super().__init__('/usr/tmp/-iy7AM')
        self.contents = {
            'first_message': 0,
            'last_message': 0,
            'messages': [],
            'items': [],
            'players': [],
        }


world = WorldService()


def close_world(state):
    if not world.connected:
        return

    world.contents['items'] = state['objinfo']
    world.contents['players'] = state['ublock']
    world.unlock()


def open_world(state):
    if world.connected:
        return state

    try:
        world.connect('r+').lock()
        return {
            **state,
            '__first_message': world.contents['first_message'],
            '__last_message': world.contents['last_message'],
            '__messages': world.contents['messages'],
            'objinfo': world.contents['items'],
            'ublock': world.contents['players'],
        }
    except ServiceError:
        raise WorldError("Cannot find World file")
