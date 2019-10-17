from ..errors import WorldError
from ..opensys import open_world, close_world, add_message, cleanup
from ..support import Player
from .message import Message


class World:
    def __init__(self, state):
        self.state = state
        self.load()

    def load(self):
        try:
            self.state = open_world(self.state)
        except WorldError:
            raise WorldError("AberMUD: FILE_ACCESS : Access failed")

    def save(self):
        close_world(self.state)

    @property
    def first_message_id(self):
        return self.state['__first_message']

    @property
    def last_message_id(self):
        return self.state['__last_message']

    @property
    def is_full(self):
        return self.last_message_id - self.first_message_id >= 199

    def __revise(self, message_id):
        player_ids = (i for i in range(16) if pname(i) and ppos(i) < message_id / 2 and ppos(i) != -2)
        for player_id in player_ids:
            player = Player(self.state, player_id)
            self.state['rd_qd'] = True
            self.send_message(Message(text="{} has been timed out\n".format(pname(player.player_id))))
            dumpstuff(player.player_id, player.location)
            setpname(player.player_id, '')

    def get_message(self, message_id):
        return self.state['__messages'][message_id - self.first_message_id]

    def get_messages(self, first, last=None):
        if last is None:
            last = self.last_message_id

        for message_id in range(first, last + 1):
            yield self.get_message(message_id)

    def send_message(self, message):
        try:
            self.state = add_message(self.state, message)
        except WorldError:
            raise WorldError("AberMUD: FILE_ACCESS : Access failed")

        if not self.is_full:
            return

        self.state = cleanup(self.state)
        self.__revise(self.last_message_id)
        longwthr()
