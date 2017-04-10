from game.utils import crapup


active = False


SIGALRM = None
SIGHUP = None
SIGINT = None
SIGTERM = None
SIGTSTP = None
SIGQUIT = None
SIGCONT = None


def aloff():
    global active
    global SIGALRM
    active = False
    SIGALRM = None
    # alarm(2147487643)


def init():
    SIGHUP = oops
    SIGINT = ctrlc
    SIGTERM = ctrlc
    SIGTSTP = None
    SIGQUIT = None
    SIGCONT = oops


def oops():
    aloff()
    # loseme();
    # keysetback();

    import sys
    sys.exit(255)


def ctrlc():
    # extern in_fight;
    print("^C")
    # if in_fight:
    #    # return;
    aloff()
    # loseme();
    crapup("Byeeeeeeeeee  ...........")
