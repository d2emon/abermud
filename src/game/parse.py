'''
 Objects held in format
 
 [Short Text]
 [4 Long texts]
 [Max State]
 
 
 Objects in text file in form
 
 Stam:state:loc:flag
 
'''
 

from d2log import logger


# define  OBMUL 8

# extern char * oname();
# extern char * pname();
# extern FILE *openlock(); 
 
# long debug_mode=0;
 
# void sendsys(to,from,codeword,chan,text)
 
# char  strbuf[128];
# char  wordbuf[128]="";
# char  wd_it[64]="";
# char  wd_him[16]="";
# char  wd_her[16]="";
# char  wd_them[16]="";
# char  wd_there[128]="";
# long  stp;
 
# void pncom()

# chklist(word,lista,listb)
# int Match(x,y)
# chkverb()

# char *verbtxt[]={"go","climb","n","e","s","w","u","d",
#    "north","east","south","west","up","down",
#    "quit",
#    "get","take","drop","look","i","inv","inventory","who",
#    "reset","zap","eat","drink","play",
#    "shout","say","tell","save","score"
#    ,"exorcise","give","steal","pinch","levels","help","value"
#    ,"stats","examine","read","delete","pass","password",
#    "summon","weapon","shoot","kill","hit","fire","launch","smash","break",
#    "laugh","cry","burp","fart","hiccup","grin","smile","wink","snigger"
#    ,"pose","set","pray","storm","rain","sun","snow","goto",
#    "wear","remove","put","wave","blizzard","open","close",
#    "shut","lock","unlock","force","light","extinguish","where","turn",
#    "invisible","visible","pull","press","push","cripple","cure","dumb",
#    "change","missile","shock","fireball","translocate","blow",
#    "sigh","kiss","hug","slap","tickle","scream","bounce","wiz"
#    ,"stare","exits","crash","sing","grope","spray"
#    ,"groan","moan","directory","yawn","wizlist","in","smoke"
#    ,"deafen","resurrect","log","tss","rmedit","loc","squeeze","users"
#    ,"honeyboard","inumber","update","become","systat","converse"
#    ,"snoop","shell","raw","purr","cuddle","sulk","roll","credits"
#    ,"brief","debug","jump","wield","map","flee","bug","typo","pn"
#    ,"blind","patch","debugmode","pflags","frobnicate","strike"
#    ,"setin","setout","setmin","setmout","emote","dig","empty"
#    ,0 };
# int verbnum[]={1,1,2,3,4,5,6,7,2,3,4,5,6,7,8,9,9,10,11,12,12,12,13,14
#    ,15,16,16,17,18,19,20,21,22,23,24,25,25,26,27,28,29,30,30,31,32,32,33,34,35,35,35,35,35
#    ,35,35,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66
#    ,100,101,102,103,104,105,106,106,107,108,109,110,111,112,117,114,115,117,117,117
#    ,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133
#    ,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149
#    ,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170
#    ,171,172,34,173,174,175,176,177,178,179,180,181,182,35,183,184,185,186,187,188,189};
 
# char *exittxt[]={"north","east","south","west","up","down","n","e","s","w","u","d",0};
# long exitnum[]={1,2,3,4,5,6,1,2,3,4,5,6};
 
 # doaction(n)

# char in_ms[81]="has arrived.";
# char out_ms[81]="";
# char mout_ms[81]="vanishes in a puff of smoke.";
# char min_ms[81]="appears with an ear-splitting bang.";
# char here_ms[81]="is here";

# dogocom(n)
# dodirn(n)
 
# long tdes=0;
# long vdes=0;
# long rdes=0;
# long ades=0;
# long zapped;

# gamrcv(blok)
 
# long me_ivct=0;
# long last_io_interrupt=0;

# eorte()
 
# long me_drunk=0;
# long me_cal=0;

# rescom()
# lightning()
# eatcom()
# calibme()
# levelof(score)
# playcom()
# getreinput(blob)
# shoutcom()
# saycom()
# tellcom()
# scorecom()
# exorcom()
# givecom()
# dogive(ob,pl)
# stealcom()
# dosumm(loc)
# tsscom()
# rmeditcom()
# u_system()
# inumcom()
# updcom()
# becom()
# systat()
# convcom()
# shellcom()
# rawcom()
# rollcom()

# long brmode=0;
 
# debugcom()
# bugcom()
# typocom()
# look_cmd()
# set_ms(x)
# setmincom()
# setincom()
# setoutcom()
# setmoutcom()
# setherecom()
# digcom()
# emptycom()