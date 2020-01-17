from ..gamego.error import MudError
from ..opensys import World, WorldError


def cleanup(meta):
    raise NotImplementedError()


def longwthr():
    raise NotImplementedError()


def loseme():
    raise NotImplementedError()


class Event:
    def __init__(self, channel, codeword, users, payload):
        self.event_id = None
        self.channel = channel
        self.codeword = codeword
        self.users = users
        self.payload = payload

    def save(self):
        try:
            unit = World.load()
        except WorldError:
            loseme()
            raise MudError("AberMUD: FILE_ACCESS : Access failed")

        meta = unit.read(0, 64)
        first = meta.get('first', 0)
        last = meta.get('last', 0)
        self.event_id = last - first
        meta = {
            'first': first,
            'last': last,
        }
        unit.write(0, meta)
        unit.write(self.event_id, self)
        if self.event_id >= 199:
            cleanup(meta)
            longwthr()

    @classmethod
    def emit(cls, receiver, sender, codeword, channel, payload):
        cls(
            channel,
            codeword,
            [
                receiver,
                sender,
            ],
            payload,
        ).save()
