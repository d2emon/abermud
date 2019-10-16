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


def __load_messages(state):
    state.update({
        '__first_message': world.contents['first_message'],
        '__last_message': world.contents['last_message'],
        '__messages': world.contents['messages'],
    })
    return state


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
        state.update({
            'objinfo': world.contents['items'],
            'ublock': world.contents['players'],
        })
        return __load_messages(state)
    except ServiceError:
        raise WorldError("Cannot find World file")


def add_message(state, message):
    world.contents['last_message'] += 1
    world.contents['messages'].append(message)
    return __load_messages(state)


def cleanup(state):
    state = open_world(state)
    world.contents['first_message'] += 100
    world.contents['messages'] = world.contents['messages'][100:]
    return __load_messages(state)
