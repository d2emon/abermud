from .errors import ServiceError


class Service:
    def __init__(self, path):
        self.path = path
        self.connected = False
        self.permissions = None
        self.contents = []

    def connect(self, permissions):
        self.connected = True
        self.permissions = permissions
        if not self.connected:
            raise ServiceError("Service {} not found".format(self.path))
        return self

    def disconnect(self):
        self.connected = False

    def lock(self):
        # if error == ENOSPC:
        #     raise ServiceError("PANIC exit device full")
        # elif error is not None:
        #     raise ServiceError("PANIC exit access failure, NFS gone for a snooze")
        return self

    def unlock(self):
        return self

    def push(self, value):
        self.contents.append(value)


# define UAF_RAND "/cygdrive/c/Programs/Adv/AberMUD2/mud/uaf.rand"
# define ROOMS "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/ROOMS/"
LOG_FILE = Service("/cygdrive/c/Programs/Adv/AberMUD2/mud/mud_syslog")
# define BAN_FILE "/cygdrive/c/Programs/Adv/AberMUD2/mud/banned_file"
# define NOLOGIN "/cygdrive/c/Programs/Adv/AberMUD2/mud/nologin"
# define RESET_T "/cygdrive/c/Programs/Adv/AberMUD2/mud/reset_t"
# define RESET_N "/cygdrive/c/Programs/Adv/AberMUD2/mud/reset_n"
# define RESET_DATA "/cygdrive/c/Programs/Adv/AberMUD2/mud/reset_data"
# define MOTD "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/gmotd2"
# define GWIZ "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/gwiz"
# define HELP1 "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/help1"
# define HELP2 "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/help2"
# define HELP3 "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/help3"
# define WIZLIST "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/wiz.list"
# define CREDITS "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/credits"
# define EXAMINES "/cygdrive/c/Programs/Adv/AberMUD2/mud/EXAMINES/"
# define LEVELS "/cygdrive/c/Programs/Adv/AberMUD2/mud/TEXT/level.txt"
# define PFL "/cygdrive/c/Programs/Adv/AberMUD2/mud/user_file"
# define PFT "/cygdrive/c/Programs/Adv/AberMUD2/mud/user_file.b"
# define EXE "/cygdrive/c/Programs/Adv/AberMUD2/mud/mud.exe"
# define EXE2 "/cygdrive/c/Programs/Adv/AberMUD2/mud/mud.1"
# define SNOOP "/cygdrive/c/Programs/Adv/AberMUD2/mud/SNOOP/"
# define HOST_MACHINE "DAVIDPOOTER"
