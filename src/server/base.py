from .formatter import Formatter


class BaseServer:
    def __init__(self, config=dict()):
        self.config = config

    def stats(self):
        return {
            'created': None,
            'elapsed': None,
        }


    def mudStats(self):
        data = self.stats()
        print(data)
        return Formatter.created(data), Formatter.elapsed(data)
