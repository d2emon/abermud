'''

                AberMUD II   C


        This game systems, its code scenario and design
        are (C) 1987/88  Alan Cox,Jim Finnis,Richard Acott


        This file holds the basic communications routines

'''
from player.models import MAX_PLAYERS, Player
from bprintf import makebfr
from world import World
from game.utils import crapup


# long i_setup=0;
# long oddcat=0;
# long  talkfl=0;


# extern FILE * openlock();
# extern long my_str;
# extern long my_sex;
# extern long my_lev;
# extern FILE * openroom();
# extern FILE * openworld();
# extern char * pname();
# extern char * oname();
# extern long ppos();
# extern char key_buff[];

# long curch=0;
# long  curmode=0;
# long  meall=0;

#
# Data format for mud packets
#
# Sector 0
# [64 words]
# 0   Current first message pointer
# 1   Control Word
# Sectors 1-n  in pairs ie [128 words]
#
# [channel][controlword][text data]
#
# [controlword]
# 0 = Text
# - 1 = general request
#

# vcpy(dest,offd,source,offs,len)
# mstoout(block,name)

# long gurum=0;
# long convflg=0;

# sendmsg(name)
# send2(block)
# readmsg(channel,block,num)

# FILE *fl_com;
# extern long findstart();
# extern long findend();

# rte(name)
# FILE *openlock(file,perm)
# long findstart(unit)
# long findend(unit)


def talker(user):
    import logging
    logging.debug("--->\ttalker({})".format(user))
    player = Player()

    # extern long curch
    # FILE *fl;
    # char string[128];
    buff = makebfr()

    player.cms = -1
    player.puton(user)

    w = World()
    if w.openworld() is None:
        crapup("Sorry AberMUD is currently unavailable")

    logging.debug(player)
    logging.debug("{} >= {}".format(player.mynum, MAX_PLAYERS))
    if player.mynum >= MAX_PLAYERS:
        print("\nSorry AberMUD is full at the moment")
        return(0)

    player.name = user.username
    # rte(name);
    # closeworld();
    player.cms = -1
    # special(".g",name);
    i_setup = 1

    import logging
    logging.debug("Main loop")
    while True:
        buff.pbfr()
        # sendmsg(name)
        if player.rd_qd:
            pass
            # rte(name)
        player.rd_qd = False
        w.closeworld()
        buff.pbfr()

        import game.sigs
        logging.debug("Signals")
        logging.debug(game.sigs.active)
        logging.debug(game.sigs.alarm)
        logging.debug(game.sigs.SIGALRM)
        logging.debug(game.sigs.SIGALRM())

        break

# cleanup(inpbk)
# special(string,name)

# long dsdb=0;
# long moni=0;

# broad(mesg)
# tbroad(message)
# sysctrl(block,luser)

# long  bound=0;
# long  tmpimu=0;
# char  *echoback="*e";
# char  *tmpwiz=".";/* Illegal name so natural immunes are ungettable! */

# split(block,nam1,nam2,work,luser)
# trapch(chan)
# putmeon(name)
# loseme(name)

# long lasup=0;

# update(name)
# revise(cutoff)
# lookin(room)
# loodrv()

# userwrap()
# fcloselock(file)