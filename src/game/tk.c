/*
 *
 *		AberMUD II   C
 *
 *
 *	This game systems, its code scenario and design
 *	are (C) 1987/88  Alan Cox,Jim Finnis,Richard Acott
 *
 *
 *	This file holds the basic communications routines
 *
 */
 
#include "files.h"
#include "flock.h"

long i_setup=0;
long oddcat=0;
long  talkfl=0;

#include <stdio.h>
#include <sys/errno.h>
#include <sys/file.h>

extern FILE * openlock();
extern char globme[];
extern long cms;
extern long curch;
extern long my_str;
extern long my_sex;
extern long my_lev;
extern FILE * openroom(); 
extern FILE * openworld();
extern char * pname();
extern char * oname();
extern long ppos();
extern char key_buff[];
long cms= -1;
long curch=0;
 
char globme[40];
long  curmode=0;
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
if(debug_mode)    bprintf("\n<%d>",block[1]);
    if (block[1]<-3) sysctrl(block,luser);
    else
       bprintf("%s", (x+2*sizeof(long)));
    }
 
long gurum=0;
long convflg=0;
 
sendmsg(name)
 char *name;
    {
    extern long debug_mode;
    extern char *sysbuf;
    extern long curch,moni,mynum;
    char prmpt[32];
    long a;
extern long tty;
    char work[200];
    long w2[35];
    extern char key_buff[];
    extern long convflg;
    extern long my_lev;
extern long my_str;
extern long in_fight;
extern long fighting;
    extern long curmode;
    l:pbfr();
if(tty==4) btmscr();
strcpy(prmpt,"\r");
    if(pvis(mynum)) strcat(prmpt,"(");
    if(debug_mode) strcat(prmpt,"#");
    if(my_lev>9)strcat(prmpt,"----");
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
    if(pvis(mynum)) strcat(prmpt,")");
    pbfr();
    if(pvis(mynum)>9999) set_progname(0,"-csh");
    else
    sprintf(work,"   --}----- ABERMUD -----{--     Playing as %s",name);
    if(pvis(mynum)==0) set_progname(0,work);
    sig_alon();
    key_input(prmpt,80);
    sig_aloff();
    strcpy(work,key_buff);
if(tty==4) topscr();
strcat(sysbuf,"\001l");
strcat(sysbuf,work);
strcat(sysbuf,"\n\001");
openworld();
rte(name);
closeworld();
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
    nadj:if(curmode==1) gamecom(work);
    else
       {
       if(((strcmp(work,".Q"))&&(strcmp(work,".q")))&& (!!strlen(work)))
          {
          a=special(work,name);
          }
       }
if(fighting>-1)
{
if(!strlen(pname(fighting))) 
{
in_fight=0;
fighting= -1;
}
if(ploc(fighting)!=curch) 
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
    extern long cms;
    extern long vdes,tdes,rdes;
    extern FILE *fl_com;
    extern long debug_mode;
    FILE *unit;
    long too,ct,block[128];
    unit=openworld();
    fl_com=unit;
    if (unit==NULL) crapup("AberMUD: FILE_ACCESS : Access failed\n");
    if (cms== -1) cms=findend(unit);
    too=findend(unit);
    ct=cms;
    while(ct<too)
       {
       readmsg(unit,block,ct);
       mstoout(block,name);
       ct++;
       }
    cms=ct;
    update(name);
    eorte();
    rdes=0;tdes=0;vdes=0;
    }
    
FILE *openlock(file,perm)
char *file;
char *perm;
    {
    FILE *unit;
    long ct;
    extern int errno;
    extern char globme[];
    ct=0;
   unit=fopen(file,perm);
   if(unit==NULL) return(unit);
   /* NOTE: Always open with R or r+ or w */
intr:if(flock(fileno(unit),LOCK_EX)== -1)
		if(errno==EINTR) goto intr; /* INTERRUPTED SYSTEM CALL CATCH */
    switch(errno)
    {
    	case ENOSPC:crapup("PANIC exit device full\n");
/*    	case ESTALE:;*/
    	case EHOSTDOWN:;
    	case EHOSTUNREACH:crapup("PANIC exit access failure, NFS gone for a snooze");
    }
    return(unit);
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
 
 
 talker(name)
 char *name;
    {
    extern long curch,cms;
    extern long mynum;
    extern long maxu;
    extern long rd_qd;
    FILE *fl;
    char string[128];
    extern char globme[];
    makebfr();
    	cms= -1;putmeon(name);
    if(openworld()==NULL) crapup("Sorry AberMUD is currently unavailable");
    if (mynum>=maxu) {printf("\nSorry AberMUD is full at the moment\n");return(0);}
    strcpy(globme,name);
    rte(name);
    	closeworld();
    cms= -1;
    special(".g",name);
    i_setup=1;
    while(1)
       {
       pbfr();
       sendmsg(name);
       if(rd_qd) rte(name);
       rd_qd=0;
       closeworld();
       pbfr();
       }
    }
    
long rd_qd=0;
 
 cleanup(inpbk)
 long *inpbk;
    {
    }
 
 
 
 special(string,name)
 char *string,*name;
    {
    extern long curmode;
    char ch,bk[128];
    extern long curch,moni;
    extern long mynum;
    extern long my_str,my_lev,my_sco,my_sex;
    FILE * ufl;
    char xx[128];
    char xy[128];
    char us[32];
    strcpy(bk,string);
    lowercase(bk);
    ch= *bk;
    if (ch!='.') return(0);
    ch=bk[1];
    switch(ch)
       {
       case 'g':
          curmode=1;
          curch= -5;
          initme();
          ufl=openworld();
          setpstr(mynum,my_str);
          setplev(mynum,my_lev);
 if(my_lev<10000) setpvis(mynum,0);
    else setpvis(mynum,10000);
          setpwpn(mynum,-1);
          setpsexall(mynum,my_sex);
          setphelping(mynum,-1);
          cuserid(us);
          sprintf(xy,"\001s%s\001%s  has entered the game\n\001",name,name);
          sprintf(xx,"\001s%s\001[ %s  has entered the game ]\n\001",name,name);
          sendsys(name,name,-10113,curch,xx);
          rte(name);
          if(randperc()>50)trapch(-5);
else{curch= -183;trapch(-183);}
sendsys(name,name,-10000,curch,xy);
          break;
       default:
          printf("\nUnknown . option\n");
          }
    return(1);
    }
 
 
 
long dsdb=0;
 
 
long moni=0;
 
 broad(mesg)
 char *mesg;
    {
extern long rd_qd;
char bk2[256];
long block[128];
rd_qd=1;
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
    }
 
long mynum=0;
 
 putmeon(name)
 char *name;
    {
    }
 
 loseme(name)
 char *name;
    {
extern long iamon;
extern long mynum;
extern long zapped;
char bk[128];
extern char globme[];
FILE *unit;  
sig_aloff(); /* No interruptions while you are busy dying */
			/* ABOUT 2 MINUTES OR SO */
i_setup=0;
			   
unit=openworld();
    dumpitems();
if(pvis(mynum)<10000) {
sprintf(bk,"%s has departed from AberMUDII\n",globme);
sendsys(globme,globme,-10113,0,bk);
}
    pname(mynum)[0]=0;
    	closeworld();
if(!zapped) saveme();
    	chksnp();
    }
 
long lasup=0;

 update(name)
 char *name;
    {
    }
 
 revise(cutoff)
 long cutoff;
    {
    }
 
 lookin(room)
 long room; /* Lords ???? */
    {
    }
 loodrv()
    {
    extern long curch;
    lookin(curch);
    }
 

long iamon=0;

userwrap()
{
extern char globme[];
extern long iamon;
if(fpbns(globme)!= -1) {loseme();syslog("System Wrapup exorcised %s",globme);}
}
