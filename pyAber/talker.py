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

cms= -1
#~ long curch=0;

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


#~ rte(name)

#~ FILE *openlock(file,perm)

#~ long findstart(unit)

#~ long findend(unit)

rd_qd = True

#~ cleanup(inpbk)

#~ special(string,name)

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

#~ putmeon(name)

def loseme(name):
    """Loosing the game"""
    from temp_aber import openworld, closeworld, dumpitems, pvis, pname, sendsys, saveme, chksnp
    from temp_aber import zapped
    from main import sig_aloff

    #~ extern long iamon;
    #~ extern long mynum;
    
    sig_aloff() 
    #~ No interruptions while you are busy dying
    #~ ABOUT 2 MINUTES OR SO
    i_setup = 0

    unit = openworld()
    dumpitems()
    if pvis(mynum)<10000:
        bk = "{0} has departed from AberMUDII\n".format(name)
        sendsys(name, name, -10113, 0, bk)
    #~ pname(mynum)[0] = 0
    closeworld()
    if not zapped:
        saveme()
    chksnp()

#~ long lasup=0;

#~ update(name)

#~ revise(cutoff)

#~ lookin(room)

#~ loodrv()

#~ long iamon=0;

#~ userwrap()

#~ fcloselock(file)

def talker(name=""):
    """This file holds the basic communications routines"""
    from main import crapup
    from bprintf import makebfr

    #~ extern long curch,cms;
    #~ extern long maxu;
    #~ extern long rd_qd;
    #~ FILE *fl;
    #~ char string[128];

    from temp_aber import putmeon, openworld, rte, closeworld, special, pbfr, sendmsg
    from temp_aber import globme, maxu
 
    makebfr()
    cms = -1
    putmeon(name);
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
        while True:
            pbfr()
            sendmsg(name)
            if rd_qd:
                rte(name)
            rd_qd = False
            closeworld()
            pbfr()
    except KeyboardInterrupt:
        from main import sig_ctrlc
        sig_ctrlc()

    return 0

if __name__ == '__main__':
    talker()

