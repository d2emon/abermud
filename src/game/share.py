import logging
from logging.handlers import RotatingFileHandler
from player.models import Player


player = None
logger = logging.getLogger('game')


def load():
    global player
    player = Player()


def load_logger(logger):
    fh = RotatingFileHandler("mud.log", 'a', 1 * 1024 * 1024, 10)
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)


if player is None:
    load()
