import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('game')
mud_logger = logging.getLogger('mud')


def load_logger(logger):
    fh = RotatingFileHandler("mud.log", 'a', 1 * 1024 * 1024, 10)
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [%(name)s in %(pathname)s:%(lineno)d]'))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
