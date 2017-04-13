from game.share import player
from world import World

interrupt = False


SIGHUP = None
SIGINT = None
SIGTERM = None
SIGTSTP = None
SIGQUIT = None
SIGCONT = None


class Alarm():
    timer = 2
    sig = None
    active = False

    def block(self):
        import logging
        logging.debug("[[ ALARM blocked ]]")

        self.sig = None

    def unblock(self):
        import logging
        logging.debug("[[ ALARM unblocked ]]")

        self.sig = self.occur
        if self.active:
            self.timer = 2

    def set_on(self):
        import logging
        logging.debug("[[ ALARM is on ]]")

        self.active = True
        self.sig = alarm.occur
        self.timer = 2

    def set_off(self):
        import logging
        logging.debug("[[ ALARM is off ]]")

        self.active = False
        self.sig = None
        self.timer = 2147487643

    def occur(self):
        import logging
        logging.debug("SIGNAL_OCCUR")

        global interrupt

        if not self.active:
            return
        self.set_off()
        w = World()
        interrupt = True
        player.rte()
        interrupt = False
        # on_timing();
        w.closeworld()
        player.save()
        # key_reprint();
        self.set_on()


alarm = Alarm()


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
    import logging
    logging.debug("SIGNAL_OOPS")

    global alarm
    alarm.set_off()
    # loseme();
    # keysetback();

    import sys
    sys.exit(255)


def ctrlc():
    import logging
    logging.debug("SIGNAL_CTRLC")

    global alarm
    # extern in_fight;
    print("^C")
    # if in_fight:
    #    # return;
    alarm.set_off()
    # loseme();

    from game.utils import crapup
    crapup("Byeeeeeeeeee  ...........")
