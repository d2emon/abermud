import logging
from logging.handlers import RotatingFileHandler
from config import CONFIG


logger = logging.getLogger('game')
mud_logger = logging.getLogger('mud')


def load_logger(l=None, filename=None):
    if l is None:
        l = logger
    if filename is None:
        filename = CONFIG.get("LOG_FILE", "mud.log")
    l.setLevel(logging.DEBUG)

    fh = RotatingFileHandler(filename, 'a', 1 * 1024 * 1024, 10)
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [%(name)s in %(pathname)s:%(lineno)d]'))
    fh.setLevel(logging.INFO)
    l.addHandler(fh)

    dh = RotatingFileHandler("debug.log", 'a', 1 * 1024 * 1024, 10)
    dh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [%(name)s in %(pathname)s:%(lineno)d]'))
    dh.setLevel(logging.DEBUG)
    l.addHandler(dh)
