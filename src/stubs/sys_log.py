import logging
from .errors import SysLogError


logger = logging.getLogger('Aber')
logger.setLevel(logging.INFO)


def syslog(message):
    try:
        # service = LOG_FILE.connect('a').lock()
        # service.push("{}:\t{}".format(datetime.utcnow(), message))
        # service.disconnect()
        logger.debug(message)
    except Exception:
        # loseme(state)
        raise SysLogError("Log fault : Access Failure")
