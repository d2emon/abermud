from getpass import getpass
from d2log import mud_logger as logger

import sys


# include <stdio.h>
# include <sys/errno.h>
# include <sys/file.h>
# include "object.h"
# include "System.h"
# include "flock.h"


def qcrypt(s):
    return s


def dcrypt(s):
    return s


ttyt = 0


def getty():
    logger.debug("--->\tgetty()")
    return "TTY"


# FILE *openlock(file,perm)
# void fcloselock(file)


def validname(name):
    return True


# int resword(name)

# extern OBJECT objects[];

# fobn(name)


def crapup(ptr):
    getpass("\n{}\n\nHit Return to Continue...\n".format(ptr))
    sys.exit(0)
