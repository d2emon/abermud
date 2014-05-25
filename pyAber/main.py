#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

import blib

#~ char **argv_p;

def main(username):
    from talker import talker
    from temp_aber import globme, tty
    
    import key
    from support import syslog

    sig_init()
    if not username:
        raise Exception("Args!")
    print("Entering Game ...");
    tty=0;
    #~ if tty=4: initbbc(): initscr(): topscr()

    if username == "D2emon":
        globme = "The {0}".format(username)
    else:
        globme = username

    user_id = blib.cuserid()

    print("Hello {0}".format(globme))
    syslog("GAME ENTRY: {name}[{user_id}]".format(name=globme, user_id=user_id))
    key.setup()
    talker(globme)
    
    return 0

#~ char privs[4];

def crapup(str):
    """Quitting game with message"""
    from temp_aber import pbfr
    from bprintf import pr_due
    import key

    dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    pbfr()
    pr_due = 0  
    #~ So we dont get a prompt after the exit
    key.setback()
    print("\n{0}\n\n{1}\n\n{0}\n".format(dashes, str))
    exit(0)
    
def listfl(name):
    """List file"""
    print(">>>listfl({0})".format(name))

def getkbd(s, l):
    """Getstr() with length limit and filter ctrl"""
    print(">>>getkbd({0}, {1})".format(s, l))

#~ import signal
import atexit

sig_active=0;

def sig_alon():
    """Set signals on"""
    print(">>>sig_alon()")

def unblock_alarm():
    """Unblock alarm"""
    print(">>>unblock_alarm()")

def block_alarm():
    """Block alarm"""
    print(">>>block_alarm()")

def sig_aloff():
    "Stopping all signals"
    sig_active=0;   

    sigs = {'alrm':0}
    print(sigs)

    #~ signal(SIGALRM,SIG_IGN);
    #~ alarm(2147487643);
    pass    

#~ long interrupt=0;

def sig_occur():
    """Signal occured"""
    print(">>>sig_occur()")

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
    from temp_aber import globme
    from talker import loseme
    import key

    sig_aloff();
    loseme(globme);
    key.setback();
    print("Ooops")

def sig_ctrlc():
    "Quitting on Ctrl+C"
    from talker import loseme
    from temp_aber import in_fight

    if in_fight:
        return

    sig_aloff();
    loseme();
    atexit.unregister(sig_oops)
    crapup("Byeeeeeeeeee  ...........")
    
def set_progname(n,text):
    """Program name set"""
    print(">>>set_progname({0}, {1})".format(n,text))

if __name__ == '__main__':
    main("D2emon")

