import logging
import sys
from ..tk import get_name, set_name
from .error import on_error
from .user import User


def closeworld():
    raise NotImplementedError()


def get_in_fight():
    raise NotImplementedError()


def key_reprint():
    raise NotImplementedError()


def loseme():
    raise NotImplementedError()


def on_timing():
    raise NotImplementedError()


def openworld():
    raise NotImplementedError()


def rte(name):
    raise NotImplementedError()


def talker(name):
    raise NotImplementedError()


def main(game_user, program_name, username):
    print("Entering Game ....")
    if username == "Phantom":
        name = "The {}".format(username)
    else:
        name = username
    set_name(name)

    print("Hello {}".format(get_name()))
    logging.info("GAME ENTRY: %s[%s]", get_name(), game_user.user_id)

    return talker(get_name())


"""
listfl(name)
char *name;
{
FILE *a;
char b[128];
a=openlock(name,"r+");
while(fgets(b,128,a)) printf("%s\n",b);
fcloselock(a);
}

char *getkbd(s,l)   /* Getstr() with length limit and filter ctrl */
 char *s;
 int l;
    {
    char c,f,n;
    f=0;c=0;
    while(c<l)
       {
       regec:n=getchar();
       if ((n<' ')&&(n!='\n')) goto regec;
       if (n=='\n') {s[c]=0;f=1;c=l-1;}
       else
          s[c]=n;
       c++;
       }
    if (f==0) {s[c]=0;while(getchar()!='\n');}
    return(s);
    }
"""


# Signals

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
        pass

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

    def __on_time(self):
        if not self.active:
            return

        self.active = False

        openworld()

        self.interrupt = True
        rte(get_name())
        self.interrupt = False

        on_timing()
        closeworld()

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


"""
set_progname(n,text)
char *text;
{
	/*
	int x=0;
	int y=strlen(argv_p[n])+strlen(argv_p[1]);  
	y++;
	if(strcmp(argv_p[n],text)==0) return;

	while(x<y)
	   argv_p[n][x++]=0; 
	strcpy(argv_p[n],text);
	*/
}
"""
