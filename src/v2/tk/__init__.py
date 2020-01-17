from ..bprintf import reset_messages, set_name, pbfr, MessageError
from ..gamego.error import MudError
from ..newuaf import new_person
from ..objsys import PlayerData
from ..opensys import World, WorldError


def getkbd(max_length):
    raise NotImplementedError()


def loseme():
    raise NotImplementedError()


def randperc():
    raise NotImplementedError()


def rte(name):
    raise NotImplementedError()


def sendmsg(name):
    raise NotImplementedError()


def sendsys(player_to, player_from, code, channel_id, message):
    raise NotImplementedError()


def trapch(channel_id):
    raise NotImplementedError()


class Actor:
    MODE_SPECIAL = 0
    MODE_GAME = 1

    def __init__(self):
        self.mode = self.MODE_SPECIAL


class Reader:
    def __init__(self):
        self.to_read = False
        self.__event_id = -1

    @property
    def event_id(self):
        return self.__event_id

    def reset(self):
        self.__event_id = -1


class Player:
    def __init__(self, name=""):
        self.__channel_id = 0
        self.in_game = False
        self.__player_id = 0

        self.__messages = reset_messages()
        self.reader = Reader()
        self.actor = Actor()
        self.__data = None
        self.__person = None

        if name == "Phantom":
            self.__name = "The {}".format(name)
        else:
            self.__name = name

    @property
    def player_id(self):
        return self.__player_id

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def name(self):
        return self.__name

    def start(self):
        self.__messages = reset_messages()
        self.reader.reset()

        try:
            World.load()
            self.__player_id = self.__new_player()
        except WorldError:
            raise MudError("Sorry AberMUD is currently unavailable")
        finally:
            World.save()

        self.reader.reset()
        special('.g', self)
        self.in_game = True

    def next_turn(self):
        pbfr()
        sendmsg(self.name)

        if self.reader.to_read:
            rte(self.name)
            self.reader.to_read = False

        World.save()
        pbfr()

    def __new_player(self):
        if PlayerData.by_name(self.name) is not None:
            raise MudError("You are already on the system - you may only be on once at a time")

        self.__data = next((p for p in PlayerData.players() if not p.exists), None)
        if self.__data is None:
            raise MudError("Sorry AberMUD is full at the moment")

        self.__data.reset()
        self.__data.name = self.name
        self.__data.channel_id = self.channel_id
        return self.__data.player_id

    def from_person(self, person):
        self.__channel_id = -5

        self.__person = person
        self.__data.strength = person.strength
        self.__data.level = person.level
        self.__data.visible = 0 if person.level < 10000 else 10000
        self.__data.weapon_id = -1
        self.__data.flags = person.sex
        self.__data.helping = -1

    def see_player(self, name):
        # fpbn
        player = PlayerData.by_visibility(self, name)
        if player is None:
            return True
        if self.player_id == player.player_id:
            return True
        set_name(player)
        return True

    def add_message(self, message):
        try:
            self.__messages.add_message(message)
        except MessageError as error:
            loseme()
            raise MudError(error)


"""
long  meall=0;
 /*
 
 Data format for mud packets
 
 Sector 0
 [64 words]
 0   Current first message pointer
 1   Control Word
 Sectors 1-n  in pairs ie [128 words]
 
 [channel][controlword][text data]
 
 [controlword]
 0 = Text
 - 1 = general request
 
 */
 
vcpy(dest,offd,source,offs,len)
long *dest,*source;
long offd,offs,len;
    {
    long c;
    c=0;
    while(c<len)
       {
       dest[c+offd]=source[c+offs];
       c++;
       }
    }
 
 mstoout(block,name)
 long *block;char *name;
    {
    extern long debug_mode;
    char luser[40];
    char *x;
    x=(char *)block;
    /* Print appropriate stuff from data block */
    strcpy(luser,name);lowercase(luser);
if(debug_mode)    player.add_message("\n<%d>",block[1]);
    if (block[1]<-3) sysctrl(block,luser);
    else
       player.add_message("%s", (x+2*sizeof(long)));
    }
 
long gurum=0;
long convflg=0;
 
sendmsg(name)
 char *name;
    {
    extern long debug_mode;
    extern char *sysbuf;
    extern long moni;
    char prmpt[32];
    long a;
extern long tty;
    char work[200];
    long w2[35];
    extern char key_buff[];
    extern long convflg;
extern long in_fight;
extern long fighting;
    l:pbfr();
if(tty==4) btmscr();
strcpy(prmpt,"\r");
    if(pvis(player.player_id)) strcat(prmpt,"(");
    if(debug_mode) strcat(prmpt,"#");
    if(player.__person.level>9)strcat(prmpt,"----");
    switch(convflg)
       {
       case 0:
          strcat(prmpt,">");
          break;
       case 1:
          strcat(prmpt,"\"");
          break;
       case 2:
          strcat(prmpt,"*");
          break;
       default:
          strcat(prmpt,"?");
          }
    if(pvis(player.player_id)) strcat(prmpt,")");
    pbfr();
    if(pvis(player.player_id)>9999) set_progname(0,"-csh");
    else
    sprintf(work,"   --}----- ABERMUD -----{--     Playing as %s",name);
    if(pvis(player.player_id)==0) set_progname(0,work);
    sig_alon();
    key_input(prmpt,80);
    sig_aloff();
    strcpy(work,key_buff);
if(tty==4) topscr();
strcat(sysbuf,"\001l");
strcat(sysbuf,work);
strcat(sysbuf,"\n\001");
World.load()
rte(name);
World.save()
    if((convflg)&&(!strcmp(work,"**")))
       {
       convflg=0;
       goto l;
       }
    if(!strlen(work)) goto nadj;
if((strcmp(work,"*"))&&(work[0]=='*')){(work[0]=32);goto nadj;}
    if(convflg)
       {
       strcpy(w2,work);
       if(convflg==1) sprintf(work,"say %s",w2);
       else
          sprintf(work,"tss %s",w2);
       }
    nadj:if(player.actor.mode == 1) gamecom(work);
    else
       {
       if(((strcmp(work,".Q"))&&(strcmp(work,".q")))&& (!!strlen(work)))
          {
          a=special(work, player);
          }
       }
if(fighting>-1)
{
if(!strlen(pname(fighting))) 
{
in_fight=0;
fighting= -1;
}
if(ploc(fighting)!=player.channel_id) 
{
in_fight=0;
fighting= -1;
}
}
if(in_fight) in_fight-=1;
    return((!strcmp(work,".Q"))||(!strcmp(work,".q")));
    }
 
 send2(block)
 long *block;
    {
    FILE * unit;
    long number;
    long inpbk[128];
    extern char *echoback;
    	unit=World.load()
    if (unit<0) {loseme();raise MudError("\nAberMUD: FILE_ACCESS : Access failed\n");}
    sec_read(unit,inpbk,0,64);
    number=2*inpbk[1]-inpbk[0];inpbk[1]++;
    sec_write(unit,block,number,128);
    sec_write(unit,inpbk,0,64);
    if (number>=199) cleanup(inpbk);
    if(number>=199) longwthr();
    }
 
 readmsg(channel,block,num)
 long channel;
 long *block;
 int num;
    {
    long buff[64],actnum;
    sec_read(channel,buff,0,64);
    actnum=num*2-buff[0];
    sec_read(channel,block,actnum,128);
    }
 
FILE *fl_com;
extern long findstart();
extern long findend();
 
 rte(name)
 char *name;
    {
    extern long vdes,tdes,rdes;
    extern FILE *fl_com;
    extern long debug_mode;
    FILE *unit;
    long too,ct,block[128];
    unit=World.load()
    fl_com=unit;
    if (unit==NULL) raise MudError("AberMUD: FILE_ACCESS : Access failed\n");
    if (player.reader.event_id== -1) player.reader.event_id=findend(unit);
    too=findend(unit);
    ct=player.reader.event_id;
    while(ct<too)
       {
       readmsg(unit,block,ct);
       mstoout(block,name);
       ct++;
       }
    player.reader.event_id=ct;
    update(name);
    eorte();
    rdes=0;tdes=0;vdes=0;
    }
    
long findstart(unit)
 FILE *unit;
    {
    long bk[2];
    sec_read(unit,bk,0,1);
    return(bk[0]);
    }
 
long findend(unit)
 FILE *unit;
    {
    long bk[3];
    sec_read(unit,bk,0,2);
    return(bk[1]);
    }
"""


def talker(player):
    player.start()
    while True:
        player.next_turn()


"""
 cleanup(inpbk)
 long *inpbk;
    {
    FILE * unit;
    long buff[128],ct,work,*bk;
    unit=World.load()
    bk=(long *)malloc(1280*sizeof(long));
    sec_read(unit,bk,101,1280);sec_write(unit,bk,1,1280);
    sec_read(unit,bk,121,1280);sec_write(unit,bk,21,1280);
    sec_read(unit,bk,141,1280);sec_write(unit,bk,41,1280);
    sec_read(unit,bk,161,1280);sec_write(unit,bk,61,1280);
    sec_read(unit,bk,181,1280);sec_write(unit,bk,81,1280);
    free(bk);
    inpbk[0]=inpbk[0]+100;
    sec_write(unit,inpbk,0,64);
    revise(inpbk[0]);
    }
"""


def __new_person(player):
    def f():
        def __get_sex():
            player.add_message("\nSex (M/F) : ")
            pbfr()
            sex = getkbd(2).lower()[0]
            if sex == 'm':
                return 0
            elif sex == 'f':
                return 1
            player.add_message("M or F")
            __get_sex()

        player.add_message("Creating character....")
        return {
            'sex': __get_sex()
        }
    return f


def __start_game(player):
    player.actor.mode = Actor.MODE_GAME

    World.load()

    try:
        player.from_person(new_person(player.name, on_new=__new_person(player)))
    except WorldError as error:
        player.add_message(error)

    sendsys(
        player.name,
        player.name,
        -10113,
        player.channel_id,
        "[s name=\"{name}\"][ {name}  has entered the game ][/s]".format(name=player.name),
    )
    rte(player.name)
    if randperc() > 50:
        trapch(-5)
    else:
        player.channel_id = -183
        trapch(-183)
    sendsys(
        player.name,
        player.name,
        -10000,
        player.channel_id,
        "[s name=\"{name}\"]{name}  has entered the game[/s]".format(name=player.name),
    )


def special(code, player):
    if len(code) < 2 or code[0] != '.':
        return False
    code = code.lower()
    if code[1] == 'g':
        __start_game(player)
    else:
        print("Unknown . option")
    return True


"""
long dsdb=0;
 
 
long moni=0;
 
 broad(mesg)
 char *mesg;
    {
char bk2[256];
long block[128];
    __READER.to_read = True
block[1]= -1;
strcpy(bk2,mesg);
vcpy(block,2,(long *)bk2,0,126);
send2(block);
}

tbroad(message)
char *message;
    {
    broad(message);
    }
    
 sysctrl(block,luser)
 long *block;
 char *luser;
    {
    gamrcv(block);
    }
long  bound=0;
long  tmpimu=0;
char  *echoback="*e";
char  *tmpwiz=".";/* Illegal name so natural immunes are ungettable! */
 
 split(block,nam1,nam2,work,luser)
 long *block;
 char *nam1;
 char *nam2;
 char *work;
 char *luser;
    {
    long wkblock[128],a;
    vcpy(wkblock,0,block,2,126);
    vcpy((long *)work,0,block,64,64);
    a=scan(nam1,(char *)wkblock,0,"",".");
    scan(nam2,(char *)wkblock,a+1,"",".");
if((strncmp(nam1,"The ",4)==0)||(strncmp(nam1,"the ",4)==0))
{
if(!strcmp(lowercase(nam1+4),lowercase(luser))) return(1);
}
    return(!strcmp(lowercase(nam1),lowercase(luser)));
    }
 trapch(chan)
 long chan;
    {
    FILE *unit;
    if(player.__person.level>9) goto ndie;
    ndie:unit=World.load()
    setploc(player.player_id,chan);
    lookin(chan);
    }
"""


"""
 loseme(name)
 char *name;
    {
extern long iamon;
extern long zapped;
char bk[128];
FILE *unit;  
sig_aloff(); /* No interruptions while you are busy dying */
			/* ABOUT 2 MINUTES OR SO */
player.in_setup = False
i_setup=0;
			   
unit=World.load()
    dumpitems();
if(pvis(player.player_id)<10000) {
sprintf(bk,"%s has departed from AberMUDII\n", player.name);
sendsys(player.name,player.name,-10113,0,bk);
}
    pname(player.player_id)[0]=0;
World.save()
if(!zapped) saveme();
    	chksnp();
    }
 
long lasup=0;

 update(name)
 char *name;
    {
    FILE *unit;
    long xp;
    extern long lasup;
    xp=player.reader.event_id-lasup;
    if(xp<0) xp= -xp;
    if(xp<10) goto noup;
    unit=World.load()
    setppos(player.player_id,player.reader.event_id);
    lasup=player.reader.event_id;
    noup:;
    }
 
 revise(cutoff)
 long cutoff;
    {
    char mess[128];
    long ct;
    FILE *unit;
    unit=World.load()
    ct=0;
    while(ct<16)
       {
       if((pname(ct)[0]!=0)&&(ppos(ct)<cutoff/2)&&(ppos(ct)!=-2))
          {
          sprintf(mess,"%s%s",pname(ct)," has been timed out\n");
          broad(mess);
          dumpstuff(ct,ploc(ct));
          pname(ct)[0]=0;
          }
       ct++;
       }
    }
 
 lookin(room)
 long room; /* Lords ???? */
    {
    FILE *un1,un2;
    char str[128];
    long xxx;
    extern long brmode;
    extern long ail_blind;
    long ct;
World.save()
    if(ail_blind)
    {
    	player.add_message("You are blind... you can't see a thing!\n");
    }
    if(player.__person.level>9) showname(room);
    un1=openroom(room,"r");
    if (un1!=NULL)
    {
xx1:   xxx=0;
       lodex(un1);
       	if(isdark())
       	{
       	    un1.disconnect()
          		player.add_message("It is dark\n");
                        World.load()
          		onlook();
          		return;
          	}
       while(getstr(un1,str)!=0)
          {
          if(!strcmp(str,"#DIE"))
             {
             if(ail_blind) {rewind(un1);ail_blind=0;goto xx1;}
             if(player.__person.level>9)player.add_message("<DEATH ROOM>\n");
             else
                {
                loseme(player.name);
                raise MudError("bye bye.....\n");
                }
             }
          else
{
if(!strcmp(str,"#NOBR")) brmode=0;
else
             if((!ail_blind)&&(!xxx))player.add_message("%s\n",str);
          xxx=brmode;
}
          }
       }
    else
       player.add_message("\nYou are on channel %d\n",room);
    un1.disconnect()
    World.load()
    if(!ail_blind)
    {
	    lisobs();
	    if(player.actor.mode == 1) lispeople();
    }
    player.add_message("\n");
    onlook();
    }
 loodrv()
    {
    lookin(player.channel_id);
    }
 

long iamon=0;

userwrap()
{
extern long iamon;
if(PlayerData.by_name(player.name)!= -1) {loseme();syslog("System Wrapup exorcised %s",player.name);}
}
"""