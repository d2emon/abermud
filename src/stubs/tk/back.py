from ..errors import PlayerIsDead
from ..parse import gamrcv, eorte
from ..support import Player
from .message import Message
from .world import World


# State
global_state = {
    '__first_message': 0,
    '__last_message': 0,
    '__messages': [],

    'i_setup': False,

    'cms': -1,
    'curch': 0,
    'name': '',
    'curmode': 0,

    'convflg': 0,

    'rd_qd': 0,

    'mynum': 0,
}

__last_save = 0


# Mutations
def set_message_id(state, player_id, message_id):
    global __last_save

    state['cms'] = message_id

    if abs(message_id - __last_save) < 10:
        return state

    world = World(state)
    setppos(world, player_id, message_id)
    __last_save = message_id
    return world.state


def set_channel(world, player_id, channel):
    player = Player(world.state, player_id)
    player.location = channel
    return world


# Actions
def process_messages(state, player_id, message_id):
    world = World(state)

    first_message_id = message_id if message_id != -1 else world.last_message_id
    state = world.state
    for message in world.get_messages(first_message_id):
        state = gamrcv(state, message)
    state = set_message_id(state, player_id, world.last_message_id)

    state = eorte(state)
    state.update({
        'rdes': 0,
        'tdes': 0,
        'vdes': 0,
    })
    return state


def broadcast(world, message):
    world.state['rd_qd'] = True
    world.send_message(Message(text=message))
    return world.state


def __parse_room_file(room_file):
    lodex(room_file)
    is_death = False
    is_verbose = False
    title = None
    text = []

    for i, s in enumerate(room_file):
        if s == "#DIE":
            is_death = True
        elif s == "#NOBR":
            is_verbose = True
        elif i == 0:
            title = s
        else:
            text.append(s)

    return {
        'title': title,
        'text': "\n".join(text),
        'is_dark': isdark(),
        'is_death': is_death,
        'is_verbose': is_verbose,
    }


def __parse_no_room_file(room_id):
    return {
        'title': '',
        'text': "You are on channel {}\n".format(room_id),
        'is_dark': False,
        'is_death': False,
        'is_verbose': False,
    }


def look(world, room):
    world.save()
    state = world.state

    if state['ail_blind']:
        state = state['bprintf'](state, "You are blind... you can't see a thing!\n")

    if state['my_lev'] > 9:
        showname(room)

    try:
        un1 = openroom(room, 'r')
        room_data = __parse_room_file(un1)
        un1.close()
    except Exception:
        room_data = __parse_no_room_file(room)

    world.load()

    if room_data['is_dark']:
        world.state = state['bprintf'](state, "It is dark\n")
        onlook()
        return world

    if room_data['is_verbose']:
        world.state['brmode'] = False

    if not world.state['ail_blind'] or room_data['is_death']:
        world.state = world.state['bprintf'](world.state, "{}\n".format(room_data['title']))
        if not world.state['brmode']:
            world.state = world.state['bprintf'](world.state, room_data['text'])

    if room_data['is_death']:
        if world.state['my_lev'] > 9:
            world.state = world.state['bprintf'](world.state, "<DEATH ROOM>\n")
        else:
            raise PlayerIsDead("bye bye.....")

    if not world.state['ail_blind']:
        lisobs()
        if world.state['curmode']:
            lispeople()

    world.state = world.state['bprintf'](world.state, "\n")
    onlook()
    return world


def change_channel(state, channel):
    world = World(state)
    world.state = set_channel(world, state['mynum'], channel)
    return look(world, channel).state
