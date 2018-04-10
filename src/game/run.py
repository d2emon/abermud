from config import CONFIG
from d2log import logger, load_logger
from game.sigs import init
from game.talker import talker


def main(title='<untitled>', user=None):
    load_logger(logger)
    logger.debug('='*80)

    run_data = {
        'filename': CONFIG['EXE'],
        'title': title,
        'user': user,
    }
    logger.debug(run_data)

    print("="*80)
    print(CONFIG['EXE'])
    print("{}{}".format(title, user.username))

    from game.utils import PROGNAME
    PROGNAME = title
    logger.debug(PROGNAME)
    print("="*80)

    init()

    assert user is not None, "User don't exists"

    print("Entering Game ....")
    tty = 0
    # if tty == 4:
    #    # initbbc()
    #    # initscr()
    #    # topscr()
    print("Hello {}".format(user.showname))
    logger.info("GAME ENTRY: {}[{}]".format(user.showname, user.id))

    # keysetup();
    talker(user)


# char privs[4];
# listfl(name)
# char *getkbd(s,l)   /* Getstr() with length limit and filter ctrl */
# set_progname(n,text)
