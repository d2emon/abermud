import sys
from .error import on_error
from ..opensys import World


def get_in_fight():
    raise NotImplementedError()


def loseme():
    raise NotImplementedError()


def key_reprint():
    raise NotImplementedError()


def on_timing():
    raise NotImplementedError()


def rte(name):
    raise NotImplementedError()


class Signals:
    def __init__(self):
        self.__active = False
        self.__alarm = None
        self.interrupt = False
        self.__signals = {
            'SIGHUP': self.__on_error,
            'SIGINT': self.__on_close,
            'SIGTERM': self.__on_close,
            'SIGTSTP': None,
            'SIGQUIT': None,
            'SIGCONT': self.__on_error,
        }

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value
        if value:
            self.blocked = False
            self.__alarm = 2
        else:
            self.blocked = True
            self.__alarm = 2147487643

    @property
    def blocked(self):
        return self.__signals.get('SIGALRM') is None

    @blocked.setter
    def blocked(self, value):
        if value:
            self.__signals['SIGALRM'] = None
        else:
            self.__signals['SIGALRM'] = self.__on_time
            if self.__active:
                self.__alarm = 2

    def signal(self, signal_id):
        return self.__signals[signal_id]

    def __shutdown(self):
        self.active = False
        loseme()

    def __on_close(self):
        print("^C")

        if get_in_fight():
            return

        self.__shutdown()
        on_error("Byeeeeeeeeee  ...........")

    def __on_error(self):
        self.__shutdown()
        sys.exit(255)

    def __on_time(self, player):
        if not self.active:
            return

        self.active = False

        World.load()

        self.interrupt = True
        rte(player.name)
        self.interrupt = False

        on_timing()
        World.save()

        key_reprint()

        self.active = True


__SIGNALS = Signals()


def unblock_alarm():
    __SIGNALS.blocked = False


def block_alarm():
    __SIGNALS.blocked = True


def sig_alon():
    __SIGNALS.active = True


def sig_aloff():
    __SIGNALS.active = False
