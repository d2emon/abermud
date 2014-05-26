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

cms   = -1
curch = 0

#~ char globme[40];
#~ long  curmode=0;
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

#~ sendmsg(name)

#~ send2(block)

#~ readmsg(channel,block,num)

#~ FILE *fl_com;


def rte(name):
    """Read messages"""
    from temp_aber import openworld, findend, readmsg, mstoout
    #~ extern long cms;
    #~ extern long vdes,tdes,rdes;
    #~ extern FILE *fl_com;
    #~ extern long debug_mode;
    #~ long too,ct,block[128];
    global cms

    unit   = openworld()
    fl_com = unit
    if not unit:
        crapup("AberMUD: FILE_ACCESS : Access failed")
        raise Exception("AberMUD: FILE_ACCESS : Access failed")

    too = findend(unit) + 1
    if cms == -1:
        cms = too

    ct  = cms
    for ct in range(cms, too):
        readmsg(unit, block, ct)
        mstoout(block, name)
    #~ update(name);
    #~ eorte();

    rdes = 0
    tdes = 0
    vdes = 0
    
    print(">>>rte({0})".format(name))

#~ FILE *openlock(file,perm)

#~ long findstart(unit)

#~ long findend(unit)

rd_qd = True

#~ cleanup(inpbk)

def special(string, name):
    """Special functions"""
    from temp_aber import openworld, setpstr, setplev, setpvis, setpwpn, setpsexall, setphelping, initme, cuserid, sendsys, randperc, trapch
    from temp_aber import my_str, my_lev, my_sex

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
        ufl = openworld()
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
    from temp_aber import openworld, setploc, setppos, setplev, setpvis, setpstr, setpwpn, setpsex, fpbn, pname, setpname
    from temp_aber import maxu

    from main import crapup

    global mynum, curch
    
    #~ extern long mynum,curch;

    iamon = False
    unit  = openworld()
    
    if fpbn(name)!= -1:
        crapup("You are already on the system - you may only be on once at a time")
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
    from temp_aber import openworld, closeworld, dumpitems, pvis, pname, sendsys, saveme, chksnp, setpname
    from temp_aber import zapped

    import signals

    signals.aloff() 
    #~ No interruptions while you are busy dying
    #~ ABOUT 2 MINUTES OR SO
    i_setup = 0

    unit = openworld()
    dumpitems()
    if pvis(mynum)<10000:
        bk = "{0} has departed from AberMUDII\n".format(name)
        sendsys(name, name, -10113, 0, bk)
    setpname(mynum, "")
    closeworld()
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
    """This file holds the basic communications routines"""
    #~ extern long curch,cms;
    #~ extern long maxu;
    #~ extern long rd_qd;
    #~ FILE *fl;
    #~ char string[128];

    from temp_aber import openworld, rte, closeworld, sendmsg
    from temp_aber import globme, maxu

    from main import crapup
    import bprintf
    import signals

    global cms, rd_qd, mynum
 
    bprintf.makebfr()
    cms = -1
    putmeon(name)
    if not openworld():
        crapup("Sorry AberMUD is currently unavailable")
        raise Exception("Sorry AberMUD is currently unavailable")
    if mynum >= maxu:
        crapup("Sorry AberMUD is full at the moment")
        raise Exception("Sorry AberMUD is full at the moment")
    globme = name
    rte(name)
    closeworld()
    cms= -1
    special(".g",name)
    i_setup = 1
    try:
        i = 0
        for i in range(0, 2):
            bprintf.pbfr()
            sendmsg(name)
            if rd_qd:
                rte(name)
            rd_qd = False
            closeworld()
            bprintf.pbfr()

            if signals.sigs['alrm']:
                print("[SIGNAL BEGIN]")
                signals.occur()
                print("[SIGNAL END]")
    except KeyboardInterrupt:
        signals.ctrlc()

    return 0

if __name__ == '__main__':
    talker()

