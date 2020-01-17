import logging
from ..gamego.error import MudError
from ..gamego.signals import block_alarm, unblock_alarm
from ..opensys import World, WorldError


def dcprnt(messages, output):
    raise NotImplementedError()


def get_iskb():
    raise NotImplementedError()


def get_log_fl():
    raise NotImplementedError()


def get_pr_qcr():
    raise NotImplementedError()


def get_snoopd():
    raise NotImplementedError()


def get_snoopt():
    raise NotImplementedError()


def opensnoop(name, **kwargs):
    raise NotImplementedError()


def set_iskb(value):
    raise NotImplementedError()


def set_pr_due(value):
    raise NotImplementedError()


def set_pr_qcr(value):
    raise NotImplementedError()


def set_wd_her(value):
    raise NotImplementedError()


def set_wd_him(value):
    raise NotImplementedError()


def set_wd_it(value):
    raise NotImplementedError()


def set_wd_them(value):
    raise NotImplementedError()


def viewsnoop():
    raise NotImplementedError()


class MessageError(MudError):
    pass


class Messages:
    def __init__(self, user_id):
        self.user_id = user_id
        self.messages = ""

    def reset(self):
        self.messages = ""

    def add_message(self, message):
        if len(message) > 255:
            logging.error("Bprintf Short Buffer overflow")
            raise MudError("Internal Error in BPRINTF")
        if len(self.messages) + len(message) > 4095:
            logging.error("Buffer overflow on user {}".format(self.user_id))
            raise MessageError("PANIC - Buffer overflow")
        self.messages += message


__MESSAGES = Messages(None)


"""
long pr_due=0;
"""


def bprintf(message):
    return __MESSAGES.add_message(message)


"""
 /* The main loop */

void dcprnt(str,file)
 char *str;
 FILE *file;
    {
    long ct;
    ct=0;
    while(str[ct])
       {
       if(str[ct]!='\001'){fputc(str[ct++],file);continue;}
       ct++;
       switch(str[ct++])
          {
          case 'f':
             ct=pfile(str,ct,file);continue;
          case 'd':
             ct=pndeaf(str,ct,file);continue;
          case 's':
             ct=pcansee(str,ct,file);continue;
          case 'p':
             ct=prname(str,ct,file);continue;
          case 'c':
             ct=pndark(str,ct,file);continue;
          case 'P':
             ct=ppndeaf(str,ct,file);continue;
          case 'D':
             ct=ppnblind(str,ct,file);continue;
          case 'l':
             ct=pnotkb(str,ct,file);continue;
          default:
             strcpy(str,"");
             loseme();crapup("Internal $ control sequence error\n");
             }
       }
    }

int pfile(str,ct,file)
 char *str;
 FILE *file;
    {
    extern long debug_mode;
    char x[128];
    ct=tocontinue(str,ct,x,128);
    if(debug_mode) fprintf(file,"[FILE %s ]\n",str);
    f_listfl(x,file);
    return(ct);
    }

int pndeaf(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[256];
    extern long ail_deaf;
    ct=tocontinue(str,ct,x,256);
    if(!ail_deaf)fprintf(file,"%s",x);
    return(ct);
    }

 pcansee(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[25];
    char z[257];
    long a;
    ct=tocontinue(str,ct,x,23);
    a=PlayerData.by_name(x);
    if(!self.see_player(a))
       {
       ct=tocontinue(str,ct,z,256);
       return(ct);
       }
    ct=tocontinue(str,ct,z,256);
    fprintf(file,"%s",z);
    return(ct);
    }

 prname(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[24];
    ct=tocontinue(str,ct,x,24);
    if(!self.see_player(PlayerData.by_name(x)))
    fprintf(file,"Someone");
    else
      fprintf(file,"%s",x);
    return(ct);
    }


int pndark(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[257];
    extern long ail_blind;
    ct=tocontinue(str,ct,x,256);
    if((!isdark())&&(ail_blind==0))
    fprintf(file,"%s",x);
    return(ct);
    }

int tocontinue(str,ct,x,mx)
 char *str;
 long ct;
 char *x;
 long mx;
    {
    long s;
    s=0;
    while(str[ct]!='\001')
       {
       x[s++]=str[ct++];
       }
    x[s]=0;
if(s>=mx)
{
syslog("IO_TOcontinue overrun");
strcpy(str,"");
crapup("Buffer OverRun in IO_TOcontinue");
}
    return(ct+1);
    }
"""


"""
int ppndeaf(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[24];
    extern long ail_deaf;
    long a;
    ct=tocontinue(str,ct,x,24);
    if(ail_deaf) return(ct);
    a=PlayerData.by_name(x);
    if(self.see_player(a)) fprintf(file,"%s",x);
    else
      fprintf(file,"Someone");
    return(ct);
    }

int  ppnblind(str,ct,file)
char *str;
FILE *file;
    {
    extern long ail_blind;
    char x[24];
    long a;
    ct=tocontinue(str,ct,x,24);
    if(ail_blind) return(ct);
    a=PlayerData.by_name(x);
    if(self.see_player(a)) fprintf(file,"%s",x);
    else
       fprintf(file,"Someone");
    return(ct);
    }
"""


def reset_messages():
    __MESSAGES.reset()
    return __MESSAGES


"""
FILE * log_fl= 0; /* 0 = not logging */

void logcom()
    {
    extern FILE * log_fl;
    extern char globme[];
    if(getuid()!=geteuid()) {__MESSAGES.add_message("\nNot allowed from this ID");return;}
    if(log_fl!=0)
       {
       fprintf(log_fl,"\nEnd of log....\n\n");
       fclose(log_fl);
       log_fl=0;
       __MESSAGES.add_message("End of log");
       return;
       }
    __MESSAGES.add_message("Commencing Logging Of Session");
    log_fl=Service.connect("mud_log","a");
    if(log_fl==0) log_fl=Service.connect("mud_log","w");
    if(log_fl==0)
       {
       __MESSAGES.add_message("Cannot open log file mud_log");
       return;
       }
    __MESSAGES.add_message("The log will be written to the file 'mud_log'");
    }

long pr_qcr; 
"""


def pbfr():
    block_alarm()
    World.save()

    if len(__MESSAGES.messages):
        set_pr_due(True)
    if len(__MESSAGES.messages) and get_pr_qcr():
        print()
    set_pr_qcr(False)

    log_fl = get_log_fl()
    if log_fl is None:
        set_iskb(False)
        dcprnt(__MESSAGES.messages, log_fl)

    snoopd = get_snoopd()
    if snoopd is not None:
        try:
            fln = opensnoop(snoopd, append=True)
            set_iskb(False)
            dcprnt(__MESSAGES.messages, fln)
            fln.disconnect()
        except WorldError:
            pass

    set_iskb(True)
    dcprnt(__MESSAGES.messages, None)

    __MESSAGES.reset()
    if get_snoopt() is not None:
        viewsnoop()

    unblock_alarm()


"""
long iskb=1;
"""


"""
int pnotkb(str,ct,file)
 char *str;
 FILE *file;
    {
    extern long iskb;
    char x[128];
    ct=tocontinue(str,ct,x,127);
    if(iskb) return(ct);
    fprintf(file,"%s",x);
    return(ct);
    }

long snoopd= -1;

FILE *opensnoop(user,per)
char *per;
char *user;
    {
    FILE *x;
    char z[256];
    sprintf(z,"%s%s",SNOOP,user);
    x=Service.connect(z,per);
    return(x);
    }

long snoopt= -1;

char sntn[32];

void snoopcom()
    {
    FILE *fx;
    long x;
    if(player.__person.level<10)
       {
       __MESSAGES.add_message("Ho hum, the weather is nice isn't it");
       return;
       }
    if(snoopt!=-1)
       {
       __MESSAGES.add_message("Stopped snooping on %s",sntn);
       snoopt= -1;
       sendsys(sntn,globme,-400,0,"");
       }
    if(brkword()== -1)
       {
       return;
       }
    x=player.by_visibility(wordbuf);
    if(x==-1)
       {
       __MESSAGES.add_message("Who is that ?");
       return;
       }
    if(((player.__person.level<10000)&&(plev(x)>=10))||(ptstbit(x,6)))
       {
       __MESSAGES.add_message("Your magical vision is obscured");
       snoopt= -1;
       return;
       }
    strcpy(sntn,pname(x));
    snoopt=x;
    __MESSAGES.add_message("Started to snoop on %s",pname(x));
    sendsys(sntn,globme,-401,0,"");
    fx=opensnoop(globme,"w");
    fprintf(fx," ");
    fcloselock(fx);
    }

void viewsnoop()
    {
    long x;
    char z[128];
    FILE *fx;
    fx=opensnoop(globme,"r+");
    if(snoopt==-1) return;
    if(fx==0)return;
    while((!feof(fx))&&(fgets(z,127,fx)))
           printf("|%s",z);
    ftruncate(fileno(fx),0);
    fcloselock(fx);
    x=snoopt;
    snoopt= -1;
    /*
    pbfr();
    */
    snoopt=x;
    }
void chksnp()
{
if(snoopt==-1) return;
sendsys(sntn,globme,-400,0,"");
}
"""


def set_name(player):
    gender = player.gender
    if gender == player.GENDER_IT:
        set_wd_it(player.name)
        return
    elif gender == player.GENDER_SHE:
        set_wd_her(player.name)
    elif gender == player.GENDER_HE:
        set_wd_him(player.name)
    set_wd_them(player.name)
