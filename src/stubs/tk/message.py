class Message:
    def __init__(
        self,
        channel=None,
        code=-1,
        receiver=None,
        sender=None,
        text=''
    ):
        self.channel = channel
        self.code = code
        self.receiver = receiver
        self.sender = sender
        self.text = text

    def is_me(self, receiver):
        receiver_name = self.receiver.lower()
        names = [receiver_name]
        if receiver_name[:4] == "the ":
            names.append(receiver_name[4:])
        return any(name for name in names if name == receiver)
