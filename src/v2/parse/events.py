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
            world = World.load()
        except WorldError:
            loseme()
            raise MudError("AberMUD: FILE_ACCESS : Access failed")

        world.add_event(self)
        if self.event_id >= 199:
            meta = world.read_meta()
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
