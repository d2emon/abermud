import logging
import sys


class User:
    def __init__(self, user_id):
        self.user_id = user_id


def get_in_fight():
    raise NotImplementedError()


def loseme():
    raise NotImplementedError()


def pbfr():
    raise NotImplementedError()


def set_pr_due(value):
    raise NotImplementedError()


def sig_aloff():
    raise NotImplementedError()


def talker(name):
    raise NotImplementedError()


def main(user, program_name, username):
    __sig_init()

    print("Entering Game ....")
    if username == "Phantom":
        name = "The {}".format(username)
    else:
        name = username

    print("Hello {}".format(name))
    logging.info("GAME ENTRY: %s[%s]", name, user.user_id)
    return talker(name)


__dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


def crapup(message):
    pbfr()
    set_pr_due(0)
    print("\n{dashes}\n{message}\n{dashes}".format(
        dashes=__dashes,
        message=message,
    ))
    sys.exit(0)


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

signals = {}

"""
#include <signal.h>

long sig_active=0;

sig_alon()
{
	extern int sig_occur();
	sig_active=1;	
	signal(SIGALRM,sig_occur);
	alarm(2);
}



unblock_alarm()
{
	extern int sig_occur();
	signal(SIGALRM,sig_occur);
	if(sig_active) alarm(2);
}

block_alarm()
{
	signal(SIGALRM,SIG_IGN);
}


sig_aloff()
{
	sig_active=0;	
	signal(SIGALRM,SIG_IGN);
	alarm(2147487643);
}

long interrupt=0;

sig_occur()
{
	extern char globme[];
	if(sig_active==0) return;
	sig_aloff();
	openworld();
	interrupt=1;
	rte(globme);
	interrupt=0;
	on_timing();
	closeworld();
	key_reprint();
	sig_alon();
}

	
"""


def __shutdown():
    sig_aloff()
    loseme()


def __sig_init():
    signals['SIGHUP'] = __sig_oops
    signals['SIGINT'] = __sig_ctrlc
    signals['SIGTERM'] = __sig_ctrlc
    signals['SIGTSTP'] = None
    signals['SIGQUIT'] = None
    signals['SIGCONT'] = __sig_oops


def __sig_ctrlc():
    print("^C")
    if get_in_fight():
        return
    __shutdown()
    crapup("Byeeeeeeeeee  ...........")


def __sig_oops():
    __shutdown()
    sys.exit(255)


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
