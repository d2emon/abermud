#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  talker.py
#  
#  Copyright 2014 МихалычЪ <d2emon@mikhalych-desktop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#~ #include "files.h"
#~ #include "flock.h"

i_setup = 0
#~ long oddcat=0;
#~ long  talkfl=0;

#~ #include <stdio.h>
#~ #include <sys/errno.h>
#~ #include <sys/file.h>

#~ extern FILE * openlock();
#~ extern long curch;
#~ extern long my_str;
#~ extern long my_sex;
#~ extern long my_lev;
#~ extern FILE * openroom(); 
#~ extern FILE * openworld();
#~ extern char * pname();
#~ extern char * oname();
#~ extern long ppos();
#~ extern char key_buff[];

cms     = -1
curch   = 0
globme  = ""
curmode = 0

#~ long  meall=0;

#~ Data format for mud packets
#~ 
#~ Sector 0
#~ [64 words]
#~ 0   Current first message pointer
#~ 1   Control Word
#~ Sectors 1-n  in pairs ie [128 words]
#~ 
#~ [channel][controlword][text data]
#~ 
#~ [controlword]
#~ 0 = Text
#~ - 1 = general request
#~ 

#~ vcpy(dest,offd,source,offs,len)

#~ mstoout(block,name)

#~ long gurum=0;
#~ long convflg=0;

def sendmsg(name):
    """Sending game messages"""
    from temp_aber import debug_mode, tty, convflg, my_lev, my_str, in_fight, fighting
    from temp_aber import pvis, pname, ploc, gamecom
    
    from main import guser
    
    import gamebuffer
    import key
    import signals
    import world
    import user

    global curch, mynum, curmode

    #~ l:
    gamebuffer.pbfr()

    if tty == 4:
        btmscr()

    prmpt = key.prmpt(vis=pvis(mynum), debug=debug_mode, wiz=(my_lev > 9), convflg=convflg)

    gamebuffer.pbfr()

    if pvis(mynum) > 9999:
        pass
        #~ set_progname(0, "-csh")
        print("------------------------------------------------------------")
        print("-csh")
        print("------------------------------------------------------------")
    else:
        work = "   --}}----- ABERMUD -----{{--     Playing as {0}".format(name)
    if pvis(mynum) == 0:
        pass
        #~ set_progname(0, work)
        print("------------------------------------------------------------")
        print(work)
        print("------------------------------------------------------------")

    signals.alon()
    key.kinput(prmpt, 80)
    signals.aloff()
    work = key.buff
    if tty == 4:
        topscr()

    gamebuffer.sysbuf += "\001l"
    gamebuffer.sysbuf += work
    gamebuffer.sysbuf += "\n\001"

    world.openw()
    guser.chkMsg()
    world.closew()
    if convflg and not work == "**":
        convflg = 0
       #~ goto l;
    if not work:
        pass
        #goto nadj;
    if work != "*" and work[0] != '*':
        pass
        #~ work[0]=32
        #~ goto nadj;
    if convflg:
        w2 = work
        if convflg == 1:
            work = "say {0}".format(w2)
        else:
            work = "tss {0}".format(w2)
    #~ nadj
    if curmode == 1:
        gamecom(work)
    else:
        if (work != ".Q" and work != ".q") and work:
            a = user.special(work, name)
    if fighting > -1:
        if not pname(fighting):
            in_fight = False
            fighting = -1
        if ploc(fighting) != curch:
            in_fight = False
            fighting = -1
    if in_fight:
        in_fight -= 1
    return (not (work == ".Q")) or (not (work == ".q"))
    
#~ send2(block)

#~ readmsg(channel,block,num)

#~ FILE *fl_com;

#~ FILE *openlock(file,perm)

#~ long findstart(unit)

rd_qd = True

#~ cleanup(inpbk)

#~ long dsdb=0;

#~ long moni=0;

#~ broad(mesg)

#~ tbroad(message)

#~ sysctrl(block,luser)

#~ long  bound=0;
#~ long  tmpimu=0;
#~ char  *echoback="*e";
#~ char  *tmpwiz=".";/* Illegal name so natural immunes are ungettable! */

#~ split(block,nam1,nam2,work,luser)

#~ trapch(chan)

mynum = 0

def loseme(name):
    """Loosing the game"""
    from temp_aber import dumpitems, pvis, pname, sendsys, saveme, chksnp, setpname
    from temp_aber import zapped

    import signals
    import world

    signals.aloff() 
    #~ No interruptions while you are busy dying
    #~ ABOUT 2 MINUTES OR SO
    i_setup = 0

    unit = world.openw()
    dumpitems()
    if pvis(mynum)<10000:
        bk = "{0} has departed from AberMUDII\n".format(name)
        sendsys(name, name, -10113, 0, bk)
    setpname(mynum, "")
    world.closew()
    if not zapped:
        saveme()
    chksnp()

#~ long lasup=0;

#~ update(name)

#~ revise(cutoff)

#~ lookin(room)

#~ loodrv()

iamon = 0

#~ userwrap()

def talker(name=""):

    return 0

if __name__ == '__main__':
    talker()

