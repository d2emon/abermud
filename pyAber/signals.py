#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  signals.py
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

#~ import signal
import atexit

active    = False
sigs      = {}
alarm     = 0
interrupt = False

def block_alarm():
    """Block alarm"""
    global sigs
    
    #~ signal(SIGALRM,SIG_IGN);
    sigs['alrm'] = 0
    print(sigs)

def unblock_alarm():
    """Unblock alarm"""
    global sigs, active, alarm
    
    #~ signal(SIGALRM,sig_occur);
    sigs['alrm'] = 'sig_occur'
    print(sigs)
    if active:
        alarm = 2
        #~ alarm(2)

def alon():
    """Set signals on"""
    global sigs, active, alarm
    
    active = True   
    #~ signal(SIGALRM,sig_occur);
    sigs['alrm'] = 'sig_occur'
    print(sigs)
    print(active)
    #~ alarm(2)
    alarm = 2

def aloff():
    """Stopping signals"""
    global sigs, active, alarm
    
    active = False   
    #~ signal(SIGALRM,SIG_IGN);
    sigs['alrm'] = 0
    print(sigs)
    print(active)
    #~ alarm(2147487643)
    alarm = 2147487643

def init():
    "Initialization if signals"
    global sigs
    
    atexit.register(oops)
    
    #~ signal(SIGHUP,sig_oops);
    #~ signal(SIGINT,sig_ctrlc);
    #~ signal(SIGTERM,sig_ctrlc);
    #~ signal(SIGTSTP,SIG_IGN);
    #~ signal(SIGQUIT,SIG_IGN);
    #~ signal(SIGCONT,sig_oops);
    sigs['hup']  = 'oops'
    sigs['int']  = 'ctrlc'
    sigs['term'] = 'ctrlc'
    sigs['tstp'] = 0
    sigs['quit'] = 0
    sigs['cont'] = 'oops'
    print(sigs)

def sloop():
    """Signals loop"""
    global sigs
    
    if sigs['alrm']:
        print("[SIGNAL BEGIN]")
        occur()
        print("[SIGNAL END]")

def occur():
    """Signal occured"""
    from temp_aber import on_timing

    import user
    import world
    import key

    global active, interrupt

    if not active:
        return 0
    aloff()
    world.openw()
    interrupt = True
    user.chkMsg(user.username)
    interrupt = False
    on_timing()
    world.closew()
    key.reprint()
    alon()

def oops():
    "Quitting"
    from temp_talker import loseme

    from main import guser;

    import key
    import user

    aloff()
    if(guser) :
        loseme(guser.name)
    key.setback()
    print("Ooops")

def ctrlc():
    "Quitting on Ctrl+C"
    from temp_aber import in_fight
    from temp_talker import loseme

    from main import guser
    
    import gamesys

    if in_fight:
        return

    atexit.unregister(oops)
    aloff()
    if guser :
        loseme(guser.name)
    else :
        loseme("guser.name")
    gamesys.crapup("Byeeeeeeeeee  ...........")

def main():
    """Functions to work with signals"""
    print("Functions to work with signals")
    return 0

if __name__ == '__main__':
    main()

