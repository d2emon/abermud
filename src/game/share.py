from player.models import Player


player = None


def load():
    global player
    player = Player()


if player is None:
    load()
