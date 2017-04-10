active = False
alarm = 2
interrupt = False


SIGALRM = None
SIGHUP = None
SIGINT = None
SIGTERM = None
SIGTSTP = None
SIGQUIT = None
SIGCONT = None


def unblock_alarm():
    global active
    global alarm
    global SIGALRM

    SIGALRM = occur
    if active:
        alarm = 2


def block_alarm():
    global SIGALRM

    SIGALRM = None


def alon():
    global active
    global alarm
    global SIGALRM

    active = True
    SIGALRM = occur
    alarm = 2


def aloff():
    global active
    global alarm
    global SIGALRM

    active = False
    SIGALRM = None
    alarm = 2147487643


def init():
    global SIGHUP
    global SIGINT
    global SIGTERM
    global SIGTSTP
    global SIGQUIT
    global SIGCONT

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

    from game.utils import crapup
    crapup("Byeeeeeeeeee  ...........")


def occur():
    global active, interrupt

    if active == 0:
        return
    aloff()
    # openworld();
    interrupt = True
    # rte(globme);
    interrupt = False
    # on_timing();
    # closeworld();
    # key_reprint();
    alon()
