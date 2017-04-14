'''

                AberMUD II   C


        This game systems, its code scenario and design
        are (C) 1987/88  Alan Cox,Jim Finnis,Richard Acott


        This file holds the basic communications routines

'''
from d2log import logger
from player.models import MAX_PLAYERS
from bprintf import makebfr
from world import World
# from game.utils import crapup
from game.share import player  # , load


# long oddcat=0;
# long  talkfl=0;

# extern long my_str;
# extern long my_sex;
# extern long my_lev;
# extern FILE * openroom();
# extern long ppos();
# extern char key_buff[];

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

def talker(user):
    logger.debug("--->\ttalker({})".format(user))

    # player = Player()
    # load(user)

    buff = makebfr()
    logger.debug("Player init %s", player)

    player.cms = -1
    player.puton(user)

    logger.debug("Player puton %s", player)
    # logger.debug("Buffer puton %s", buff)

    w = World()
    assert w.filrf is not None, "Sorry AberMUD is currently unavailable"

    logger.debug("{} >= {}".format(player.mynum, MAX_PLAYERS))
    # assert player.mynum < MAX_PLAYERS, "Sorry AberMUD is full at the moment"

    player.name = user.username
    player.rte()
    player.save(w)

    logger.debug("Player saved %s", player)
    # logger.debug("Buffer saved %s", buff)

    player.cms = -1
    # player.special(".g")
    player.player_load()
    i_setup = 1

    logger.debug("Player loaded %s", player)
    # logger.debug("Buffer loaded %s", buff)
    logger.debug("Main loop")
    logger.debug('<!' + '-'*40)
    # while True:
    for t in range(5):
        logger.debug('<!' + '-'*20)
        buff.pbfr()

        buff.sendmsg(player)
        logger.debug("Player sendmsg %s", player)
        # logger.debug("Buffer sendmsg %s", buff)

        if player.rd_qd:
            player.rte()
        player.rd_qd = False
        logger.debug("Player rte %s", player)
        # logger.debug("Buffer rte %s", buff)

        player.save(w)
        buff.pbfr()
        logger.debug("Player saved %s", player)
        # logger.debug("Buffer saved %s", buff)

        print_sigs()
        logger.debug('-'*20 + '>')
    logger.debug('-'*40 + '>')


def print_sigs():
    import game.sigs
    logger.debug('='*4)
    # logger.debug("Signals")
    # logger.debug("SIGALRM:\t%s", game.sigs.alarm.sig)
    # logger.debug("SIGHUP:\t%s", game.sigs.SIGHUP)
    # logger.debug("SIGINT:\t%s", game.sigs.SIGINT)
    # logger.debug("SIGTERM:\t%s", game.sigs.SIGTERM)
    # logger.debug("SIGTSTP:\t%s", game.sigs.SIGTSTP)
    # logger.debug("SIGQUIT:\t%s", game.sigs.SIGQUIT)
    # logger.debug("SIGCONT:\t%s", game.sigs.SIGCONT)
    # logger.debug('-'*4)
    logger.debug("Active:\t%s", game.sigs.alarm.active)
    logger.debug("Alarm:\t%d", game.sigs.alarm.timer)
    logger.debug("Function:\t%s", game.sigs.alarm.sig)
    logger.debug("Interrupt:\t%d", game.sigs.interrupt)
    a = game.sigs.alarm.sig
    if a is not None:
        a()
    logger.debug('='*4)

    from game.utils import PROGNAME
    logger.debug("Progname:\t%s", PROGNAME)
    logger.debug('='*4)

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
# loseme(name)

# lookin(room)
# loodrv()

# userwrap()
# fcloselock(file)
