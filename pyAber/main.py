#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  без имени.py
#  
#  Copyright 2014 МихалычЪ <МихалычЪ@PC>
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

#~ char **argv_p;

def main(username):
    from temp_aber import syslog, keysetup, talker, cuserid
    from temp_aber import globme, tty

    sig_init()
    if not username:
        raise Exception("Args!")
    print("Entering Game ....\n");
    tty=0;
    #~ if tty=4: initbbc(): initscr(): topscr()

    if username == "D2emon":
        globme = "The {0}".format(username)
    else:
	    globme = username

    print("Hello {0}\n".format(globme))
    syslog("GAME ENTRY: {name}[{user_id}]".format(name=globme, user_id=cuserid()))
    keysetup()
    talker(globme)
	
    return 0

#~ char privs[4];

def crapup(str):
	"""Quitting game with message"""
    #~ extern long pr_due;
    #~ static char *dashes =
    #~ "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-";
    #~ pbfr();
    #~ pr_due=0;  /* So we dont get a prompt after the exit */ 
    #~ keysetback();
    #~ printf("\n%s\n\n%s\n\n%s\n", dashes, str, dashes);
    exit(0)

#~ listfl(name)
#~ char *getkbd(s,l)   /* Getstr() with length limit and filter ctrl */

#~ import signal

import atexit

sig_active=0;

#~ sig_alon()
#~ unblock_alarm()
#~ block_alarm()

def sig_aloff():
    "Stopping all signals"
    sig_active=0;	
    #~ signal(SIGALRM,SIG_IGN);
    #~ alarm(2147487643);
    print("sig_aloff")    

#~ long interrupt=0;
#~ sig_occur()

def sig_init():
    "Initialization if signals"
    sigs = {'int':'sig_ctrlc', 'term':'sig_ctrlc'}
    print(sigs)

    atexit.register(sig_oops)
    
	#~ signal(SIGHUP,sig_oops);
	#~ signal(SIGINT,sig_ctrlc);
	#~ signal(SIGTERM,sig_ctrlc);
	#~ signal(SIGTSTP,SIG_IGN);
	#~ signal(SIGQUIT,SIG_IGN);
    #~ signal(SIGCONT,sig_oops);
    pass

def sig_oops(is_ctrlc = False):
    "Quitting"
    from temp_aber import loseme, keysetback

    sig_aloff();
    loseme();
    keysetback();
    print("Ooops")

def sig_ctrlc():
    "Quitting on Ctrl+C"
    from temp_aber import loseme, crapup
    from temp_aber import in_fight

    if in_fight:
        return

    sig_aloff();
    loseme();
    atexit.unregister(sig_oops)
    crapup("Byeeeeeeeeee  ...........")
	
#~ set_progname(n,text)

if __name__ == '__main__':
    main("D2emon")

