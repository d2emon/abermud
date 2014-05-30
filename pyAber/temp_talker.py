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
    
    import gamebuffer
    import key
    import signals
    import world

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
    rte(name)
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
        if (work != ".Q" and work != ".q") and worker:
            a = special(work, name)
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


def rte(name):
    """Read messages"""
    from temp_aber import readmsg, mstoout, update, eorte
    import world
    
    #~ extern long cms;
    #~ extern long vdes,tdes,rdes;
    #~ extern FILE *fl_com;
    #~ extern long debug_mode;
    #~ long too,ct,block[128];
    global cms

    unit   = world.openw()
    fl_com = unit
    if not unit:
        crapup("AberMUD: FILE_ACCESS : Access failed")
        raise Exception("AberMUD: FILE_ACCESS : Access failed")

    too = world.findend(unit) + 1
    if cms == -1:
        cms = too

    ct  = cms
    for ct in range(cms, too):
        readmsg(unit, block, ct)
        mstoout(block, name)
    update(name)
    eorte()

    rdes = 0
    tdes = 0
    vdes = 0

#~ FILE *openlock(file,perm)

#~ long findstart(unit)

rd_qd = True

#~ cleanup(inpbk)

def special(string, name):
    """Special functions"""
    from temp_aber import setpstr, setplev, setpvis, setpwpn, setpsexall, setphelping, initme, cuserid, sendsys, randperc, trapch
    from temp_aber import my_str, my_lev, my_sex

    import world
    
    global mynum, curmode, curch

    #~ extern long curmode;
    #~ extern long curch,moni;
    #~ extern long my_sco
    #~ char xx[128];
    #~ char xy[128];
    #~ char us[32];

    bk = string.lower()
    ch = bk[0]
    if ch != '.':
        return False
    ch = bk[1]

    if ch == 'g':
        curmode = 1
        curch   = -5
        initme()
        ufl = world.openw()
        setpstr(mynum, my_str)
        setplev(mynum, my_lev)
        if my_lev < 10000:
            setpvis(mynum, 0)
        else:
            setpvis(mynum, 10000)
        setpwpn(mynum,-1)
        setpsexall(mynum,my_sex)
        setphelping(mynum,-1)
        cuserid()
        xy = "\001s{0}\001{1}  has entered the game\n\001".format(name, name)
        xx = "\001s{0}\001[ {1}  has entered the game ]\n\001".format(name, name)
        sendsys(name, name, -10113, curch, xx)
        rte(name)
        if randperc() > 50:
            trapch(-5)
        else:
            curch = -183
            trapch(-183)
        sendsys(name, name, -10000, curch, xy)
    else:
        print("Unknown . option")

    return True

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

def putmeon(name):
    """TODO : Put player on"""
    from temp_aber import setploc, setppos, setplev, setpvis, setpstr, setpwpn, setpsex, fpbn, pname, setpname
    from temp_aber import maxu

    import gamesys
    import world

    global mynum, curch
    
    #~ extern long mynum,curch;

    iamon = False
    unit  = world.openw()
    
    if fpbn(name)!= -1:
        gamesys.crapup("You are already on the system - you may only be on once at a time")
        raise Exception("You are already on the system - you may only be on once at a time")

    ct = 0
    for ct in range(0, maxu+1):
        if not pname(ct):
            break

    if ct == maxu:
        mynum = maxu
        return False

    setpname(ct, name)
    setploc(ct, curch)
    setppos(ct, -1)
    setplev(ct,  1)
    setpvis(ct,  0)
    setpstr(ct, -1)
    setpwpn(ct, -1)
    setpsex(ct,  0)
    mynum = ct

    iamon = True
    return iamon    
    
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

